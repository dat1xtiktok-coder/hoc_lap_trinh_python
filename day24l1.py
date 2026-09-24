try:#bọc lỗi nếu đúng thì thực hiện logic
    #1. nhận dữ liẹu vào từ bàn phím
    so_bi_chia = int(input("nhập số bị chia từ bàn phím(TỬ SỐ):"))#khai báo biến và định nghĩa cho biến là số nguyên và dùng cú pháp input()để nhập số đó từ bàn phím
    so_chia = int(input("nhập số chia(MẪU SỐ):"))#KHAI BÁO biến và định nghĩa như dòng 3 
    #=>lúc này ta chưa có phép chia chính xác nhưng đã có phần tử để định hình phép chia

    #2.thực hiện phép chia
    ket_qua = so_bi_chia / so_chia#viết ra công thức để máy tính thực hiện
    print(f"-> kết quả phép chia là :{ket_qua}")#in ra thông báo  và kết quả nếu thực hiện xong

except ZeroDivisionError :
        print("tôi không thể thực hiện phép chia vì phép chia không hợp lệ" )
