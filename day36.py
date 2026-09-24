# Một cái form tin nhắn mẫu để gửi tự động cho khách hàng khi họ mua đồ
tin_nhan_mau = "Chào sếp {}, đơn hàng {} của sếp đã được đóng gói thành công!"

# Cách dùng .format(): Bơm biến theo đúng thứ tự từ trái qua phải vào các dấu {}
tin_hoan_chinh = tin_nhan_mau.format("Nguyễn Văn Sếp", "DH-9923")
print(tin_hoan_chinh)

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 36:
# Giả sử sếp viết một con bot tự động gửi tin nhắn báo giá cho khách hàng

form_bao_gia = "Sản phẩm {} hiện đang có giá là {} VNĐ."

# Nhiệm vụ của sếp:
# 1. Khai báo 2 biến: `ten_sp = "Chuột Gaming"` và `gia_sp = 350000`
# 2. Dùng lệnh `.format()` để bơm 2 biến này vào chuỗi `form_bao_gia`, rồi gán kết quả vào biến `ket_qua`
# 3. In biến `ket_qua` ra màn hình Terminal bằng lệnh print()

# --- SẾP GÕ CODE CỦA SẾP Ở DƯỚI NÀY NHE ---
ten_sp = "chuột gaming"
gia_sp = 350000

from_hoan_chinh = form_bao_gia.format(ten_sp, gia_sp)
print(from_hoan_chinh)
print("-"*40)