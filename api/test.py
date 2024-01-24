from pymongo import MongoClient
from datetime import datetime,timedelta

# Kết nối đến MongoDB (mặc định là localhost, port 27017)
client = MongoClient('mongodb+srv://20520646:20520646@cluster0.ukwx1ww.mongodb.net/')

# Tên cơ sở dữ liệu và collection
database = client['QLSV']
PhuHuynh_collection = database["PhuHuynh"]
SinhVien_collection = database["SinhVien"]
LopMonHoc_collection = database["LopMonHoc"]
DiemSo_collection = database["DiemSo"]
MonHoc_collection = database["MonHoc"]
GiangVien_collection = database["GiangVien"]
BuoiHoc_collection = database["BuoiHoc"]
DiemDanh_collection = database["DiemDanh"]
ThietBi_colleciton = database["ThietBi"]
ThietBi_data = [{"MaTB":1, "MaLMH":"CE410.O11"},
                {"MaTB":2, "MaLMH":"CE410.O11"},
                {"MaTB":3, "MaLMH":"CE410.O11"},
                {"MaTB":4, "MaLMH":"CE410.O11"},
                {"MaTB":5, "MaLMH":"CE410.O11"},
                {"MaTB":6, "MaLMH":"CE410.O11"},
                {"MaTB":7, "MaLMH":"CE410.O11"},
                {"MaTB":8, "MaLMH":"CE410.O11"},
                {"MaTB":9, "MaLMH":"CE410.O11"},
                {"MaTB":10, "MaLMH":"CE410.O11"},
                {"MaTB":11, "MaLMH":"CE410.O11"},
                {"MaTB":12, "MaLMH":"CE410.O11"},
                {"MaTB":13, "MaLMH":"CE410.O11"},
                {"MaTB":14, "MaLMH":"CE410.O11"},
                {"MaTB":15, "MaLMH":"CE410.O11"},
                {"MaTB":16, "MaLMH":"CE410.O11"},
                {"MaTB":17, "MaLMH":"CE410.O11"},
                {"MaTB":18, "MaLMH":"CE410.O11"},
                {"MaTB":19, "MaLMH":"CE410.O11"},
                {"MaTB":20, "MaLMH":"CE410.O11"},
                {"MaTB":21, "MaLMH":"CE410.O11"},
                {"MaTB":22, "MaLMH":"CE410.O11"},
                {"MaTB":23, "MaLMH":"CE410.O11"},
                {"MaTB":24, "MaLMH":"CE410.O11"},
                {"MaTB":25, "MaLMH":"CE410.O11"},
                {"MaTB":26, "MaLMH":"CE410.O11"},
                {"MaTB":27, "MaLMH":"CE410.O11"},
                {"MaTB":28, "MaLMH":"CE410.O11"},
                {"MaTB":29, "MaLMH":"CE410.O11"},
                {"MaTB":30, "MaLMH":"CE410.O11"},
                {"MaTB":31, "MaLMH":"CE410.O11"},
                {"MaTB":32, "MaLMH":"CE410.O11"},
                {"MaTB":33, "MaLMH":"CE410.O11"},
                {"MaTB":34, "MaLMH":"CE410.O11"},
                {"MaTB":"35", "MaLMH":"CE410.O11"},
                {"MaTB":"36", "MaLMH":"CE410.O11"},
                {"MaTB":"37", "MaLMH":"CE410.O11"},
                {"MaTB":"38", "MaLMH":"CE410.O11"},
                {"MaTB":"39", "MaLMH":"CE410.O11"},
                {"MaTB":"40", "MaLMH":"CE410.O11"},
                {"MaTB":"41", "MaLMH":"CE435.O11"},
                {"MaTB":"42", "MaLMH":"CE435.O11"},
                {"MaTB":"43", "MaLMH":"CE435.O11"},
                {"MaTB":"44", "MaLMH":"CE435.O11"},
                {"MaTB":"45", "MaLMH":"CE435.O11"},
                {"MaTB":"46", "MaLMH":"CE435.O11"},
                {"MaTB":"47", "MaLMH":"CE435.O11"},
                {"MaTB":"48", "MaLMH":"CE435.O11"},
                {"MaTB":"49", "MaLMH":"CE435.O11"},
                {"MaTB":"50", "MaLMH":"CE435.O11"},
                {"MaTB":"51", "MaLMH":"CE435.O11"},
                {"MaTB":"52", "MaLMH":"CE435.O11"},
                {"MaTB":"53", "MaLMH":"CE435.O11"},
                {"MaTB":"54", "MaLMH":"CE435.O11"},
                {"MaTB":"55", "MaLMH":"CE435.O11"},
                {"MaTB":"56", "MaLMH":"CE435.O11"},
                {"MaTB":"57", "MaLMH":"CE435.O11"},
                {"MaTB":"58", "MaLMH":"CE435.O11"},
                {"MaTB":"59", "MaLMH":"CE435.O11"},
                {"MaTB":"60", "MaLMH":"CE435.O11"},
                {"MaTB":"61", "MaLMH":"CE435.O11"},
                {"MaTB":"62", "MaLMH":"CE435.O11"},
                {"MaTB":"63", "MaLMH":"CE435.O11"},
                {"MaTB":"64", "MaLMH":"CE435.O11"},
                {"MaTB":"65", "MaLMH":"CE435.O11"},
                {"MaTB":"66", "MaLMH":"CE435.O11"},
                {"MaTB":"67", "MaLMH":"CE435.O11"},
                {"MaTB":"68", "MaLMH":"CE435.O11"},
                {"MaTB":"69", "MaLMH":"CE435.O11"},
                {"MaTB":"70", "MaLMH":"CE435.O11"},
                {"MaTB":"71", "MaLMH":"CE435.O11"},
                {"MaTB":72, "MaLMH":"CE435.O11"},
                {"MaTB":73, "MaLMH":"CE435.O11"},
                {"MaTB":74, "MaLMH":"CE435.O11"},
                {"MaTB":75, "MaLMH":"CE435.O11"},
                {"MaTB":76, "MaLMH":"CE435.O11"},
                {"MaTB":77, "MaLMH":"CE435.O11"},
                {"MaTB":78, "MaLMH":"CE435.O11"},
                {"MaTB":79, "MaLMH":"CE435.O11"},
                {"MaTB":80, "MaLMH":"CE435.O11"},
                ]
