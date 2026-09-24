def tinh_hieu_suat(ten, doanh_so, ty_le):  # tạo 1 hàm tính hiệu suất
    diem_so = float(doanh_so.strip()) * float(ty_le.strip())  # công thức tính hiệu suất
    # Sếp lưu ý: File thô dùng dấu ";" thì file ghi ra mình cũng dùng dấu ";" cho đồng bộ nhé sếp
    chuoi_sach = f"{ten.strip()};{diem_so}\n"
    return diem_so, chuoi_sach


# Khối lệnh đọc file - ghi file
try:  # bọc giáp
    # mở song song 4 file
    with open("doanh_so_tho.csv", "r", encoding="utf-8-sig") as file_doc, \
            open("sale_xuat_sac.csv", "w", encoding="utf-8-sig") as file_ghi, \
            open("sale_kazen.csv", "w", encoding="utf-8-sig") as file_kz, \
            open("sale_co_gang.csv", "w", encoding="utf-8-sig") as file_cg:

        # ghi tiêu đề cho 3 file (Thụt vào 1 Tab so với with)
        file_ghi.write("tên nhân viên;điểm hiệu suất\n")
        file_kz.write("tên nhân viên;điểm hiệu suất\n")
        file_cg.write("tên nhân viên;điểm hiệu suất\n")

        # Vòng lặp phải nằm TRONG khối with (Thụt vào 1 Tab so với with)
        for dong in file_doc:
            # Lọc bỏ tiêu đề gốc và dòng trống (Thụt vào 1 Tab so với for)
            if "Tên" in dong or dong.strip() == "":
                continue

            # Cắt dữ liệu bằng dấu chấm phẩy (Phải thẳng hàng với if "Tên")
            cat_du_lieu = dong.split(";")

            # Tính toán số liệu bằng cách gọi hàm (Phải thẳng hàng với if "Tên")
            diem, dong_ghi_file = tinh_hieu_suat(cat_du_lieu[0], cat_du_lieu[1], cat_du_lieu[2])

            # Khối phân nhánh ghi file (Phải thẳng hàng với if "Tên")
            if diem >= 100.0:
                file_ghi.write(dong_ghi_file)
            elif diem >= 50.0:
                file_kz.write(dong_ghi_file)
            else:
                file_cg.write(dong_ghi_file)

except PermissionError:
    print("Sếp ơi, tắt file Excel đang mở giải quyết lỗi bản quyền đi nhé!")
except Exception as e:
    print(f"Có lỗi phát sinh rồi sếp: {e}")

# Lệnh in cuối cùng nằm sát lề trái ngoài cùng
print("🎉 Quá đẳng cấp sếp ơi! Đã phân chia nhân sự vào 3 nhóm thành công!")