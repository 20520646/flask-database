from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from datetime import datetime,timedelta
import json
from numpy import load
from sklearn.preprocessing import LabelEncoder, Normalizer
import pickle
from make_embeddings import get_embeddings
from extract_faces import extract_face
from firebase1 import get_firebase
# Kết nối đến MongoDB (mặc định là localhost, port 27017)
client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')

# Tên cơ sở dữ liệu và collection
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]


times = 0
data = None
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/"
mongo = PyMongo(app)
CORS(app)
@app.route('/')
def welcome():
    return "Kinh Khung's database"


@app.route('/home/<MaSV>',methods= ['GET','POST'])
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
    return app.response_class(
        response=converted,
        status=200,
        mimetype='application/json'
    )    
@app.route('/students/<MaSV>',methods= ['GET','POST'])
def get_student(MaSV):
    all_students = list(SinhVien_collection.find({"MaSV":MaSV}))
    converted_students = json_util.dumps(all_students)
    return app.response_class(
        response=converted_students,
        status=200,
        mimetype='application/json'
    )
@app.route('/giangvien/<MaGV>',methods= ['GET','POST'])
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
    return app.response_class(
        response=converted_students,
        status=200,
        mimetype='application/json'
    )    
@app.route('/monhoc/<MaSV>',methods= ['GET','POST'])
def get_monhoc(MaSV):
    if SinhVien_collection.find({"MaSV":MaSV}):
        all_monhoc = list(MonHoc_collection.find())
        converted_students = json_util.dumps(all_monhoc)
        return app.response_class(
            response=converted_students,
            status=200,
            mimetype='application/json'
        )

@app.route('/monhoc/<MaSV>/<MaLMH>',methods= ['GET','POST'])
def get_lopmonhoc(MaSV,MaLMH):
    if SinhVien_collection.find({"MaSV":MaSV}):
        if LopMonHoc_collection.find({"MaLMH":MaLMH}):
            all_Lopmonhoc = LopMonHoc_collection.find({"MaLMH":MaLMH})
        converted_students = json_util.dumps(all_Lopmonhoc)
        return app.response_class(
            response=converted_students,
            status=200,
            mimetype='application/json'
        )
@app.route('/phuhuynh/<MaPH>/',methods= ['GET','POST'])
def get_phuhuynh(MaPH):
    if PhuHuynh_collection.find({"MaPH":MaPH}):
        if SinhVien_collection.find({"MaSV":ph["MaSV"] for ph in PhuHuynh_collection.find()}):
            all_Phuhuynh = PhuHuynh_collection.find({"MaPH":MaPH})
            all_Phuhuynhs = PhuHuynh_collection.find({"MaPH":MaPH})
            for ph in all_Phuhuynhs:
                MaSVs = ph["MaSV"]
            all_sinhvien = SinhVien_collection.find({"MaSV":MaSVs})
            for sv in all_sinhvien:
                _id = sv["_id"]
                MaSV = sv["MaSV"]
                TenSV = sv["TenSV"]
                GioiTinh = sv["GioiTinh"]
                NoiSinh = sv["NoiSinh"]
                DiaChi = sv["DiaChi"]
                TenDN = sv["TenDN"]
                mk = sv["MK"]
        converted_students = json_util.dumps({"PhuHuynh":all_Phuhuynh,
                                              "SinhVien":{
                                                 "_id":_id,
                                                 "MaSV":MaSV,
                                                 "TenSV": TenSV,
                                                 "GioiTinh": GioiTinh,
                                                 "NoiSinh": NoiSinh,
                                                 "DiaChi":DiaChi,
                                                 "TenDN":TenDN,
                                                 "MK":mk
                                            }
                                             })
        return app.response_class(
            response=converted_students,
            status=200,
            mimetype='application/json'
        )   
