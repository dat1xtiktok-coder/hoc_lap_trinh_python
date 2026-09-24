# Ví dụ mẫu: Hệ thống kiểm tra xem ví tiền có đủ mua hàng không
gia_shopee = 150000
vi_tien = 200000

# Sử dụng toán tử so sánh ">" (Lớn hơn)
du_tien = vi_tien > gia_shopee
print(f"Kết quả kiểm tra ví: {du_tien}")  # Kết quả sẽ in ra: True

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 40:
# Hệ thống kiểm tra xem tài khoản khách hàng có đủ điểm để lên VIP hay không.

so_diem_tich_luy = 850

# Nhiệm vụ của sếp:
# 1. Khai báo một biến tên là: `la_khach_vip`
# 2. Gán cho nó một phép so sánh: Kiểm tra xem `so_diem_tich_luy` có LỚN HƠN HOẶC BẰNG (>=) con số 1000 hay không.
# 3. In kết quả của biến `la_khach_vip` ra màn hình Terminal bằng lệnh print().

# --- SẾP TRỔ TÀI GÕ CODE CỦA SẾP Ở DƯỚI NÀY NHE ---
khach_vip = 1000
so_sanh_thu = so_diem_tich_luy > khach_vip
print(f"kết quả kiểm tra : {so_sanh_thu}")