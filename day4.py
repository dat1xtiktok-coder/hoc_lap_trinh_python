


#thời gian chơi là 
thoi_gian = int(input("Bạn muốn chơi bao nhiêu giờ"))
#mỗi giờ chơi = 10000
mot_gio = 10000
#tổng thời gian chơi là:
so_tien = thoi_gian * mot_gio
print("Bạn đã nạp với só giờ chơi",thoi_gian ,"giờ", "và số tiền là", so_tien)
#nếu gio_choi lớn hơn hoặc bằng 5
if thoi_gian >=5:
    print("Bạn được tặng 1 chai sting")
#nếu không thì in chúc bạn chơi game vui vẻ
else:
    print("Chúc bạn chơi game vui vẻ")
