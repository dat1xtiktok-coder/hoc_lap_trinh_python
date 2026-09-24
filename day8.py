danh_sach_kho = ["Ti vi", "Tủ lạnh", "Hàng lỗi", "Máy giặt", "Hàng lỗi", "Điều hòa"]

# 1. Tạo một danh sách mới để chứa hàng ngon
danh_sach_sach = []

# 2. Chạy qua danh sách cũ để nhặt hàng ngon
for hang in danh_sach_kho:
    if hang.lower() != "Hàng lỗi":  # Dấu != nghĩa là "Khác" hoặc "Không phải"
        danh_sach_sach.append(hang) # Nhét hàng ngon vào danh sách mới

# 3. In kết quả cuối cùng ra xem
print("Số lượng hàng còn lại là:", len(danh_sach_sach))
print("Danh sách hàng sạch để xuất kho:", danh_sach_sach)