#chặng 1 : khởi tạo tên lửa
#tạo một danh sách rỗng để chứa tất cả các sản phẩm nhập vào
danh_sach_ban_hang =[] # TẠO MỘT BIẾN RỖNG LƯU DỮ LIỆU

print("===HỆ THỐNG QUẢN LÝ DOANH THU CỬA HÀNG===")#TÊN HỆ THỐNG

while True:# nếu điều kiện đúng
    print("\n---MENU QUẢN LÝ----")
    print("1.Nhập sản phẩm mới")
    print("2.xem danh sách và thoát trương trình")

    lua_chon = input("mời sếp chọn tính năng 1 hoặc hai")# nhập một hoặc hai từ bàn phím và tiếp tục câu lệnh

    if lua_chon =="1": #nếu biến nhập nhận giá trị bằng 1 str()
        print("\n[TIẾN HÀNH NHẬP SẢN PHẨM]")#vì lựa chọn 1 là nhập sản phẩn nên sẽ in ra dòng này để thông báo
        #1 nhập thông tin từ bàn phím
        ten_sp = input("nhập tên sản phẩm: ")
        so_luong = int(input("nhập số lượng bán: "))#nhập số lượng kiểu int số nguyên
        gia_ban = int(input("nhập giá bán(VND):"))

        #gom ba thôn tin này thành một dictionary cho dễ quản lý
        san_pham = {
            "ten": ten_sp,
            "so_luong": so_luong,
            "gia": gia_ban
        }#->lúc này các dữ liệu trong biến lại được lưu vào các chuỗi 

        danh_sach_ban_hang.append(san_pham)#dùng lệnh .append để ghi cái dictionary vào biến tạo ở đầu file

        print(f"-> đã thêm sản phẩm{ten_sp} vào hệ thống thành công!")

    elif lua_chon == "2":
        print("\n[DANH SACH BÁO CÁO CỦA DOANH THU]:")
        tong_doanh_thu_cua_hang = 0
        #1.bước mở file : mở một file để ghi dữ liệu (chế độ  "w" - write)
        #lệnh này sẽ tự động đẻ ra file bao_cao_doanh_thu.txt trong máy
        with open ("bao_cao_doanh_thu.txt", "w", encoding = "utf - 8") as file: #khai báo file tạo file và sử dụng chế độ ghi để ghi dữ liệu

            #ghi tiêu đề
            file.write("===BAO CÁO DOANH THU CỬA HÀNG===\n\n")

            for sp in danh_sach_ban_hang:
                tien_cua_sp = sp ["so_luong"] *sp["gia"]
                tong_doanh_thu_cua_hang = tong_doanh_thu_cua_hang +tien_cua_sp

                dong_thong_tin = f"Sản phẩm {sp['ten']}: bán được{sp["gia"]}cái | Doanh thu: {tien_cua_sp}VND\n" #định dạng của các dòng văn bản ghi vào file

                print(dong_thong_tin.strip())#in ra màn ginhf teminal
                file.write(f"TỔNG DOANH THU CỦA HÀNG:{tong_doanh_thu_cua_hang}VND\n")

        #kết thúc khối with open file được lưu và đogns án toàn
        print("-"*30)
        print(f"tổng doanh thu:{tong_doanh_thu_cua_hang}VND")
        print("đã xuất dữ liệu vào file bao_cao_doanh_thu.txt thành công")
        print("\n thoát chương trình hẹn gặp lại")



    else:
        print("lựa chọn không hợp lệ, mời sếp chọn lại")