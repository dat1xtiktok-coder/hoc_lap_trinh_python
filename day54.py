def scrape_website(url, max_page=5):
    print(f"đang cào dữ liệu từ {url} với số trang là {max_page}")
    return "THÀNH CÔNG"

cao1 = scrape_website("[https://tiki.vn](https://tiki.vn)")

print (cao1)

cao2 = scrape_website("[https://shopee.vn](https://shopee.vn)",20)
print(cao2)