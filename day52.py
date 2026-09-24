thong_tin_san_pham= {
    "ten_sp" : "tai nghe Bluetooth",
    "gia_niem_yet": 500000,
    "so_luong_kho" : 8
}
giam_gia = thong_tin_san_pham.get("giam_gia", 50000)
print(f"tiền giảm giá:{giam_gia}")

for key , value in thong_tin_san_pham.items():
    print(f"Thuộc tính [{key}] có giá trị là {value}")
