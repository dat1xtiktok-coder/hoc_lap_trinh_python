def tinh_tong_hoa_don(*danh_sach_tien): # khai báo hàm và sử dụng agument với cú pháp *
    tong_tien = 0 # khai báo biến chứa tổng tiền

    for dong in danh_sach_tien: #vòng lặp chạy qua từng phần tử trong danh_sach_tien
        tong_tien = tong_tien + dong# lấy từng số liệu ra và tính tổng tiền
        return tong_tien#kết thúc hàm bằng cách trả về dữ liệu từ biến tổng tiền
    
#test hệ thống
bill1 = tinh_tong_hoa_don(50000,20000,30000)
print (f"hóa đơn khách gọi 3 món {bill1} VND")

bill2 = tinh_tong_hoa_don(10000, 5000, 15000, 20000, 50000)
print(f"hóa đơn bill 2 5 món :{bill2}VND")