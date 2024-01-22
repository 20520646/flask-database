from flask import request
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from flask import Blueprint

login = Blueprint("login",__name__, static_folder="", template_folder="")


client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]

CORS(login)
@login.route('/login',methods= ['GET','POST'])    
def login_account():
    data = request.get_json()
    username = data.get('id')
    password = data.get('password')
    
    if username and password :
        for sv in SinhVien_collection.find():
            if sv["TenDN"] == username and sv["MK"] == password:
                converted = json_util.dumps({"isCorrect":True,
                                             "typeAccount":"sv"})
                return converted, 200, {'Content-Type': 'application/json'}

        for gv in GiangVien_collection.find():
            if gv["TenDN"] == username and gv["MK"] == password:
                converted = json_util.dumps({"isCorrect":True,
                                             "typeAccount":"gv"})
                return converted, 200, {'Content-Type': 'application/json'}

        for ph in PhuHuynh_collection.find():
            if ph["TenDN"] == username and ph["MK"] == password:
                converted = json_util.dumps({"isCorrect":True, "typeAccount":"ph"})
                return converted, 200, {'Content-Type': 'application/json'}

    converted = json_util.dumps({"isCorrect":False}) 
    return converted, 200, {'Content-Type': 'application/json'}
