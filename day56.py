def calculate_total_spend(*prices, **extra_info):
    # Tính tổng các giá trị truyền qua *prices
    tong_chi_phi = sum(prices)
    print(f"Tổng chi phí: {tong_chi_phi}")
    
    # In thông tin phụ trợ từ **extra_info
    print("Thông tin bổ sung:")
    for key, value in extra_info.items():
        print(f"  - {key}: {value}")
        
    return tong_chi_phi

# Gọi hàm thực thi
total = calculate_total_spend(150, 200, 350, currency="USD", tax_included=True)
print(f"Kết quả trả về: {total}")
#khi chương trình chạy
#tham số truyền vào price (150, 200, 350) > đi vào hàm > trong hàm thực hiện cộng tổng bằng sum() sau đó gán vào tong chi phi rối return ra ngoài
#tham số truyền vào extra_info (currency  = "usd" , tax_included = true)> đi vào hàm> sau đó vào vòng lặp for thực hiện lấy các giá trị value và key rồi in chúng ra dưới dạng - key : value
#nếu vậy thì các tham số được truyền vào vòng lặp ta đâu có retrun ra ngoài đâu sao lại hiện kết quả nếu ta gọi hàm ở dòng 14 và gắn vào total thì cũng chỉ in ra kết quả của phép tính sum() còn trong vòng lặp thì sao ?