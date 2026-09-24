ratings = [5, 4, 3, 5, 1, 2, 5, 4,]
def analyze_ratings(ratings_list):
    tong_luot = len(ratings_list)
    diem_trung_bing = sum(ratings_list)  / len(ratings_list)
    is_good =  diem_trung_bing >= 3.5
    return tong_luot, diem_trung_bing, is_good
total, avg, is_quality = analyze_ratings(ratings)
print(f"tổng lượt: {total} | điểm trung bình :{avg} | chất lượng đạt: {is_quality}")
    

    