@app.route('/date/<date>',methods= ['GET','POST'])
def get_date(date):
    try:
        today_date = datetime.now().strftime(date)
        today_courses = []
        for buoihoc in BuoiHoc_collection.find({"NgayHoc": today_date}):
            malmh = buoihoc["MaLMH"]

            for lopmonhoc in LopMonHoc_collection.find({"MaLMH": malmh}):
                mavm = lopmonhoc["MaMH"]
                tengv = next((gv["TenGV"] for gv in GiangVien_collection.find({"MaGv": lopmonhoc["MaGV"]})), None)
                today_courses.append({"MaMH": mavm, "TenMH": lopmonhoc["TenLMH"], "TenGV": tengv})
        converted_courses = json_util.dumps(today_courses)
        return app.response_class(
            response=converted_courses,
            status=200,
            mimetype='application/json'
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/lopmonhoc/<MaLMH>',methods= ['GET','POST'])    
def get_lmh(MaLMH):
    if LopMonHoc_collection.find({"MaLMH":MaLMH}):
        Lopmonhoc_all = list(LopMonHoc_collection.find({"MaLMH":MaLMH}))
    if SinhVien_collection.find({"Lop":MaLMH}):
        sinhvien_all= list(SinhVien_collection.find({"Lop":MaLMH}))
        sinhvien1 = []
        print(sinhvien_all)
        for sv in sinhvien_all:
            _id = sv["_id"]
            MaSV = sv["MaSV"]
            TenSV = sv["TenSV"]
            sinhvien1.append({"_id":_id,"MaSV":MaSV,"TenSV": TenSV})
    converted_courses = json_util.dumps({"Thong tin lop hoc":Lopmonhoc_all,
                                         "Thong tin sinh vien":sinhvien1})
    return app.response_class(
        response=converted_courses,
        status=200,
        mimetype='application/json'
    )
@app.route('/login',methods= ['GET','POST'])    
def login_account():
    data = request.get_json()
    username = data.get('id')
    password = data.get('password')
    if username and password :
        for sv in SinhVien_collection.find():
            if sv["TenDN"] == username and sv["MK"] == password:
                converted = json_util.dumps({"isCorrect":True,
                                             "typeAccount":"sv"})
                return app.response_class(
                    response=converted,
                    status=200,
                    mimetype='application/json'
                )
        for gv in GiangVien_collection.find():
            if gv["TenDN"] == username and gv["MK"] == password:
                converted = json_util.dumps({"isCorrect":True,
                                             "typeAccount":"gv"})
                return app.response_class(
                    response=converted,
                    status=200,
                    mimetype='application/json'
                )
        for ph in PhuHuynh_collection.find():
            if ph["TenDN"] == username and ph["MK"] == password:
                converted = json_util.dumps({"isCorrect":True,
                                             "typeAccount":"ph"})
                return app.response_class(
                    response=converted,
                    status=200,
                    mimetype='application/json'
                )
    converted = json_util.dumps({"isCorrect":False}) 
    return app.response_class(
        response=converted,
        status=200,
        mimetype='application/json'
    )
    return jsonify({'success': False, 'message': 'Đăng nhập không thành công'})
@app.route('/<MaLMH>/diemdanh',methods= ['GET','POST'])    
def get_img_to_check_attendance(MaLMH):
    global times
    global data
    global converted
    if times == 0:
        url = 'data_embeddings.npz'
        data = load(url)
        print(">>>",data)
        faces, labels = data['arr_0'], data['arr_1']
        # print(f'>>> Dataset: train={faces.shape[0]}')
        # model, out_encoder = train_model(faces, labels)
        # in_encoder = Normalizer(norm ='l2')
        # faces = in_encoder.transform(faces)
        out_encoder = LabelEncoder()
        out_encoder.fit(labels)

        # print(labels, type(labels))

        labels = out_encoder.transform(labels)
        with open('./faces_classification.pkl',  'rb') as file:
            model = pickle.load(file)
        # with open('faces_classification.pkl',  'wb') as file:
        #     pickle.dump(model,file)
        print(labels)
        img = get_firebase()
        face, box = extract_face("",link = False, img = img)
        embedding = get_embeddings([face])

        yhat_class = model.predict(embedding)
        yhat_prop = model.predict_proba(embedding)
        class_index = yhat_class[0]
        
        class_probability = yhat_prop[0,class_index] * 100
        predict_name = out_encoder.inverse_transform(yhat_class)
        print("probability: ", class_probability)
        print("name:", predict_name[0])
        if class_probability >= 60:
            for sv in SinhVien_collection.find({"Lop":MaLMH}):
                if sv["MaSV"] == predict_name[0].strip():
                    converted = json_util.dumps({"attendance":True})
                    data = converted
                    times += 1 
                    return app.response_class(
                        response=converted,
                        status=200,
                        mimetype='application/json')  
        converted = json_util.dumps({"attendance":False}) 
        data = converted 
        times += 1 
        return app.response_class(
            response=converted,
            status=200,
            mimetype='application/json')
    else:
        return app.response_class(
            response=converted,
            status=200,
            mimetype='application/json')
@app.route('/diemdanh/<MaSV>/<MaLMH>/<day>',methods= ['GET','POST'])    
def start_to_check_attendance(MaSV,MaLMH):
    pass

if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")

