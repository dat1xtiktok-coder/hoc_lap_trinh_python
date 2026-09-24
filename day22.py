# file: day22.py
import os

print("=== HỆ THỐNG TÌM KIẾM NHÂN VIÊN THÔNG MINH ===")

# 1. Nhập từ khóa tìm kiếm từ bàn phím
tu_khoa = input("Sếp muốn tìm nhân viên nào? Nhập tên hoặc họ: ")

# Chuẩn hóa từ khóa về chữ thường và xóa khoảng trắng thừa
tu_khoa_chuan = tu_khoa.strip().lower()

file_nguon = "tong_hop_doanh_so.csv"

# 2. Kiểm tra file có tồn tại không
if not os.path.exists(file_nguon):
    print(f"❌ Không tìm thấy file {file_nguon}!")
else:
    print(f"\n🔍 Kết quả tìm kiếm cho từ khóa '{tu_khoa}':")
    print("-" * 40)
    
    dem_ket_qua = 0
    
    with open(file_nguon, "r", encoding="utf-8-sig") as f_doc:
        # Bỏ qua dòng tiêu đề đầu tiên
        f_doc.readline()
        
        # Duyệt qua từng dòng dữ liệu
        for dong in f_doc:
            if dong.strip() == "":
                continue
            
            # Cắt chuỗi để lấy Tên và Doanh số (như Ngày 21 sếp đã làm)
            ten, doanh_so_str = dong.strip().split(";")
            
            # CHUẨN HÓA: Biến tên trong file thành chữ thường để tìm kiếm không phân biệt hoa thường
            ten_chu_thuong = ten.lower()
            
            # LOGIC TÌM KIẾM GẦN ĐÚNG: Nếu từ khóa nằm trong tên nhân viên
            if tu_khoa_chuan in ten_chu_thuong:
                print(f"📌 Tìm thấy: {ten} | Doanh số: {doanh_so_str}")
                dem_ket_qua += 1
                
    print("-" * 40)
    print(f"🎉 Đã tìm thấy tổng cộng {dem_ket_qua} nhân sự khớp với yêu cầu.")
    