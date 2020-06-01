from config import url
import base64
import json
import requests


def qyd_front_login(username, passwd):
    """轻易贷前端登录"""
    qyd_front_login_url = url.host_qyd_front_login
    headers = {"Content-Type": "application/json"}
    token = base64.b64encode((username+":"+passwd).encode("utf-8"))
    data = 'Basic %s' % token
    data = data.replace("'", "").replace("b", "")
    body = {}
    body["authorization"] = data
    data_json = json.dumps(body)
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=qyd_front_login_url, data=data_json, headers=headers, verify=False).json()
    print(r)
    return r["entities"][0]["xAuthToken"]


def qyd_app_login(username, passwd):
    """轻易贷APP登录"""
    qyd_front_login_url = url.host_qyd_app_login
    app_login_param = {
        "appversion": "3.8.5",
        "imei": "864328033646159",
        "sysversion": "6.0.1",
        "appmac": "02:00:00:00:00:00",
        "imsi": "IMSI",
        "height": "1920",
        "width": "1080",
        "system": "ANDROID",
        "loginWay": "1",
        "channel": "2",
        "deviceId": "864328033646159",
        "deviceName": "OPPO R9s",
        "ip": "172.16.80.111",
        "authorization": "Basic MTY4NjYwNjYxMTA6Y2hlMDAx"
    }
    headers = {"Content-Type": "application/json"}
    token = base64.b64encode((username + ":" + passwd).encode("utf-8"))
    data = 'Basic %s' % token
    data = data.replace("'", "").replace("b", "")
    app_login_param["authorization"] = data
    data_json = json.dumps(app_login_param)
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=qyd_front_login_url, data=data_json, headers=headers, verify=False).json()
    # print(r["mapData"]["xAuthToken"])
    return r["mapData"]["xAuthToken"]
# qyd_app_login("16866066110","che001")


def submit_token():
    """轻盈开标：申请借款获取submitToken值接口"""
    urls = url.host_qy_submit_token
    data = {}
    r = requests.post(url=urls, json=data, verify=False).json()
    return r["entities"][0]["submitToken"]


def open_qy(username, amount, password):
    """轻盈标的生成：借款申请接口"""
    urls = url.host_qy_open
    data = {
        "submitToken": str(submit_token()),
        "amount": str(amount),
        "debtType": "CAR_BORROW",
        "tenderName": "购车贷",
        "debitTerm": 180,
        "interestRate": 4.25,
        "remark": "轻盈借款申请1111"
    }
    headers = {
        "Content-Type": "application/json",
        "X-Auth-Token": qyd_front_login(username, password)
    }
    result = requests.post(url=urls, json=data, headers=headers, verify=False).json()
    return result


def login_backed():
    username = "admin"
    password = "ultche001"
    auth = username + ":" + password
    headers = {"Content-Type": "application/json",
               "authorization": "Basic " + base64.b64encode(auth.encode(encoding="utf-8")).decode(encoding='utf-8')}
    head = requests.get(url=url.host_admin_login, headers=headers)
    return head.headers['X-Auth-Token']


def first_audit(qy_loan_id, bussinessId):
    """轻盈标的借款申请成功后：初审"""
    urls = url.host_qy_first_audit
    data = {
        "id": str(qy_loan_id),
        "borrowType": "CAR_BORROW",
        "businessId": str(bussinessId),
        "isYYD": "0",
        "status": "0",
        "description": "",
        "openNow": 0
    }
    headers = {"Content-Type": "application/json",
               "x-auth-token": login_backed()
               }
    r = requests.post(url=urls, json=data, headers=headers, verify=False).json()
    return r["msg"]


def receive_task(qy_loan_id):
    """轻盈标的借款申请成功后：初审，复审认领任务"""
    urls = url.host_qy_receiveTask
    data = {
        "id": str(qy_loan_id)
    }
    headers = {"Content-Type": "application/json",
               "x-auth-token": login_backed()
               }
    r = requests.post(url=urls, json=data, headers=headers, verify=False).json()
    return r["msg"]


def second_audit(qy_loan_id, businessId):
    """轻盈标的借款申请成功后：复审"""
    urls = url.host_qy_secondAudit
    data = {
        "id": str(qy_loan_id),
        "borrowType": "CAR_BORROW",
        "businessId": str(businessId),
        "isYYD": "0",
        "status": "0",
        "description": "轻盈复审申请通过",
        "openNow": 1
    }
    headers = {"Content-Type": "application/json",
               "x-auth-token": login_backed()
               }
    r = requests.post(url=urls, json=data, headers=headers, verify=False).json()
    return r