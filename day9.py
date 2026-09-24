import pprint
dien_thoai = {
    "ten_may": "iPhone 15",
    "gia_ban": 22000000,
    "so_luong_kho": 10
}

dien_thoai["so_luong_kho"] = 10+5
dien_thoai["gia_ban"] = 28500000
dien_thoai["thoi_gian_bao_hanh"] = "12 tháng"

pprint.pprint(dien_thoai)