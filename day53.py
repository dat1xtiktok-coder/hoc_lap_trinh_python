raw_product = {
    "name": "  laptop dell xps 13    ",
    "price": "28.500.000 vnd",
    "status": "  con hang   "
}

def clean_text(text):
    text_clean = text.strip().title()
    return text_clean

def clean_price(price_str):
    pricer = price_str.replace("vnd", "").replace(".","").strip()

    final = int(pricer)

    return final


    # --- YÊU CẦU 3: LẮP RÁP VÀO TỪ ĐIỂN MỚI ---

# Tạo một từ điển mới sạch sẽ
clean_product = {
    "name": clean_text(raw_product["name"]),
    "price": clean_price(raw_product["price"]),
    "status": clean_text(raw_product["status"])
}

# In kết quả ra màn hình để kiểm tra
print("Dữ liệu gốc bẩn:")
print(raw_product)

print("\nDữ liệu sau khi làm sạch:")
print(clean_product)
4