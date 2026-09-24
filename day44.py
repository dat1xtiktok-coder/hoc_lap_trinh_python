the_hop_le = True
so_du = 30000000
so_tien_muon_rut = 5000000

if the_hop_le == True:
    if so_du >= so_tien_muon_rut:
        print("Giao dịch thành công ! đang nhả tiền ...")
    else:
        print(" giao dịch thất bại: số dư tài khoản 0 đủ")
else:
    print("Lỗi : thẻ không hợp lệ hoặc đã bị khóa")