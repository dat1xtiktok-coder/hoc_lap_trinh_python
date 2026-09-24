# Giả sử khách hàng đăng ký tài khoản bằng Email trên Web của sếp
email_khach = "admin@fpt.edu.vn"

# 1. Thử chặt đôi cái email này ra làm 2 phần bằng ký tự "@"
cac_phandoc = email_khach.split("@")
print(f"Mảng sau khi chặt bằng chữ '@': {cac_phandoc}") 
# Kết quả sẽ ra: ['admin', 'fpt.edu.vn']

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 34:
# Khách hàng gửi cho sếp một chuỗi dữ liệu thô chứa thông tin sản phẩm ngăn cách nhau bằng dấu gạch đứng "|"
du_lieu_tho = "Giày Nike|Size 42|Màu Đen|Giá 1500000"

# Nhiệm vụ của sếp:
# 1. Dùng lệnh .split("|") để chặt cái `du_lieu_tho` này thành một cái mảng (List) tên là `thong_tin_sp`.
# 2. In ra màn hình phần tử đầu tiên của mảng đó (chính là tên sản phẩm "Giày Nike") bằng cú pháp gọi chỉ số index: thong_tin_sp[vị_trí_cần_lấy]

thong_tin_sp = du_lieu_tho.split("|")

print(f"Tên sản phẩm bóc tách tự động là: {thong_tin_sp[0]}")
print(f"Tên sản phẩm bóc tách tự động là: {thong_tin_sp}")