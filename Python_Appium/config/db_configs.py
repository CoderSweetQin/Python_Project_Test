import pymysql
DEBUG = True

"""azure_QA环境：test"""
testdb = dict(host='172.15.00.17', user='platform', passwd='platform2018', db='testproduction', charset='utf8', port=23306, cursorclass=pymysql.cursors.DictCursor)


"""azure_QA环境：new_test"""
testnewdb = dict(host='172.15.00.17', user='platform', passwd='platform2018', db='testnewproduction', charset='utf8',port=23306, cursorclass=pymysql.cursors.DictCursor)


"""azure_QA环境：test账务系统"""
testaccount = dict(host='172.15.00.17', user='platform', passwd='platform2018', db='testAccount', charset='utf8', port=23306, cursorclass=pymysql.cursors.DictCursor)


"""azure_QA环境：交易网关"""
transaction = dict(host='172.15.00.17', user='platform', passwd='platform2018', db='paycenter', charset='utf8', port=23306, cursorclass=pymysql.cursors.DictCursor)

"""azure_QA环境：个人企业测试数据入库"""
Azure_qa_testdata = dict(host='172.15.00.10', user='root', passwd='root', db='test', charset='utf8', port=3307, cursorclass=pymysql.cursors.DictCursor)

