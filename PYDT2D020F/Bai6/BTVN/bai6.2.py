FRUIT_PRICES = {
    'tao':40000,
    'chuoi':15000,
    'cam':90000,
    'xoai':45000,
    'nho':180000
}
def get_fruit_info():
    print("Chon loai trai cay:")
    for fruit, price in FRUIT_PRICES.items():
        print(f"-{fruit}: {price} dong/kg")
        
    fruit = input("Nhap loai trai cay: ").lower()
    weight = input("Nhap so luong(Kg): ")
    return fruit,weight

def calculate_price(fruit, weight, money):
    try:
        price_per_kg = FRUIT_PRICES[fruit]          #giá tiền của 1kg trái cây
        weight=float(weight)                        #trọng lượng trái cây
        cal_price = int(money) - (price_per_kg * weight)
        print(f'Gia tien cua {weight}kg {fruit} la: {price_per_kg * weight} dong')
        print(f'Khach tra: {money} dong')
        print(f'Tien thua: {cal_price} dong')
    except KeyError:
        print(f"Loi: {fruit}khong co trong danh sach gia ban")
        return
    except ValueError:
        print("Loi: gia tri nhap khong hop le.")
        return

while True:
    print("=========MENU=========")
    print("1. Tinh gia tien")
    print("2. Thoat")
    choice = input("Vui long chon (1/2: )")

    if choice == "1":
        fruit, weight = get_fruit_info()
        money = input("Nhap so tien hanh khach tra (dong): ")
        calculate_price(fruit, weight, money)
    elif choice == "2":
        break
    else:
        print("Tuy chon khong hop le vui long chon lai")

