def tien_thuc_nhan (luong_goc):
    if luong_goc > 15000000:
        print("bạn phải nộp thuế là")
        thue = luong_goc *0.1
    else:
        print("chúc mừng bạn nhận trọn vẹn 100% thu nhập")
        thue = 0
    thuc_nhan = luong_goc - thue
    return ( thuc_nhan , thue )
# --- CÁCH CHẠY CHUẨN NGÀY 6 ---

# Người thứ nhất: Nhập từ bàn phím
luong_nhan_vien = int(input("Mời bạn nhập lương gốc của nhân viên (VND): "))

# Dùng 2 biến ngăn cách bằng dấu phẩy để HỨNG 2 kết quả từ hàm ném ra
tien_nhan_1, thue_nop_1 = tien_thuc_nhan(luong_nhan_vien)

print("Số tiền thực chuyển cho nhân viên là:", tien_nhan_1, "VND")
print("Số tiền thuế nhân viên này đã nộp là:", thue_nop_1, "VND\n")


# Người thứ hai: Lương cố định 20 triệu
# Tiếp tục dùng 2 biến mới để hứng kết quả của người thứ 2
tien_nhan_2, thue_nop_2 = tien_thuc_nhan(20000000) # <--- Gọi đúng tên hàm nha sếp

print("Lương VIP sau thuế là:", tien_nhan_2, "VND")
print("Tiền thuế của VIP là:", thue_nop_2, "VND")