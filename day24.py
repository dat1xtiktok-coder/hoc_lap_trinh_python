import os # khai báo hệ điều hành sẽ kiểm tra file
print ("=== HỆ THỐNG XỬ LÝ BIỆT LỆ VÀ LÀM SẠCH DỮ LIỆU LỖI===")

input1 = "data_input.txt" # gom dữ liệu trong file vào biến này
output1 = "eror_log.txt" # các dữ liệu lỗi được ghi vào đây
output2 = "tong_doanh_thu.txt"#các dữ liệu sạch đã tính toán thông tin vào đây
tong_doanh_thu= 0
if not os.path.exists(input1):
        print("---KHÔNG TÌM THẤY FILE TRONG HỆ THỐNG---")
else:
    #mở file để đọc nội dung
    with open (input1,"r",encoding="utf -8")as f:
         for dong in f:
             dong = dong.strip()#.strip xóa khoảng trắng thừa và dấu xuống dòng
             if not dong:#nếu dòng trống
                 continue
               
             try:
                #tách dòng thàn 3 phần dựa vào dấu -
                thong_tin = dong.split("-")

                #nếu không đủ 3 phần = thiếu thông tin
                if len(thong_tin) !=3:#thông tin không đủ 3 phần dựa vào dấu gạch
                     raise (IndexError("thiếu thông tin sản phẩm"))#thông báo lỗi
                
                ten_sp = thong_tin[0]#định nghĩ biến tức là hứng vị trí sau khi cắt
                so_luong = int(thong_tin[1])#biến số lượng  lưu trữ giá trị là số nếu là chữ thì thong báo lỗi
                don_gia = int(thong_tin[2])#không phải số bắn ra thông báo lỗi
                
                # nếu chạy đến đây mà mượt tức là dữ liệu sạch
                print(f"hợp lệ:{ten_sp} | thành tiền:{so_luong * don_gia}")
        
                 # Cộng dồn số tiền của dòng hiện tại vào tổng tích lũy
                tong_doanh_thu = tong_doanh_thu + (so_luong * don_gia)
            #nếu dòng lỗi 
             except (ValueError, IndexError) as e:
                  #nếu dòng lỗi py nhảy vào đây
                print(f"Phát hiện dòng lỗi :{dong} ->lý do:{e}")
                with open ("eror_log.txt", "a", encoding=("utf-8")) as f1:
                     
                     f1.write(f"dòng lỗi: {dong}    | lý do: {e}\n")
# ĐẶT SÁT LỀ TRÁI - Khi vòng lặp for chạy xong hết toàn bộ các dòng
with open(output2, "w", encoding="utf-8") as f:
    f.write(f"Tổng doanh thu hệ thống: {tong_doanh_thu}")
