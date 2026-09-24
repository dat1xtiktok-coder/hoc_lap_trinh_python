# 1. Hàm bây giờ nhiệm vụ là TÍNH VÀ TRẢ VỀ CHUỖI VĂN BẢN (dùng return)
def tinh_luong_clc(ten, luong_goc, he_so):
    luong_thuc_nhan = int(luong_goc) * float(he_so)
    # Trả về một chuỗi văn bản hoàn chỉnh để tí nữa ghi vào file
    return f"\n{ten} co luong thuc nhan la: {luong_thuc_nhan} vnd"

# Tạo một cái kho chứa dữ liệu trước khi ghi
ket_qua_list = []

# 2. Khối ĐỌC FILE để lấy dữ liệu cho vào kho
try:
    with open("luong_tho.csv", "r", encoding="utf-8-sig") as file_doc:
        for dong in file_doc:
            if ";" in dong:
                cat_du_lieu = dong.split(";")
                
                # Chạy hàm để lấy chuỗi kết quả trả về
                dong_ket_qua = tinh_luong_clc(cat_du_lieu[0], cat_du_lieu[1], cat_du_lieu[2])
                
                # Ném chuỗi đó vào kho chứa
                ket_qua_list.append(dong_ket_qua)
                
except PermissionError:
    print("Tắt file đi nhé!")

# 3. Khối GHI TIẾP VÀO FILE (Viết tách biệt hoàn toàn ở dưới theo ý sếp)
# Đổi chế độ sang "a" để ghi tiếp vào cuối file
with open("luong_tho.csv", "a", encoding="utf-8-sig") as file_ghi:
    # Duyệt qua từng dòng kết quả trong kho chứa để ghi vào file
    for dong_ghi in ket_qua_list:
        file_ghi.write(dong_ghi)

print("Ghi file thành công!")