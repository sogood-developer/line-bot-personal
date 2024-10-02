import requests

url = "https://api.sms-activate.org/stubs/handler_api.php?"

apikey = "c0f1508592bd4cd0edbc4299A28de43d"

def generatePhoneNumber(country="6"): # 6 = indo, 52 = thai
    params = {
        "api_key": apikey,
        "action": "getNumber",
        "service": "me",
        "country": country
    }
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    result = requests.get(url, params=params, headers=headers).text.split(":")
    
    if result[0] == "ACCESS_NUMBER":
        return {"status":result[0], "otpid": result[1], "number": result[2].replace("66","0",1)}
    
    # raise Exception(result[0])

    else:
        print(result)
        return {"status":result[0]}

def getPhonePincode(order_id):
    params = {
        "api_key": apikey,
        "action": "getStatus",
        "id": order_id
    }
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    result = requests.get(url, params=params, headers=headers).text.split(":")
    if result[0] == "STATUS_OK":
        return {"status":result[0], "otp": result[1]}
    else:
        return {"status":result[0]}

def completeActivation(order_id):
    params = {
        "api_key": apikey,
        "action": "setStatus",
        "id": order_id,
        "status": "6"
    }
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    result = requests.get(url, params=params, headers=headers).text.split(":")
    if result[0] == "ACCESS_ACTIVATION":
        return True
    else:return False

def resendActivationCode(order_id):
    params = {
        "api_key": apikey,
        "action": "setStatus",
        "id": order_id,
        "status": "3"
    }
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    result = requests.get(url, params=params, headers=headers).text.split(":")
    return {"status":result[0]}

def cancelActivation(order_id):
    params = {
        "api_key": apikey,
        "action": "setStatus",
        "id": order_id,
        "status": "8"
    }
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"}
    result = requests.get(url, params=params, headers=headers).text.split(":")
    if result[0] == "ACCESS_CANCEL":
        return True
    else:return False