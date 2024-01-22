from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from flask import Blueprint

user = Blueprint("user",__name__)


client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]

CORS(user)
@user.route('/home/<MaSV>',methods= ['GET','POST'])
def get_students(MaSV):
    all_Lopmonhoc =[]
    mssv = SinhVien_collection.find({"MaSV":MaSV})
    name = [st["TenSV"] for st in mssv]
    for lmh in LopMonHoc_collection.find():
        for gv in GiangVien_collection.find():
            if lmh["MaGV"] == gv["MaGv"]:
                all_Lopmonhoc.append({
                    "LopMonHoc":lmh["MaLMH"],
                    "TenMonHoc":lmh["TenLMH"],
                    "TenGiangVien":gv["TenGV"]
                })
    converted = json_util.dumps({"TenSV":name,
                                "MonHoc":all_Lopmonhoc})
    return converted, 200, {'Content-Type': 'application/json'}
@user.route('/students/<MaSV>',methods= ['GET','POST'])
def get_student(MaSV):
    all_phuhuynh = PhuHuynh_collection.find({"MaSV": MaSV})
    all_sinhvien = SinhVien_collection.find({"MaSV":MaSV})
    converted_students = json_util.dumps({"Thong tin sinh vien":all_sinhvien,
                                         "Thong tin phu huynh":all_phuhuynh})
    return converted_students, 200, {'Content-Type': 'application/json'} 