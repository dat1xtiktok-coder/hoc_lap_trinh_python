khach_vip= ["Nguyễn Văn A", "Trần Thị B","Lê Hoàng C"] #input
with open ("vip.txt ", "w", encoding= "utf -8") as file:# tạo 1 file tên vip.txt ở chế độ ghi "w" encoding để không bị lỗi tiếng việt và biến file để chỉ flie đó 
    for khach in khach_vip:# tạo vòng lặp để lấy từng phần tử trong file
        file.write(khach +"\n") #biến file vừa tại ở as file dùng để ghi .write từng phần tử vào file
with open ("vip.txt", "r", encoding= "utf -8") as file:# tiếp tục mở lại file vip.txt nhưng ở chế độ đọc để lấy đó làm input cho trả về terminal
    input = file.read()#tạo 1 biến chứa dữ liệu đầu vào(từ file vừa tạo) để in ra terminal
    print(input) #in các phần tử từ biến trước đó đã tạo ra