#hàm 1 in ra dòng chữ khi được gọi
def chao_sep(): #khai báo hàm bằng def dặt tên cho hàm
    print("chào sếp! con bot của sếp đã sẵn sàng tác chiến")# ham chỉ thực hiện một nhiệm vụ duy nhất là in ra dòng này

#hàm 2 tính doanh thu có 2 đơn vị là số lượng và đơn giá  đầu ra là kết quả
def tinh_doanh_thu(so_luong,gia):#khai báo hàm tên là tính doanh thu có 2 biến đầu vào là số lượng và giá
    ket_qua  = so_luong * gia# khai báo và sử dụng biến kết quả để lưu kết quả của hai biến số lượng và đơn giá nhân với nhau 
    return ket_qua #dùng lệnh return để gọi biến kết quả ra ngoài

#gọi hàm 1 để in ra dòng chữ thông báo khởi động
chao_sep()
#gắn giá trị vào hai biến trong hàm để hàm xử lý như ta đã viết ở trên
tien_thu_ve = tinh_doanh_thu(5 , 20000)# kết quả trả ra giá trị và gán vào biến tiền thu về vì các biến trong hàm trước return sẽ chỉ sử dụng mà không lấy đi được còn return chỉ có thể lưu dữ liệu không lưu tên biến

print(f"tiền thu về từ nhà máy là :{tien_thu_ve}    vnd")



