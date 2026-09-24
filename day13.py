try:  
    with open ("luong_tho.csv", "w", encoding = "utf-8-sig") as file: 
        file.write("test bọc giáp hệ thống")
except PermissionError:
    print("Tắt file đi nhé !!!")
else:
     print("Ghi file thành công ")