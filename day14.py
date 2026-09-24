#cách tự chế hàm bằng lệnh def
def tinh_luong_clc(ten, luong_goc, he_so):
    #tất cả code bên trong hàm phải thụt lề vào
    luong_thuc_nhan = int(luong_goc) * float(he_so)
    print (ten,"có lương thực nhận là" , luong_thuc_nhan)

# thử gọi hàm mà không cần phép tính
tinh_luong_clc("nguyễn văn a", 10000000, 1.2)
tinh_luong_clc("Trần thị b", 15000000, 1.5)
tinh_luong_clc("Lê Hoàng C",8000000, 0.9)