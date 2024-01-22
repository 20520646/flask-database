from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from flask import Blueprint

giangvien = Blueprint("giangvien",__name__, static_folder="", template_folder="")


client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]

CORS(giangvien)

@giangvien.route('/giangvien/<MaGV>',methods= ['GET','POST'])
def get_giangvien(MaGV):
    giangvien_all = list(GiangVien_collection.find({"MaGv":MaGV}))
    if LopMonHoc_collection.find({"MaGV":MaGV}):
        lophoc_all = LopMonHoc_collection.find({"MaGV":MaGV})
        malmh = []
        for lmh in lophoc_all:
            mlmh = lmh["MaLMH"]
            malmh.append({"MaLMH":mlmh})
    converted_students = json_util.dumps({"Thong tin giang vien":giangvien_all,
                                          "MaLMH":malmh})
    return converted_students, 200, {'Content-Type': 'application/json'}