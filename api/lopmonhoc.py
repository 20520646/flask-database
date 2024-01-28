from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from flask import Blueprint
from datetime import datetime,timedelta

lopmonhoc = Blueprint("lopmonhoc",__name__, static_folder="", template_folder="")


client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]
DiemSo_colection = database["DiemSo"]
Diemdanh_colection = database["DiemDanh"]

CORS(lopmonhoc)
@lopmonhoc.route('/lopmonhoc/<MaLMH>',methods= ['GET','POST'])    
def get_lmh(MaLMH):
    dsdiemdanh = []
    thoi_gian_hien_tai = datetime.now()
    for a in list(Diemdanh_colection.find({"LopMH":MaLMH})):
        if thoi_gian_hien_tai.date() == a["Thoi gian diem danh"].date():
            dsdiemdanh.append(a)
   
    if LopMonHoc_collection.find({"MaLMH":MaLMH}):
        Lopmonhoc_all = list(LopMonHoc_collection.find({"MaLMH":MaLMH}))
    if SinhVien_collection.find({"Lop":MaLMH}):
        sinhvien_all= list(SinhVien_collection.find())
        all_buoihoc = BuoiHoc_collection.find({"MaLMH":MaLMH})
        sinhvien1 = []
        for sv in sinhvien_all:
            all_diem = DiemSo_colection.find({"MaLMH":MaLMH,"MaSV":sv["MaSV"]})
            for diem in all_diem:
                diemm = diem["Diem"]
            _id = sv["_id"]
            MaSV = sv["MaSV"]
            TenSV = sv["TenSV"]
            sinhvien1.append({"_id":_id,"MaSV":MaSV,"TenSV": TenSV,"Diem":diemm})
    converted_courses = json_util.dumps({"Thong tin lop hoc":Lopmonhoc_all,
                                         "Thong tin sinh vien":sinhvien1,
                                         "Thong tin buoi hoc":all_buoihoc,
                                         "Danh sach sv diem danh":dsdiemdanh})
    return converted_courses, 200, {'Content-Type': 'application/json'}
