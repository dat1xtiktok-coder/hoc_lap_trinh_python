import os #khai báo với hệ điều hành để kiểm tra file

print("== HỆ THỐNG THỐNG KÊ SỐ LƯỢNG ĐƠN HÀNG===")

file_nguon = "tong_hop_doanh_so.csv"#gắn file vào biến để code đây là file lấy dữ liệu
file_dich = "thong_ke_don_hang.csv"#tạo ra một biến và lát nữa tạo file để ghi kết quả

#tạo một dictionaty trống để lưu : tên nhân viên : số lượng đơn
dem_don_hang = {}

if not os.path.exists(file_nguon):#logic kiểm tra file nguồn có trong hệ thống hay không
    print(f"không tìm thấy file {file_nguon}")#in ra dòng này và tên file
else:#nếu có file trong hệ thống
    #đọc flie và đếm 
    with open(file_nguon, "r", encoding = "utf - 8 -sig") as f_doc:#mở file với chế độ đọc và ghi vào biến f_nguon
    #bỏ qua các dòng tiêu đề
     f_doc.readline()

     for dong in f_doc:#lặp chạy qua từng dòng trong file nguồn
        if dong.strip() == "" or "Tên" in dong:# nếu dòng có khoảng trắng thừa và chữ tên thì đi tếp
            continue

        #cắt chuỗi lấy phần tên (bỏ qua phần doanh số vì bài này chỉ đếm người)
        ten, _ = dong.strip().split(";")#cho phần có tên vào biến tên còn lại vào biến _ vì không sử dụng cắt tại vị trí ; tức các cột

        #logic đếm của bài
        if ten not in dem_don_hang:# nếu ten không có trong biến đã tạo trước đó
            dem_don_hang[ten] =1 #lầm đầu tiên thấy người này máy tính tính là 1 đơn
        else:#nếu trong biến đã chạy có tên người này
            dem_don_hang[ten] +=1 #đã có tên cộng thêm 1

    #2. ghi kết quả ra file mới 
        with open (file_dich, "w", encoding ="utf -8 - sig")as file_ghi:#lệnh tạo file để ghi kết quả
        #ghi tiêu đề cho file mới
            file_ghi.write("Tên nhân viên ; số lượng đơn hàng \n")

    #duyẹt qua dictionary để ghi từng người vào file 
            for ten,so_don in dem_don_hang.items():#lọc qua từng người trong dictionary
                file_ghi.write(f"{ten};{so_don}\n") #ghi tên người đó vào file
            print(f"nhân viên{ten}| đã chốt {so_don}đơn")

    print("-"*40)
    print(f"hoàn thành kết quả thống kê đã lưu vào file đích")