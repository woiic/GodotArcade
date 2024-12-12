import requests as rq
import json
import os
from PIL import Image
import numpy as np

import base64
from io import BytesIO



API_Key = "xxxxxxxxxxxxxxxxxxxx" ## My api key to the dcc api
test="tokenAuth"
api_direction = "https://api.dcc.uchile.cl/personas/"
def getAPIuserINFO(user_info):
    parameters = {
        "rut":"12345678-9"

    }

    headers = {
        "Authorization":"Token "+API_Key
    }
    Security = {
        "tokenAuth": API_Key,
        "basicAuth": "",
        "cookieAuth": ""
    }
    #res = rq.get("https://api.dcc.uchile.cl/personas/",params=parameters,headers=headers,security=Security)
    res = rq.get("https://api.dcc.uchile.cl/personas/",params=parameters,headers=headers)
    print("res = " + str(res))
    inJson = json.loads(res.text)
    print("in json = " + str(inJson))
    return inJson

def getAPIuserINFO_byRUT(in_rut):
    parameters = {
        "rut":str(in_rut)
    }
    headers = {
        "Authorization":"Token "+API_Key
    }
    
    res = rq.get(api_direction,params=parameters,headers=headers)
    #print(res.text)
    if res.status_code == 200:
        inJson = json.loads(res.text)
        #print("in json = " + str(inJson))
        in_dict = inJson[0]
        in_dict["status"] = "OK"
        return inJson[0]
    else:
        inJson = json.loads(res.text)
        inJson["status"] = "error"
        return inJson

def savePFP(coded_img, img_direction=""): # "pro file photo"
    base64_str = coded_img
    print("a")
    image_data = base64.b64decode(base64_str)
    print("b")
    image = BytesIO(image_data)
    print("c")
    img = Image.open(image)
    print("d")
    if img_direction.lower().endswith(".png"):
        img.save(img_direction)
    else:
        file_path = os.path.realpath(__file__)
        img.save(file_path[0:len(file_path) -7] + "ProfilePicture/profileImg.png")
        return "ProfilePicture/profileImg.png"
    return img_direction
