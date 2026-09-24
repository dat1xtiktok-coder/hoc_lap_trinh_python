#1. Tạo class (bản thiết kế)
class AutomationBot:
    #hàm khởi tại định nghĩa thông tin ban đầu của từng con bot
    def __init__(self, name, proxy):
        self.name = name # thuộc tính Tên bot
        self.proxy = proxy #thuộc tính địa chỉ ip proxy
        self.satus = "Stopped" #trạng thái mặc định

    #phương thức(methol): hành động mà bot có thể làm (hàm)
    def start_bot(self):
        self.satus = "Running" #chỉnh trạng thái 
        print(f"[{self.name}] Đã bật trình duyệt với proxy : {self.proxy}")

    #phương thức kiểm tra trạng thái và bot đang chạy
    def show_info(self):
        print(f"Bot: {self.name} | Satus: {self.satus}")

#2. chạy thử trong main
if __name__ == "__main__":
    #tạo object từ clas(đối tượng đưa vào class)
    bot_shoppe = AutomationBot("Bot Shoppe", "192.168.1.1:8080")

    #tạo object 2 từ class 
    bot_tiktok = AutomationBot("Bot Tiktok", "10.0.0.1:9090")

#cho từng bot thực hiện hành động 
bot_shoppe.start_bot()
bot_tiktok.show_info()

#bot tiktok vấn đang stopped vì chưa gọi start_bot()
bot_tiktok.show_info()











