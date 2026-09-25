import csv

def hien_thi_danh_sach():
    try:
        with open('khach_hang.csv', mode='r', encoding='utf-8') as file:
            noi_dung = list(csv.reader(file))
            
            if not noi_dung:
                print("\n[!] File dữ liệu đang trống!")
                return
            
            print("\n--- DANH SÁCH KHÁCH HÀNG ---")
            for dong in noi_dung:
                if not dong:
                    continue
                # Nếu đủ 5 cột thì in căn chỉnh chuẩn
                if len(dong) >= 5:
                    print(f"{dong[0]:<5} | {dong[1]:<20} | {dong[2]:<12} | {dong[3]:<12} | {dong[4]}")
                else:
                    # Nếu dòng bị thiếu cột vẫn in đẹp mắt
                    print(" | ".join(f"{item:<12}" for item in dong))
            print("-" * 60)
    except FileNotFoundError:
        print("\n[!] Lỗi: Không tìm thấy file khach_hang.csv!")

def them_khach_hang():
    print("\n--- THÊM KHÁCH HÀNG MỚI ---")
    ten = input("Nhập họ và tên: ")
    sdt = input("Nhập số điện thoại: ")
    
    try:
        doanh_so = int(input("Nhập doanh số mua hàng (VNĐ): "))
    except ValueError:
        print("[!] Doanh số phải là số nguyên! Thêm thất bại.")
        return

    phan_loai = "VIP" if doanh_so >= 10000000 else "Normal"

    # Kiểm tra xem dòng cuối của file có ký tự xuống dòng chưa
    can_xuong_dong = False
    try:
        with open('khach_hang.csv', mode='r', encoding='utf-8') as file:
            noi_dung = file.read()
            if noi_dung and not noi_dung.endswith('\n'):
                can_xuong_dong = True
            
            lines = [line for line in noi_dung.splitlines() if line.strip()]
            stt = len(lines)
    except FileNotFoundError:
        stt = 1

    with open('khach_hang.csv', mode='a', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        if can_xuong_dong:
            file.write('\n')
        writer.writerow([stt, ten, sdt, doanh_so, phan_loai])

    print(f"--> Thêm thành công khách hàng {ten} ({phan_loai})!")

def tim_kiem_khach_hang():
    print("\n--- TÌM KIẾM KHÁCH HÀNG ---")
    tu_khoa = input("Nhập tên hoặc SĐT cần tìm: ").strip().lower()
    
    if not tu_khoa:
        print("[!] Từ khóa không được để trống!")
        return

    try:
        with open('khach_hang.csv', mode='r', encoding='utf-8') as file:
            noi_dung = list(csv.reader(file))
            ket_qua = []
            
            # Bỏ qua dòng tiêu đề (dòng 0), tìm từ dòng 1 trở đi
            for dong in noi_dung[1:]:
                if len(dong) >= 3:
                    ten = dong[1].lower()
                    sdt = dong[2].lower()
                    if tu_khoa in ten or tu_khoa in sdt:
                        ket_qua.append(dong)
            
            if ket_qua:
                print(f"\n[+] Tìm thấy {len(ket_qua)} kết quả phù hợp:")
                print(f"{'STT':<5} | {'Họ và tên':<20} | {'SĐT':<12} | {'Doanh số':<12} | Phân loại")
                print("-" * 60)
                for dong in ket_qua:
                    if len(dong) >= 5:
                        print(f"{dong[0]:<5} | {dong[1]:<20} | {dong[2]:<12} | {dong[3]:<12} | {dong[4]}")
                    else:
                        print(" | ".join(dong))
                print("-" * 60)
            else:
                print(f"\n[-] Không tìm thấy khách hàng nào chứa từ khóa '{tu_khoa}'!")
    except FileNotFoundError:
        print("\n[!] Lỗi: Không tìm thấy file khach_hang.csv!")

def hien_thi_menu():
    print("\n=== HỆ THỐNG QUẢN LÝ KHÁCH HÀNG ===")
    print("1. Xem danh sách khách hàng")
    print("2. Thêm khách hàng mới")
    print("3. Tìm kiếm khách hàng")
    print("4. Thoát chương trình")

# Luồng chạy chính (Main Loop)
while True:
    hien_thi_menu()
    lua_chon = input("Sếp chọn chức năng (1-4): ")
    
    if lua_chon == '1':
        hien_thi_danh_sach()
    elif lua_chon == '2':
        them_khach_hang()
    elif lua_chon == '3':
        tim_kiem_khach_hang()
    elif lua_chon == '4':
        print("\nCảm ơn sếp đã sử dụng phần mềm. Tạm biệt!")
        break
    else:
        print("\n[!] Lựa chọn không hợp lệ, vui lòng chọn lại từ 1 đến 4!")