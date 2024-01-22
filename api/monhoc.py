from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from flask import Blueprint

monhoc = Blueprint("monhoc",__name__)


client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]

CORS(monhoc)
@monhoc.route('/monhoc/<MaSV>',methods= ['GET','POST'])
def get_monhoc(MaSV):
    if SinhVien_collection.find({"MaSV":MaSV}):
        all_monhoc = list(MonHoc_collection.find())
        converted_students = json_util.dumps(all_monhoc)
        return converted_students, 200, {'Content-Type': 'application/json'}

@monhoc.route('/monhoc/<MaSV>/<MaLMH>',methods= ['GET','POST'])
def get_lopmonhoc(MaSV,MaLMH):
    if SinhVien_collection.find({"MaSV":MaSV}):
        if LopMonHoc_collection.find({"MaLMH":MaLMH}):
            all_Lopmonhoc = LopMonHoc_collection.find({"MaLMH":MaLMH})
        converted_students = json_util.dumps(all_Lopmonhoc)
        return converted_students, 200, {'Content-Type': 'application/json'}