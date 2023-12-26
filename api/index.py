from flask import Flask, render_template, jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient
from bson import json_util
from flask_cors import CORS
from datetime import datetime,timedelta
import json
# Kết nối đến MongoDB (mặc định là localhost, port 27017)
client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')

# Tên cơ sở dữ liệu và collection
database = client['QLSV']
SinhVien_collection = database["SinhVien"]
MonHoc_collection = database["MonHoc"]
BuoiHoc_collection = database["BuoiHoc"]
LopMonHoc_collection = database["LopMonHoc"]
GiangVien_collection = database["GiangVien"]



app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/"
mongo = PyMongo(app)

@app.route('/')
def home():
    return "Kinh Khung's database"
@app.route('/students/<MaSV>',methods= ['GET','POST'])
def get_student(MaSV):
    all_students = list(SinhVien_collection.find({"MaSV":MaSV}))
    converted_students = json_util.dumps(all_students)
    return app.response_class(
        response=converted_students,
        status=200,
        mimetype='application/json'
    )
    
@app.route('/monhoc',methods= ['GET','POST'])
def get_monhoc():
    all_monhoc = list(MonHoc_collection.find())
    converted_students = json_util.dumps(all_monhoc)
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
if __name__ == "__main__":
    app.run(debug= True)
    