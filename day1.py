ten_san_pham = "Toll quét Data"
so_luong = 6 
don_gia = 200000
 #1.tính tổng tiền gốc 
tong_tien = so_luong * don_gia
print (" Tổng tiền gốc là:", tong_tien)

#2 kiểm tra điều kiện if
#nếu tổng tiền lớn hơn hoặc bằng 1.000.000
if tong_tien >= 1000000:
    print("chúc mừng! bạn mua nhiều nên được giảm 50000 VND")
    tong_tien = tong_tien - 50000
# nếu không 
else:
    print("bạn chưa đủ điều kiện giảm giá(Cần phải mua trêm 1000000)")
 
#3 số tiền phải trả cuối cùng
print("số tiền phải trả cuối cùng:", tong_tien)
