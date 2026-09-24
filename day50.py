danh_sach_file = ["nhan_vien.csv", "baocao_rac.tmp", "doanh_so.csv", "danh_sach_ip.txt"]

for file in danh_sach_file:
    if file.strip().lower().endswith(".tmp"):#phương thức endswith dùng để lọc đuôi fileS
        print(f"bỏ qua file rác {file}")
        continue

    elif file == "danh_sach_ip.txt".strip().lower():
        print(f"phát hiện file không đúng định dạng: {file} !! dừng chương trình")
        break

    else:
        print(f"đang xử lý dữ liệu: {file}")