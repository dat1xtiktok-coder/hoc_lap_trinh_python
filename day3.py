# Tạo một danh sách tên khách hàng
danh_sach_khach = ["Anh Tuấn","Chị Lan", "Chú Ba","Cô Năm"]
# In ra thử xem có gì 
print("Danh sách hôm nay:", danh_sach_khach)
# Lệnh for: Với mỗi 'nguoi' nằm trong 'danh_sach_khach'
for nguoi in danh_sach_khach:
    print("Chào khách hàng:", nguoi)
    print("Chúc bạn một ngày tốt lành!")
    print("---")







































#số lượng mua 
danh_sach_mua = [2 , 5 , 8 , 1, 10]
#đơn giá
don_gia = 100000
#tính tiền từng con số trong sanh sách
for sl in danh_sach_mua:
    tong = sl * don_gia
    print("số lượng mua:", sl , "-Thành tiền:", tong)
# Nếu số lượng trên 5 món, hãy in thêm dòng:"Đơn hàng này được tặng quà"
    if  sl >= 5 :
        print("<<<Đơn hàng này được tặng quà:>>>", tong)
