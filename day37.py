# Ví dụ mẫu: Định dạng số tiền lớn
so_tien_goc = 50000000  # 50 triệu

# Dùng mật mã {:,} bên trong chuỗi tin nhắn
chuoi_mau = "Số dư tài khoản của sếp là: {:,} VNĐ"
print(chuoi_mau.format(so_tien_goc))
# Kết quả ra: Số dư tài khoản của sếp là: 50,000,000 VNĐ

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 37:
# Khách hàng yêu cầu sếp viết tool gửi tin nhắn tự động thông báo doanh thu tháng

form_thong_bao = "Doanh thu tháng này đạt {:,} VNĐ, tăng trưởng {}% so với tháng trước."

doanh_thu = 18500000
tang_truong = 15
print(form_thong_bao.format(doanh_thu, tang_truong))