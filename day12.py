#tạo file dữ liệu giả lập (3 cột:Tên , lương cơ bản , hệ số)
with open ("luong_tho.csv", "w", encoding ="utf-8_sig") as file: #tạo 1 file .csv(exel)ở chế độ đọc 
    file.write("Nguyễn Văn A;10000000;1.2\n")
    file.write("Trần Thị B;15000000;1.5\n")
    file.write("Lê Hoàng C;8000000;1.0\n")#ghi cả 3 dữ liệu vào file


with open ("luong_tho.csv","r", encoding = "utf-8_sig") as file_doc: #mở lại file ở chế độ đọc để xử lý dữ liệu ở đây
    for dong in file_doc:#lấy dữ liệu từ từng trong file để xử lý
        cat_du_lieu=dong.split(";")#lúc này các cột sẽ chia theo biến và kí hiệu số thứ tự từ 0
        luong_co_ban=int(cat_du_lieu[1])
        he_so=float(cat_du_lieu[2])
        luong_thuc_nhan=luong_co_ban*he_so
        print(cat_du_lieu[0], "ban nhan so luong la:", luong_thuc_nhan)