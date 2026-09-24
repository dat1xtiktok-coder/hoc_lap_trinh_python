# Ví dụ mẫu:
chuoi_ti_gia = "25450.75"
so_ti_gia = float(chuoi_ti_gia) # Ép chuỗi thành số thực để tính toán
print(f"Tỉ giá sau khi ép kiểu: {so_ti_gia}")

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 39:
# Con bot của sếp chia phần trăm hoa hồng cho đối tác và ra một con số lẻ loét:
hoa_hong_chua_tron = 1550.6666666666667

# Nhiệm vụ của sếp:
# 1. Dùng hàm `round()` để làm tròn biến `hoa_hong_chua_tron`, chỉ lấy ĐÚNG 2 chữ số sau dấu phẩy thập phân.
# 2. Gán kết quả vào biến `hoa_hong_dep`.
# 3. In biến `hoa_hong_dep` ra màn hình Terminal bằng lệnh print().

# --- SẾP TRỔ TÀI GÕ CODE CỦA SẾP Ở DƯỚI NÀY NHE ---
hoa_hong_dep = round(hoa_hong_chua_tron, 2)
print(f"hoa hồng đẹp nè{hoa_hong_dep}")