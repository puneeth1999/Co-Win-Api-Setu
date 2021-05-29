import http.client
import json
import hashlib
from variables import mobile, beneficiary_id

def requestOTP(mobile):
    mobile = str(mobile)
    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = json.dumps({
        "mobile": mobile
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/v2/auth/public/generateOTP", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print('requestOTP(mobile) - data:', data.decode("utf-8"))
    return data.decode("utf-8")


def sha_hash(otp):
    str = otp
    result = hashlib.sha256(str.encode())
    hexdecimal = result.hexdigest()
    # print('hexdecimal:', hexdecimal)
    return hexdecimal


def confirmOTP(otp, txnID):

    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = json.dumps({
        "otp": str(otp),
        "txnId": str(txnID)
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api/v2/auth/public/confirmOTP", payload, headers)
    res = conn.getresponse()
    data = res.read()
    # print('confirmOTP(mobile) - data:',data.decode("utf-8"))
    return data.decode("utf-8")



def getCertificate(token, beneficiary_id):

    conn = http.client.HTTPSConnection("cdn-api.co-vin.in")
    payload = ''
    headers = {
        'Authorization': 'Bearer {}'.format(token)
    }
    conn.request("GET", "/api/v2/registration/certificate/public/download?beneficiary_reference_id={}".format(beneficiary_id), payload,
                 headers)
    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    return data.decode("utf-8")



##################################### MAIN SCRIPT ###################################################


txn_id = requestOTP(mobile)
txn_id = json.loads(txn_id)
txn_id = txn_id["txnId"]


# try:
#     txn_id = json.loads(txn_id)
#     txn_id = txn_id["txnId"]
#     print('try - txn_ID',txn_id, '\n\n')
# except Exception as e:
#     print(e)
#     txn_id = txn_id["txnId"]
#     print('except - txn_ID', txn_id, '\n\n')




otp = str(input('Enter the OTP: '))
otp = sha_hash(otp)
token = confirmOTP(otp, txn_id)
token = json.loads(token)
token = token['token']
print('token:',token, '\n\n')



print(getCertificate(token, beneficiary_id))
