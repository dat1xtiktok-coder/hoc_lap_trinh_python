scraped_data = [ 
    ("Giá vàng hôm nay tăng mạnh", "http://vnexpress.net/gia_vang-12345.html"),
    ("Chỉ sos VN=Index vượt mốc 1200", "http://vnexpress.net/vn-index-67890.html")
]
#input bài toán

def save_to_csv(data_list, filename = "news.csv"):
    with open(filename, "w", encoding = "utf-8-sig" )as file:
        file.write("Tieu_de, Duong_link\n") #file.write để ghi vào trong file trên ram
        for tupe in data_list:
            dinh_dang = f"{tupe[0]},{tupe[1]}\n"
            file.write(dinh_dang)

            print(f"đã lưu định dạng vào: {filename}")

save_to_csv(scraped_data)