BuoiHoc_data = [{"MaBH":"111","MaLMH": "CE410.O11","LoaiBH":"TH","NgayHoc":"23_12_2023","TGBD":"7:30:00","TGKT":"11:30:00"},
                {"MaBH":"112","MaLMH": "CE410.O11","LoaiBH":"LT","NgayHoc":"24_12_2023","TGBD":"8:30:00","TGKT":"11:30:00"},
                {"MaBH":"113","MaLMH": "CE410.O11","LoaiBH":"TH","NgayHoc":"23_1_2024","TGBD":"13:30:00","TGKT":"16:30:00"},
                {"MaBH":"114","MaLMH": "CE435.O11","LoaiBH":"LT","NgayHoc":"25_12_2023","TGBD":"7:30:00","TGKT":"11:30:00"},
                {"MaBH":"115","MaLMH": "CE435.O11","LoaiBH":"LT","NgayHoc":"26_12_2023","TGBD":"13:30:00","TGKT":"16:30:00"},
                {"MaBH":"116","MaLMH": "CE435.O11","LoaiBH":"LT","NgayHoc":"25_1_2024","TGBD":"7:30:00","TGKT":"11:30:00"},
                {"MaBH":"117","MaLMH": "CE124.O11","LoaiBH":"LT","NgayHoc":"23_1_2024","TGBD":"7:30:00","TGKT":"11:30:00"},
                {"MaBH":"118","MaLMH": "CE124.O11","LoaiBH":"LT","NgayHoc":"26_12_2023","TGBD":"7:30:00","TGKT":"11:30:00"},
                {"MaBH":"119","MaLMH": "CE124.O11","LoaiBH":"LT","NgayHoc":"24_1_2024","TGBD":"7:30:00","TGKT":"11:30:00"},
                
                ]
