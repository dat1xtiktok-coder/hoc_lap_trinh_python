raw_title = "    [TIN NÓNG] giá vàng hôm nay    tăng kỷ lục!    \n"
raw_link = "https://vnexoress.net/gia-bang-hom-nay-12345.html"

def clean_new_data(title,link):
    clean_title = title.strip().replace("[TIN NÓNG]","")
    #xử lý link
    check_link = link.endswith(".html") #bản thân endswith là kiểm tra điều kiện nên trả vể (return) sẽ là true false
    return clean_title , check_link

#ct chính (test)
title_ok, link_ok = clean_new_data(raw_title, raw_link)
print(f"tiêu đề: {title_ok} | link hợp lệ: {link_ok}")