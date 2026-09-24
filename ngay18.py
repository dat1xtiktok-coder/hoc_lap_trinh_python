def Diem_trung_binh(ten , diem_lt, diem_th):
    diem_tb = (float(diem_lt) + float(diem_th)) /2
    chuoi_sach = f"{ten};{diem_tb}\n"
    return diem_tb, chuoi_sach
#2. Khối lệnh 1 đọc file - ghi file song hành 
try:
    #mở song song 3 file 1 file đọc 2 file ghi đạt và trượt
    with open ("diem_tho.csv", "r" , encoding ="utf-8-sig") as file_doc,\
         open ("Hoc_singdat.csv", "w", encoding= "utf-8-sig")as file_dat,\ 
         open("hoc_sinh_truot.csv", "w", encoding ="utf-8-sig")as file_truot:
        
        #ghi dòng tiêu đề cho 2 file kết quả 
        file_dat.write("Tên Học sinh; Điểm trung bình\n")# ghivaof file tạo from
        file_truot.write("tên học sinh; điểm trung bình\n")#tạo form file

        #vòng lặp quyét qua từng dòng trong file điểm thô
        for dong in file_doc:
            #lọc dòng tiêu đề gốc 
            if "Tên"in dong or dong.strip=="":
                continue
        
            #cắt dữ liệu bằng ;
            cat_du_lieu = dong.split(";")

            #ném dữ liệu vào hàm 
            diem, dong_ghi_file = Diem_trung_binh(cat_du_lieu[0],cat_du_lieu[1],cat_du_lieu[2])

            #sau khi tính toán đưa vào điều kiện ghi vào 2 file đã chuẩn bj
            if diem >= 5.0:
                #nếu điểm từ 5.0 trở lên ghi vào file đạt
                file_dat.write(dong_ghi_file)
            else:
                #nếu dưới 5 điểm ghi vào file trượt
                file_truot.write(dong_ghi_file)


except PermissionError:
    print("Sếp ơi tắt file đi exel đang mở")
except Exception as e:
    print(f"Có lỗi phát sinh:{e}")
else: print("đã phân loại xong")