GiangVien_data = [{"MaGv":"111111","TenGV":"Phạm Thanh Hùng","Dia Chi":"HCM","TenDN":"111111","MK":"123456"},
                  {"MaGv":"111112","TenGV":"Hồ Ngọc Diễm","Dia Chi":"HCM","TenDN":"111112","MK":"123457"},
                  {"MaGv":"111113","TenGV":"Trịnh Lê Huy","Dia Chi":"HCM","TenDN":"111113","MK":"123458"},
                  {"MaGv":"111114","TenGV":"Trần Quang Nguyên","Dia Chi":"HCM","TenDN":"111114","MK":"123458"},
                  {"MaGv":"111115","TenGV":"Tạ Trí Đức","Dia Chi":"HCM","TenDN":"111115","MK":"123458"},
                  {"MaGv":"111116","TenGV":"Chung Quang Khánh","Dia Chi":"HCM","TenDN":"111116","MK":"123458"},
                  {"MaGv":"111117","TenGV":"Đoàn Duy","Dia Chi":"HCM","TenDN":"111117","MK":"123458"},
                  {"MaGv":"111118","TenGV":"Nguyễn Minh Sơn","Dia Chi":"HCM","TenDN":"111118","MK":"123458"},
                  {"MaGv":"111119","TenGV":"Ngô Hiếu Trường","Dia Chi":"HCM","TenDN":"111119","MK":"123458"},
                  ]
MonHoc_data = [{"MaMH": "CE410", "TenMH": "Kỹ thuật hệ thống máy tính", "STC": "4", "STCLT": "3", "STCTH": "1"},
               {"MaMH": "CE435", "TenMH": "Chuyên đề thiết kế hệ vi mạch 2", "STC": "4", "STCLT": "3", "STCTH": "1"},
               {"MaMH": "CE232", "TenMH": "Thiết kế hệ thống nhúng không dây", "STC": "4", "STCLT": "3", "STCTH": "1"},
               {"MaMH": "CE224", "TenMH": "Thiết kế hệ thống nhúng", "STC": "4", "STCLT": "3", "STCTH": "1"},
               {"MaMH": "CE213", "TenMH": "Thiết kế hệ thống số với HDL", "STC": "4", "STCLT": "3", "STCTH": "1"},
               {"MaMH": "CE124", "TenMH": "Các thiết bị và mạch điện tử", "STC": "4", "STCLT": "3", "STCTH": "1"},
               {"MaMH": "CE121", "TenMH": "Lý thuyết mạch điện", "STC": "2", "STCLT": "2", "STCTH": "0"},
               {"MaMH": "CE118", "TenMH": "Thiết kế luận lý số", "STC": "2", "STCLT": "2", "STCTH": "0"},
               {"MaMH": "CE408", "TenMH": "Đồ án chuyên ngành Thiết kế vi mạch và phần cứng", "STC": "2", "STCLT": "2", "STCTH": "0"},
               ]
LopMonHoc_data = [{"MaLMH": "CE410.O11", "MaMH": "CE410","MaGV":"111118", "TenLMH": "Kỹ thuật hệ thống máy tính - CE410.O11","SoSV": "40"},
                  {"MaLMH": "CE435.O11", "MaMH": "CE435","MaGV":"111119", "TenLMH": "Chuyên đề thiết kế hệ vi mạch 2 - CE435.O11", "SoSV": "50"},
                  {"MaLMH": "CE232.O11", "MaMH": "CE232","MaGV":"111117", "TenLMH": "Thiết kế hệ thống nhúng không dây - CE232.O11", "SoSV": "50"},
                  {"MaLMH": "CE224.O12", "MaMH": "CE224","MaGV":"111116", "TenLMH": "Thiết kế hệ thống nhúng - CE224.O12", "SoSV": "50"},
                  {"MaLMH": "CE213.O12", "MaMH": "CE213","MaGV":"111115", "TenLMH": "Thiết kế hệ thống số với HDL - CE213.O12", "SoSV": "50"},
                  {"MaLMH": "CE124.O11", "MaMH": "CE124","MaGV":"111114", "TenLMH": "Các thiết bị và mạch điện tử - CE124.O11", "SoSV": "40"},
                  {"MaLMH": "CE121.O11", "MaMH": "CE121","MaGV":"111113", "TenLMH": "Lý thuyết mạch điện - CE121.O11", "SoSV": "60"},
                  {"MaLMH": "CE118.O11", "MaMH": "CE118","MaGV":"111112", "TenLMH": "Thiết kế luận lý số - CE118.O11", "SoSV": "50"},
                  {"MaLMH": "CE408.O11", "MaMH": "CE408","MaGV":"111111", "TenLMH": "Đồ án chuyên ngành Thiết kế vi mạch và phần cứng - CE408.O11", "SoSV": "100"},
                  ]
