from src.common import test_sql
from src.common.dbserver import mysqldb
import random, time


def qy_amount_open(req_phone, req_amount):
    open_loan = test_sql.open_qy(str(req_phone), str(req_amount), str("che001"))
    qy_loan_id = open_loan['items'][0]
    business_id = "QA" + str(random.randrange(100000, 999999, 5))
    if str(open_loan['successful']) == 'True':
        user_type_sql = 'select type from user where tel_num="' + str(req_phone) + '"'
        user_type = mysqldb('qyddb').selectsql(user_type_sql)
        if str(user_type[0]['type']) == 'Company':
            borrower_type = '企业用户'
        else:
            borrower_type = '个人用户'
        first_audit_data = test_sql.first_audit(qy_loan_id, business_id)
        if str(first_audit_data) == 'SUCCESS':
            receive_task = test_sql.receive_task(qy_loan_id)
            if str(receive_task) == 'SUCCESS':
                second_audit = test_sql.second_audit(qy_loan_id, business_id)
                if str(second_audit['msg']) == 'SUCCESS':
                    result = second_audit['msg']
                    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    """增加测试数据入库步骤：成功"""
                    insert_sql = 'insert into zt_testdata_record (phone, business_type, data_type, data_money, ' \
                                 'data_to_student, createTime, data_remark) VALUES ("' + req_phone + '",' \
                                 '"开青盈标", "'+str(borrower_type)+'", "' + req_amount + '", "' + str(req_phone) + '", "' + \
                                 str(createTime) + '", "Ui自动化产生的青盈开标数据")'
                    exec_result = mysqldb("Azure_qa_testdata").updatesql(insert_sql)
                    print(exec_result)
                else:
                    result = '复审失败！！！'
                    createTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    """增加测试数据入库步骤：失败"""
                    insert_sql = 'insert into zt_testdata_record (phone, business_type, data_type, data_money, ' \
                                 'data_to_student, createTime, data_remark) VALUES ("' + req_phone + '",' \
                                 '"开青盈标", "' + str(borrower_type) + '", "' + req_amount + '", "' + str(req_phone) + '", "' + \
                                 str(createTime) + '", "' + str(result) + '")'
                    exec_result = mysqldb("Azure_qa_testdata").updatesql(insert_sql)
                    print(exec_result)
            else:
                result = '复审认领任务失败！！！'
        else:
            result = '初审失败！！！'
    else:
        result = '开标失败！！！'
    return result
