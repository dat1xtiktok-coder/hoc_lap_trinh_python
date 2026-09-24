kho_dien_thoai = [
    {"ten": "Iphone 15 pro","gia":28000000 ,"so_luong":5},
    {"ten": "SamSung A55", "gia" : 10000000, "so_luong":12},
    {"ten": "Xiaomi 14 ", "gia":21000000 ,"so_luong":8},
    {"ten": "Oppo A18", "gia":35000000, "so_luong":2}
]
tong_tai_san =0
for san_pham in kho_dien_thoai:
    tong_tien = san_pham["so_luong"] * san_pham["gia"]
    print("tong tien cua san pham:", san_pham["ten"], "là:", tong_tien )
    tong_tai_san += tong_tien
    print("-" * 40)
    if san_pham["gia"] >= 20000000:
        print(  "số sản phẩm lớn hơn 20000000 là:",san_pham['ten'])
        print("-" * 40)
