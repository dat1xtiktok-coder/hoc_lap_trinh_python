#1. Hàm tính toán tổng tiền và trả về cả số tiền lẫn chuỗi dữ liệu sạch
def xu_ly_don_hang(ten, so_luong, don_gia):#tạo hàm xử lý tính toán các biến trùng với dlieu khách cho
    tong_tien = int(so_luong) * int(don_gia)
    chuoi_sach = f"{ten}.{tong_tien}\n"#????
    return tong_tien, chuoi_sach

#khối 1 lệnh đọc flie - ghi 2 file song hành 
try: #bọc giáp nếu file k chạy thì thực hiện ctrinh bình thường
    with open("don_hang_tho.csv","r", encoding = "utf - 8 - sig") as file_doc,\
         open("khach_vip.csv", "w", encoding = "utf -8 - sig")as file_vip,\
         open("khach_normal.csv","w", encoding = "utf -8 -sig") as file_normal:
        #dùng ',\' để thao tác với nhiều file

        #ghi dòng tiêu đề cho cả 2 file mới 
        file_vip.write("Tên khách VIP, Tông chi tiêu\n")
        file_normal.write("Tên khách thường,tổng chi tiêu\n")

    # Quét qua từng dòng trong file đơn hàng thô
        for dong in file_doc:
            # 1. Lọc rác và dòng tiêu đề NGAY TỪ ĐẦU
            if "Tên" in dong or dong.strip() == "":
                continue  # Gặp dòng tiêu đề hoặc dòng trống thì bỏ qua luôn
                
            # 2. Cắt dữ liệu (nhớ chọn đúng dấu khớp với file của sếp nhé)
            cat_du_lieu = dong.split(",") 
            
            # 3. Gọi hàm xử lý khi dữ liệu đã sạch sẽ
            tien, dong_ghi_file = xu_ly_don_hang(cat_du_lieu[0], cat_du_lieu[1], cat_du_lieu[2])

                # phân nhánh 
            if tien >=1000000:
                    file_vip.write(dong_ghi_file)
            else:
                    file_normal.write(dong_ghi_file)

except PermissionError:
    print("Sếp ơi, tắt các file Excel đang mở đi nhé!")
except Exception as e:
    print(f"Có lỗi rồi sếp ơi: {e}")
else:
    print("🎉 Xuất sắc sếp ơi! Đã phân loại xong khách hàng VIP và NORMAL!")