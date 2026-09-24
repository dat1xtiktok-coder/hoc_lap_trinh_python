def tinh_luong_clc(ten, luong_goc, he_so ):#khai báo hàm tính toán và in ra kết quả
    luong_thuc_nhan = int(luong_goc) * float(he_so)
    print(ten, "có lương thực nhận là:", luong_thuc_nhan, "vnd")
try:#bọc try chống sập khi code chạy
    with open ("luong_tho.csv", "r", encoding = "utf-8-sig") as file_doc:#vào file để lấy dữ liệu
         for dong in file_doc:# lấy từng dòng trong file
             cat_du_lieu = dong.split(";") #cắt từng dòng trong file
             tinh_luong_clc ( cat_du_lieu[0] ,cat_du_lieu [1], cat_du_lieu[2])#đưa dữ liệu đã cắt quay lại hàm
except PermissionError:# nếu đang bật file thì thông báo tắt file
    print("Tắt file đi nhé!") 
else:#nếu đã ghi xong thì thông báo ghi thành công
    print("Ghi file thành công")
with open ("luong_tho.csv", "w", encoding = "utf-8-sig") as file_doc:
    file_doc.write(tinh_luong_clc)
