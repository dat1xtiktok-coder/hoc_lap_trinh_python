# Giả sử sếp có một danh sách các hashtag chuẩn bị đem đi spam đăng bài Facebook tự động
cac_hashtag = ["hocpython", "freelance", "kiemtienonline"]

# Ví dụ mẫu: Nối các hashtag lại với nhau bằng dấu cách và thêm dấu thăng
chuoi_hashtag = " #".join(cac_hashtag)
print(f"Chuỗi sau khi nối mẫu: #{chuoi_hashtag}")
# Kết quả ra: #hocpython #freelance #kiemtienonline

print("-" * 40)

# ========================================================
# 🎯 NƠI SẾP TRỔ TÀI NGÀY 35:
# Sau khi cào dữ liệu địa chỉ của khách hàng, sếp thu được một cái mảng tách rời như sau:
dia_chi_tach_roi = ["Số 12 Láng Hạ", "Quận Ba Đình", "Hà Nội"]

# Nhiệm vụ của sếp:
# Hãy dùng lệnh `.join()` để nối các phần tử trong mảng `dia_chi_tach_roi` lại với nhau.
# Nhưng các phần tử phải được ngăn cách nhau bởi một dấu phẩy và một khoảng trắng ", "

dia_chi_ship = ", ".join(dia_chi_tach_roi) # Xóa chữ pass cũ đi và trổ tài đổ keo dính chuỗi vào đây nhé sếp!

print(f"Địa chỉ in trên thẻ ship: {dia_chi_ship}")