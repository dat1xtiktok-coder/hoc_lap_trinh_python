gia_phong = 750000 

if gia_phong < 500000 :
    print("phòng bình dân")
elif  500000 <= gia_phong <=  1500000: 
    print("Phòng tiêu chuẩn")
else:
    print("phòng cao cấp")

diem_so = 85

if diem_so >= 90:
    print("xuất sắc")
elif 70 <= diem_so <= 90:
    print("khá")
elif 50 <= diem_so <= 70:
    print("trung bình")
else:
    print("yếu")