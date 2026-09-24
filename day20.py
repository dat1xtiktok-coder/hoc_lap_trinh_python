#taoj một dictionary rỗng để chưa dữ liệu cộng biến
thong_ke_tong = {}

#danh sách các file cần đọc để gộp
cac_file_thang = ["doanh_so_thang5.csv", "doanh_so_thang6.csv"]

try:
    #vòng lặp quét qua từng file trong danh sách
    for ten_file in cac_file_thang:
        with open(ten_file, "r",encoding= ("utf-8")) as file_doc:
            for dong in file_doc:
                #lọc bỏ dòng tiêu đề và dòng trống
                if "Tên" in dong or dong.strip() =="":
                    continue

                #cắt dữ liệu bằng dấu chấm phẩy
                ten, doanh_so = dong.strip().split(";")
                doanh_so = float(doanh_so)# ép kiểu hay đổi kiểu về float để tính toán 

                # logic cộng dồn doanh số
                if ten in thong_ke_tong:
                    #nếu người đã có trong từ điển rồi cộng thêm tiền tức tên trùng lặp
                    thong_ke_tong[ten] += doanh_so
                else:
                    #nếu người này chưa có tạo mới và gắn múc doanh số đầu tiên
                    thong_ke_tong[ten] = doanh_so

    with open("tong_hop_doanh_so.csv" ,"w",encoding = "utf - 8 -sig") as file_ghi:
        file_ghi.write("Tên nhân viên;Tổng hợp doanh số\n")#tiêu đề file

        #vòng lặp quét qua từng người trong dictionary để ghi vào file 
        for ten, tong_tien in thong_ke_tong.items():
            file_ghi.write(f"{ten};{tong_tien}\n")

except Exception as e:
    print(f"úi có lỗi rồi sếp :{e}")
else:
    print(f"Dữ liệu đã ghi vào thong_ke_tong")