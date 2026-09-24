mat_khau_dung = "1234"
nguoi_dung_nhap = "123"
if nguoi_dung_nhap == mat_khau_dung :
    print("Chào Sếp")
else:
    print("Sai mật khâu, Hệ thống đang báo động")























so_luong = 10
don_gia = 2000000
tong = so_luong * don_gia
# nếu là khách hàng mục tiêu gửi tin nhắn ( tổng tiền lớn hơn hoặc bằng 1000000)
if tong >= 1000000:
    print("Bạn là khách VIP - Giảm 50k")
    tong = tong - 50000
# nếu là bạn bè chỉ thẻ tim ( tổng tiền lớn hơn hoặc bằng 500000)
elif tong >= 500000:
    print("Bạn là khách hàng thân thiết - giảm 20k")
    tong = tong - 20000
#nếu là khách mới không giảm giá 
else:
    print("bạn là khách mới - không giảm giá")
#in ra tổng tiền cuói cùng 
print("Tổng tiền cuối cùng:", tong)