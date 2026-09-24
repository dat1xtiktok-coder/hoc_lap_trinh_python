# 1. Hàm nhận vào dữ liệu thô, tính toán và TRẢ VỀ một chuỗi sạch sẽ để ghi file
def tinh_va_tao_chuoi(ten, luong_goc, he_so):
    luong_thuc_nhan = int(luong_goc) * float(he_so)
    if ten == ("Nguyễn Văn A"):
        luong_thuc_nhan =int(luong_goc) * float(he_so) + 500000
    # Trả về định dạng chuẩn CSV, cách nhau bằng dấu phẩy để tí mở bằng Excel cho đẹp
    return f"{ten},{luong_thuc_nhan}\n"


# 2. Khối lệnh ĐỌC và GHI SONG HÀNH (Chiến thuật cuốn chiếu)
try:
    # Mở file gốc để ĐỌC ("r") và mở luôn file mới để GHI MỚI ("w")
    with open("luong_tho.csv", "r", encoding="utf-8-sig") as file_doc, \
         open("luong_sach.csv", "w", encoding="utf-8-sig") as file_ghi:
        
        # Viết dòng tiêu đề đầu tiên cho file sạch
        file_ghi.write("Tên Nhân Viên,Lương Thực Nhận\n")
        
        # Quét qua từng dòng trong file thô
        for dong in file_doc:
            # Điều kiện lọc: Chỉ xử lý dòng nào có chứa dấu ";" (dòng dữ liệu chuẩn)
            if ";" in dong:
                cat_du_lieu = dong.split(";") # Cắt chuỗi thành List 3 phần tử
                
                # Bốc dữ liệu ném vào hàm để lấy về chuỗi kết quả
                dong_sach = tinh_va_tao_chuoi(cat_du_lieu[0], cat_du_lieu[1], cat_du_lieu[2])
                
                # GHI THẲNG dòng sạch đó vào file_ghi luôn, không cần kho chứa trung gian!
                file_ghi.write(dong_sach)
                
except PermissionError:
    print("Úi! Sếp ơi tắt file Excel đang mở đi thì code mới chạy được nhé!")
except Exception as e:
    print(f"Có lỗi phát sinh rồi sếp ơi: {e}")
else:
    print("🎉 Quá chuẩn sếp ơi! Đã lọc rác và xuất file 'luong_sach.csv' thành công!")