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
from student import user
from monhoc import monhoc
from giangvien import giangvien
from lopmonhoc import lopmonhoc
from login import login



client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]
PhuHuynh_collection = database["PhuHuynh"]
Diemdanh_colection = database["DiemDanh"]
ThietBi_colleciton = database["ThietBi"]

ds_diem_danh = []
isConfirm = False
times = 0
data = None
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/"
mongo = PyMongo(app)
app.register_blueprint(user)
app.register_blueprint(monhoc)
app.register_blueprint(lopmonhoc)
app.register_blueprint(giangvien)
app.register_blueprint(login)








@app.route('/')
def welcome():
    return "Kinh Khung's database"
@app.route('/phuhuynh/<MaPH>/',methods= ['GET','POST'])
def get_phuhuynh(MaPH):
    all_phuhuynh = PhuHuynh_collection.find({"MaPH": MaPH})
    all_phuhuynhs = PhuHuynh_collection.find({"MaPH": MaPH})
    for ph in all_phuhuynhs:
        all_sinhvien = SinhVien_collection.find({"MaSV":ph["MaSV"]})
    converted_students = json_util.dumps({"Thong tin sinh vien":all_sinhvien,
                                         "Thong tin phu huynh":all_phuhuynh})
    return app.response_class(
        response=converted_students,
        status=200,
        mimetype='application/json'
    )   
# @app.route('/date/<date>',methods= ['GET','POST'])
# def get_date(date):
#     try:
#         today_date = datetime.now().strftime(date)
#         today_courses = []
#         for buoihoc in BuoiHoc_collection.find({"NgayHoc": today_date}):
#             malmh = buoihoc["MaLMH"]

#             for lopmonhoc in LopMonHoc_collection.find({"MaLMH": malmh}):
#                 mavm = lopmonhoc["MaMH"]
#                 tengv = next((gv["TenGV"] for gv in GiangVien_collection.find({"MaGv": lopmonhoc["MaGV"]})), None)
#                 today_courses.append({"MaMH": mavm, "TenMH": lopmonhoc["TenLMH"], "TenGV": tengv})
#         converted_courses = json_util.dumps(today_courses)
#         return app.response_class(
#             response=converted_courses,
#             status=200,
#             mimetype='application/json'
#         )
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500



    # return jsonify({'success': False, 'message': 'Đăng nhập không thành công'})

# @app.route('/diemdanh',methods= ['GET','POST'])    
# def start_to_check_attendance():
#     global mssv
#     global lop
#     data = request.get_json()
#     mssv = data.get('mssv')
#     lop = data.get('class')
#     if mssv and lop :
#         converted = json_util.dumps({"mssv":mssv,
#                                     "lop":lop}) 
#         return app.response_class(
#             response=converted,
#             status=200,
#             mimetype='application/json')
#     return "No ok"

   
@app.route('/confirm',methods= ['GET','POST'])    
def confirm():
    global MaLMH
    global id_device
    # Mathietbi = request.get_json()
    # id_device = Mathietbi.get("id_device")
    id_device = "15"
    sinhvien_all= list(ThietBi_colleciton.find({"MaTB":id_device}))
    for i in sinhvien_all:
        MaLMH = i["MaLMH"]
        print(">>>",MaLMH)
        return "phat" 
@app.route('/confirm1',methods= ['GET','POST'])    
def confirm1():
    if MaLMH:
        converted = json_util.dumps({"MaLMH":MaLMH})
        return converted, 200, {'Content-Type': 'application/json'}
    return "Phat"
@app.route('/confirm3',methods= ['GET','POST'])    
def confirm3():
    if MaLMH:
        converted = json_util.dumps({"MaLMH":MaLMH})
        return converted, 200, {'Content-Type': 'application/json'}
    return "Phat"
@app.route('/diemdanh',methods= ['GET','POST'])    
def get_img_to_check_attendance():
    
    global times
    global data
    global img 
    try:
        url = './api/data_embeddings.npz'
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
        with open('./api/faces_classification.pkl',  'rb') as file:
            model = pickle.load(file)
        # with open('faces_classification.pkl',  'wb') as file:
        #     pickle.dump(model,file)
        print(labels)
        # img = get_firebase(url = f"data/5.jpg")
        img = get_firebase(url = f"data/{MaLMH}_{id_device}.jpg")
        face, box = extract_face("",link = False, img = img)
        if face.shape == (0,0,0):
            converted = json_util.dumps({"attendance":False}) 
            return app.response_class(
                response=converted,
                status=200,
                mimetype='application/json')
        embedding = get_embeddings([face])

        yhat_class = model.predict(embedding)
        yhat_prop = model.predict_proba(embedding)
        class_index = yhat_class[0]
        
        class_probability = yhat_prop[0,class_index] * 100
        predict_name = out_encoder.inverse_transform(yhat_class)
        print("probability: ", class_probability)
        print("name:", predict_name[0])
        if class_probability >= 60:
            for a in list(Diemdanh_colection.find({"MaSV":predict_name[0]})):
                convertedd = json_util.dumps({"attendance":True,
                                            "mssv":predict_name[0]})
                return convertedd, 200, {'Content-Type': 'application/json'}
                    
            sinhvien_all= list(SinhVien_collection.find({"MaSV":predict_name[0]}))
            for i in sinhvien_all:
                TenSV = i["TenSV"]
                print(">>>",TenSV)
            Diemdanh_colection.insert_one({"MaSV":predict_name[0],"TenSV":TenSV})
                
            convertedd = json_util.dumps({"attendance":True,
                                        "mssv":predict_name[0]})
            return convertedd, 200, {'Content-Type': 'application/json'}     
        converted = json_util.dumps({"attendance":False}) 
        return converted, 200, {'Content-Type': 'application/json'} 
        print("fgfdgfdgdfgfd")
    except:
        converted = json_util.dumps({"attendance":False}) 
        return converted, 200, {'Content-Type': 'application/json'} 
if __name__ == "__main__":
    app.run(debug=True, host = "0.0.0.0")
    

