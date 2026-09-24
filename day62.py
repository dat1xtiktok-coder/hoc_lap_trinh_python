class Customer:
    def __init__(self, name, email):
        #1. kiểm tra email phải có dấu@
        if "@" not in email:
            raise ValueError (f"Email '{email}' không hợp lệ thiếu dấu '@'")

        self.name = name
        self.email = email
        self.balance = 0

    def nap_tien(self, amount):
        #kiểm tra số tiền nạp phải lớn hơn o
        if amount <= 0:
            raise ValueError("số tiền nạp phải lớn hơn 0")

        self.balance += amount
        print(f"[{self.name}] Nạp thành công {amount:,} VND . Số dư mới: {self.balance} VND")

    def rut_tien(self, amount):
        if amount <= 0:
            raise ValueError ("số tiền nạp phải lớn hơn 0")
        elif amount > self.balance :
            raise ValueError ("số dư không đủ để rút")

        

#chạy thử bẫy lỗi 
if __name__ == "__main__":
    print("---- chạy thử bẫy lỗi khi tạo khách hàng ----")

    #th1 lỗi email
    try:
        khach_bad = Customer("Đạt Lỗi", "datlangson.com")#thiếu @
    except ValueError as e:
        print(f" lỗi bắt được {e}")




    #lỗi nạp tiền 
    print("\n --- THỬ BẪY LỖI NẠP TIỀN---")
    try:
        khach_ok = Customer("Thành Đạt", "dat@gmail.com")
        khach_ok.nap_tien(5000000)
        khach_ok.nap_tien(-500000)
    except ValueError as e:
        print(f"bắt được lỗi {e}")
    print ("chương trình vẫn chạy bình thường chưa bị sập")



    #lỗi rút tiền 
    try:
        khach_ok.rut_tien(10000000)
       #khach_ok.rut_tien(100000)
    except ValueError as e:
        print(f"bắt lỗi : {e}")