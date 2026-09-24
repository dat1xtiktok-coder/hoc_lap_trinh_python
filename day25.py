try: #bọc nếu không lỗi xung đột từ hệ thống lỗi mở file thì sẽ vào đây
    so_bi_chia = int(input("nhập tử số:")) #lệnh gán vào biến một con số từ bàn phím int()khai báo kiểu dữ liệu input()lệnh nhập
    so_chia = int(input("nhập mẫu số:"))#như lệnh dòng ba

    ket_qua = so_bi_chia / so_chia # lệnh gán phép tính vào biến kết quả của phép tính sẽ được lưu ở hai biến yêu cầu nhập ở dòng 3 và 4
    print(f"->kết quả :{ket_qua}")#dùng cú pháp f để đưa biến vào  trong ngoặc -> in trực tiếp ra kết quả

except ZeroDivisionError: # bọc lại nếu trong try xảy ra các lỗi nhập liệu hoặc sai quy luật
    print("LỖI: không thể chia cho số 0")

except ValueError:
        print(  "hãy nhập số bị  chia:từ 0-9\nhãy nhập so chia:từ 1-9")

