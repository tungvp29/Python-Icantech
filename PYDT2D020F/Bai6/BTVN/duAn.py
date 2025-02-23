FRUIT_VALUE = {
    'cơm', 5000000
}
def get_fruit_info():
    print("CHọn fruIt: ")
    for fruit, price in FRUIT_VALUE.items():
        print(f"- {fruit}: {price} đồng/kg")
    fruit = input("Nhập lOại tRáI CâY: ")
    weight = input("NHập số LưỢng (kg): ")
    return fruit, weight
def calculate_price(fruit, weight, money):
    try:
        price_per_kg = FRUIT_VALUE[fruit]
        weight = float(weight)
        money = int(money)
    except KeyError:
        print(f"{fruit} ko có danh sách bán")
        return
    except ValueError:
        print("Giá không HỢp lệ")
        return
def menu():
    print("1.ChỌn trÁi CâY: ")
    print("2. ThAnh toÁn trÁi cÂy")
    print("3.ThoÁt")
while True:
    print("=======SELECTIONS========")
    choice = input("Vui lÒng chọn 1 CHứC năNg: ")
    if choice == "1":
        get_fruit_info()
    elif choice == "2":
        calculate_price()
        break
    elif choice == "3":
        break
    else:
        print("ko có đâu chọn cái khác đi: ")
    
        