DiemSo_data = [
    {"MaSV": "20520646", "MaLMH": "CE410.O11", "HocKy": "HK1", "NamHoc": "2022-2023", "Diem": 8.5},
    {"MaSV": "20521737", "MaLMH": "CE410.O11", "HocKy": "HK1", "NamHoc": "2022-2023", "Diem": 8.5},
    {"MaSV": "20521727", "MaLMH": "CE410.O11", "HocKy": "HK1", "NamHoc": "2022-2023", "Diem": 8.5},
    {"MaSV": "20520467", "MaLMH": "CE410.O11", "HocKy": "HK1", "NamHoc": "2022-2023", "Diem": 8.5},
    {"MaSV": "20520438", "MaLMH": "CE410.O11", "HocKy": "HK2", "NamHoc": "2022-2023", "Diem": 7.8},
    {"MaSV": "19520965", "MaLMH": "CE206.O11", "HocKy": "HK1", "NamHoc": "2022-2023", "Diem": 9.2},
]
SinhVien_data = [
    {"MaSV": "20520646", "TenSV": "Vo Nhat Nam",
     "GioiTinh": "Nam", "NoiSinh": "TienGiang", "Dia Chi": "HCM", "TenDN": "20520646", "MK": "123456"},
    {"MaSV": "20521737", "TenSV": "Nguyen Thanh Phat",
     "GioiTinh": "Nam", "NoiSinh": "TienGiang", "DiaChi": "HCM", "TenDN": "20521737", "MK": "123456"},
    {"MaSV": "20521727", "TenSV": "Tran Bao Nhung",
     "GioiTinh": "Nu", "NoiSinh": "TienGiang", "DiaChi": "HCM", "TenDN": "20521727", "MK": "123456"},
    {"MaSV": "20520467", "TenSV": "Le Nguyen Quang Duy",
     "GioiTinh": "Nam", "NoiSinh": "TienGiang", "DiaChi": "HCM", "TenDN": "20520647", "MK": "123456"},
    {"MaSV": "19520965", "TenSV": "Pham Ngoc Thanh Thao",
     "GioiTinh": "Nu", "NoiSinh": "TienGiang", "DiaChi": "HCM", "TenDN": "20520646", "MK": "123456"},
    {"MaSV": "20520438", "TenSV": "Tran Tuan Dat",
     "GioiTinh": "Nam", "NoiSinh": "TienGiang", "DiaChi": "HCM", "TenDN": "20520438", "MK": "123456"},
]

PhuHuynh_data = [
    {"MaPH": "123456", "MaSV": "20520646", "TenPH": "Vo Van A", "SDT": "098765432", "DiaChi": "TienGiang",
     "TenDN": "123456", "MK": "123456", "QuanHe": "Cha"},
    {"MaPH": "123457", "MaSV": "20521737", "TenPH": "Nguyen Van B", "SDT": "098737526", "DiaChi": "TienGiang",
     "TenDN": "123457", "MK": "123456", "QuanHe": "Cha"},
    {"MaPH": "123458", "MaSV": "20521727", "TenPH": "Tran Van C", "SDT": "098797215", "DiaChi": "TienGiang",
     "TenDN": "123458", "MK": "123456", "QuanHe": "Cha"},
    {"MaPH": "123459", "MaSV": "20520467", "TenPH": "Nguyen Thi Ngoc D", "SDT": "098774246", "DiaChi": "TienGiang",
     "TenDN": "123459", "MK": "123456", "QuanHe": "Me"},
    {"MaPH": "123455", "MaSV": "19520965", "TenPH": "Ly Thi E", "SDT": "098777777", "DiaChi": "TienGiang",
     "TenDN": "123455", "MK": "123456", "QuanHe": "Me"},
    {"MaPH": "123454", "MaSV": "20520438", "TenPH": "Tran Van F", "SDT": "098785643", "DiaChi": "TienGiang",
     "TenDN": "123454", "MK": "123456", "QuanHe": "Cha"}
]
SinhVien_collection.insert_many(SinhVien_data)
PhuHuynh_collection.insert_many(PhuHuynh_data)
LopMonHoc_collection.insert_many(LopMonHoc_data)
DiemSo_collection.insert_many(DiemSo_data)
MonHoc_collection.insert_many(MonHoc_data)
GiangVien_collection.insert_many(GiangVien_data)
BuoiHoc_collection.insert_many(BuoiHoc_data)
ThietBi_colleciton.insert_many(ThietBi_data)
