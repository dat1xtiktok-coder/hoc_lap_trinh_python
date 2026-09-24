# Ví dụ mẫu:
gia_chuoi = "150"  # Đây là chuỗi chữ (String), không tính toán được
gia_so = int(gia_chuoi)  # Dùng lệnh int() để ép nó biến hình thành số nguyên 150

print(f"Kiểu dữ liệu sau khi ép: {type(gia_so)}")  # Sẽ in ra <class 'int'>
print(f"Tính toán thử: {gia_so + 50}")  # Ra kết quả 200 mượt mà

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 38:
# Khách hàng nhập vào ô mua hàng số lượng là "5" (nhưng hệ thống nhận về dạng chuỗi chữ)
so_luong_nhap = "5"
gia_san_pham = 120000  # Con số này là số nguyên (int) sẵn rồi

# Nhiệm vụ của sếp:
# 1. Ép kiểu biến `so_luong_nhap` từ chuỗi chữ thành số nguyên và gán vào biến `so_luong_so`.
# 2. Tính tổng tiền bằng cách lấy `so_luong_so` nhân với `gia_san_pham` và gán vào biến `tong_tien`.
# 3. In kết quả `tong_tien` ra màn hình Terminal bằng lệnh print().

# --- SẾP TRỔ TÀI GÕ CODE CỦA SẾP Ở DƯỚI NÀY NHE ---s
so_luong_so = int(so_luong_nhap)
tong_tien = gia_san_pham* so_luong_so
print(f"tổng tiền tính được sau khi ép kiểu là: { tong_tien}")