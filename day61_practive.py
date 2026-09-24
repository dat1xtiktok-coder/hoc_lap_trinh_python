class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    def nap_tien(self, amount):
        self.balance = self.balance + amount
    
    def hien_thi_thong_tin(self):
        print(f"Tên: {self.name} | Email: {self.email} | Số dư: {self.balance}")



if __name__ == "__main__":
    khach1 = Customer("ĐẠT", "datcus1@gmail.com")
    khach2 = Customer("DŨNG", "dungcus2@gmail.com")

    khach1.hien_thi_thong_tin()
    khach2.hien_thi_thong_tin()