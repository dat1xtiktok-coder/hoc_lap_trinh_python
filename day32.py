
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 32:
# Khách hàng gửi cho sếp một danh sách các file ảnh và file excel lẫn lộn:
ten_file_1 = "bao_cao_doanh_thu.xlsx"
ten_file_2 = "anh_chan_dung_sep.jpg"


# Sếp hãy dùng lệnh `.endswith()` để kiểm tra xem `ten_file_1` có phải là file Excel (đuôi ".xlsx") hay không.
# Cú pháp mẫu: bien_ket_qua = ten_file.endswith(".đuôi_cần_check")

la_file_excel = ten_file_1.endswith(".xlsx") # Xóa chữ pass cũ đi và hoàn thiện logic của sếp vào đây

print(f"File số 1 có phải là file Excel không? -> {la_file_excel}")

la_file_anh = ten_file_2.endswith(".jpg")
print(f"file số 2 có phải là file ảnh không  ? -> {la_file_anh}")

# Giả sử đây là tin nhắn log hệ thống cào được từ một con Botday33 gửi về
tin_nhan_he_thong = "THÔNG BÁO: Đơn hàng số ĐH-10293 đã được thanh toán thành công."

# 1. Tuyệt chiêu `in` để kiểm tra nhanh (Trả về True/False)
co_thanh_toan_khong = "thanh toán" in tin_nhan_he_thong
print(f"Có chữ 'thanh toán' trong tin nhắn không? -> {co_thanh_toan_khong}")

# 2. Tuyệt chiêu `.find()` để tìm vị trí chính xác (Trả về số thứ tự ký tự)
vi_tri_ma_don = tin_nhan_he_thong.find("ĐH-10293")
print(f"Mã đơn hàng nằm bắt đầu từ ký tự thứ: {vi_tri_ma_don}")

print("-" * 40)

# ========================================================
#>>vậy thì .endswith là cú pháp để kiểm tra file kèm đuôi file nếu ta đặt điều kiện sai máy tính sẽ trả về kq false
#còn in thì để tìm kiếm 1 mẩu tin find()tìm kiếm vị trí chính xác 
#còn cái câu hoàn thiện logic là gì vậy bài này bạn làm hết rồi 

