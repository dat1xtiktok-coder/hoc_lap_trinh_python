def So_phut_di_muon(thoi_gian):
    if thoi_gian == 0:
        tien_phat = 0
        print("Bạn đến đúng giờ, xuất sắc!")
    elif thoi_gian <= 15:
        tien_phat = thoi_gian * 10000
        print("Bạn đã đi muộn dưới 15 phút, phạt nhẹ:", tien_phat, "VND")
    else: 
        # CÁI NÀY LÀ KHÔN NHẤT: Bất kỳ số nào lớn hơn 15 (16, 17, 20, 100...) đều rơi vào đây hết!
        tien_phat = thoi_gian * 20000 # Sửa lại đúng 20.000đ nha sếp
        print("Bạn đã đi muộn trên 15 phút, phạt nặng:", tien_phat, "VND")
        
    return tien_phat
danh_sach_muon = [ 10, 20 ,0 ,5 , 30] #khai báo biến danh sach thời gian chứa dữ liệu đi làm muộn

print("---HỆ THỐNG KIỂM TRA DANH SÁCH ĐI LÀM---")

for gio in danh_sach_muon: #biến giờ sẽ lấy từng phần tử trong danh sách muộn để chạy hàm và trả về kết quả
    ban = So_phut_di_muon(gio)


