def read_news_csv(file_name = "news.csv"):
    try:
        with open (file_name, "r", encoding = "utf-8-sig") as file:
            doc = file.readline()

            dong_can_tim = []

            for dong in file:
                if dong.endswith("duong_linh"):
                    continue
                dong_can_tim = dong.split(",")
                tieu_de = dong_can_tim[0]
                duong_link = dong_can_tim[1]
                print(f"Tiêu Đề {tieu_de} | Đường link {duong_link}")
                #nếu mà nó chạy thì sao không in trực tiếp biến đếm kèm index luôn :))
    except FileNotFoundError:
        print(f"cảnh báo {file_name} Không tồn tại")            

#test 
read_news_csv("news.csv")
read_news_csv("file_test.txt")


#clean code
def read_news_csv(file_name="news.csv"):
    try:
        with open(file_name, "r", encoding="utf-8-sig") as file:
            header = file.readline()  # Đọc bỏ dòng tiêu đề đầu tiên
            
            for dong in file:
                # Tách dòng thành list gồm [tiêu đề, link]
                cat_chuoi = dong.split(",")
                
                # Dùng .strip() để loại bỏ \n ở cuối link và khoảng trắng thừa
                tieu_de = cat_chuoi[0].strip()
                duong_link = cat_chuoi[1].strip()
                
                print(f"Tiêu đề: {tieu_de} | Đường link: {duong_link}")
                
    except FileNotFoundError:
        print(f" Cảnh báo: File {file_name} không tồn tại!")

# Test 2 trường hợp
read_news_csv("news.csv")
read_news_csv("file_test.txt")