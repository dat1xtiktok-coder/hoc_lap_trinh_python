
# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 33:
# Khách hàng yêu cầu sếp viết tool cào mã đơn hàng ẩn trong chuỗi này:
tin_nhan = "Don hang DH-8892 cua ban da duoc gui di."

# Tôi đã dò hộ sếp: Chữ "D" của "DH-8892" nằm ở vị trí số 9. 
# Chữ số "2" cuối cùng của mã nằm ở vị trí số 15.

# Nhiệm vụ của sếp: Hãy dùng cú pháp cắt lát [bắt đầu:kết thúc] 
# để lấy ra đúng chữ "DH-8892" và gán vào biến `ma_don_hang`.
# (Nhớ quy tắc: Vị trí kết thúc phải cộng thêm 1 đơn vị thì mới ôm trọn được số 2 nhé!)

ma_don_hang = tin_nhan[9:16 ]  # Xóa chữ pass này đi và tự tay cắt chuỗi xem nào sếp ơi!

print(f"Mã đơn hàng bóc tách thành công là: {ma_don_hang}")