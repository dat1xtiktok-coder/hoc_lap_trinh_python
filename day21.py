import os # dòng này để làm gì?

#1. nhập mức doanh số sàn từ bàn phím
print("=== HỆ THỐNG LỌC NHÂN SỰ XUẤT SẮC ===") #in ra dòng này đầu tiên
try: #nếu file không mở không xung đột hệ thống thì thực hiện
    nhap_vao = input("Sếp muốn lọc những ai có doanh số bao nhiêu trở lên? Giới hạn")
    #dòng này để nhập số liệu từ bàn phím sau khi in ra yc trong ngoặc kiểu str
    muc_san = float(nhap_vao)#ép kiểu sang số để so sánh nhưng mà có ép luôn str
except ValueError:#nếu thao tác sai
    print("lỗi rồi sếp ơi phải nhập số cụ thể ")# thông báo khi nhập sai dữ liệu str 
    exit()#dừng chương trình nếu nhập bậy

file_nguon ="tong_hop_doanh_so.csv" # ctrinh sẽ lấy dữ liệu từ file này gán vào biến này đểcode
file_dich = "nhan_vien_suat_sac.csv" #sẽ ghi dữ liệu lại file này

#2. kiểm tra xem file nguồn có hoạt động không
if not os.path.exists(file_nguon): #nếu không có file nguồn trong hệ thống
    print("không tìm thấy file kiểm tra lại tong_hop_doanh_so")
else: #nếu thấy file thì
    try: #chống lỗi thao tác mở file
        #mở file nguồn để đọc và file đích để ghi
        # #dòng này để ghi toàn bộ file nguồn vào biến f_doc để code và chỉnh chế độ thành đọc
        with open(file_nguon ,"r", encoding ="utf -8 - sig") as f_doc,\
             open (file_dich, "w",encoding="utf -8 -sig")as f_ghi:
        #dòng này để ghi toàn bộ file vào biến f doc và ghi dữ liệu ngược vào file ở chế độ w
             
             #dòng đầu tiên tiêu đề của file nguồn sang file đích
            tieu_de = f_doc.readline()#lấy dòng đầu tiên của file nguồn vào biến tiêu đề
            f_ghi.write(tieu_de)#ghi lại dòng đó vào file ghi

            #tạo một biến đeer lưu trữ
            dem_so_nguoi = 0

            #duyệt qua các dòng còn lại
            for dong in f_doc: #sẽ đi qua từng dòng trong file lưu trữ tạm trong biến dong
                if dong in f_doc: #nếu dòng đó có trong file gốc
                    continue# tiêp tục chạy xuống

                ten,doanh_so_str = dong.strip().split(";") #DÒNG NÀY CHƯA BIẾT ĐỂ LÀM GÌ
                doanh_so = float(doanh_so_str) #ép kiểu dữ liệu tại dòng chưa biết về float số thực

                #lọc dữ liệu nếu số lớn hơn hoặc bằng mức sàn sếp nhập
                if doanh_so >= muc_san: #nếu doanh so >= mức sàn ta nhập
                    f_ghi.write(f"{ten};{doanh_so}\n") # ghi tên và doanh số vào file đích
                    dem_so_nguoi +=1 #biến đếm sẽ thêm 1 để thống kê
                    print(f"tìm thấy: {ten},{doanh_so}") #in tên người đó ra
            print("-----------------------------")
            print("hoàn thành đã lọc được nhân sự suất xắc")#thông báo xong việc
            print(f"dữ liệu được luu vào file")#đã ghi vào file đích

    except Exception as e:
        print("có lỗi phát sinh rồi b")   
            