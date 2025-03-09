#Giá bán
FRUIT_PRICE = {
    'cam': 5000,
    'tao': 6000,
    'xoai': 7000,
    'nho': 8000,
    'le': 9000
}

#hàm lấy thông tin trái cây và số lượng
def get_fruit_info():
    print("Danh sách trái cây và giá bán: ")
    for key, value in FRUIT_PRICE.items():
        print(f'{key}: {value} đồng/kg')

    tieptuc = ''
    lst = []
    while True:
        fruit = input("Nhập tên trái cây: ")
        weight = input("Nhập số kg: ")
        lst.append((fruit, weight))
        tieptuc = input("Tiếp tục mua (y/n): ")
        if tieptuc == 'n':
            break
    return lst

#hàm tính toán giá tiền
def calculate_price(fruit, weight, money):
    try:
        price = FRUIT_PRICE[fruit]
        total = price * float(weight)
        return_money = float(money) - total
        return return_money
    except KeyError:
        print(f"Trái cây {fruit} không tồn tại")
        return None
    except ValueError:
        print("Số kg không phù hợp")
        return None
    except:
        print(f"Lỗi: ")

def add_fruit(fruit, price):
    try:
        price = int(price)
        FRUIT_PRICE[fruit] = price
        print("Thêm trái cây thành công")
    except ValueError:
        print("Giá phải là số")

#menu chức năng
def menu():
    print('======   Menu   ======')
    print('1. Tính tiền')
    print('2. Thêm trái cây')
    print('3. Thoát')
    print('======================')

#vòng lặp while
while True:
    menu()
    choice = input("Chọn chức năng: ")
    if choice == "1":
        lst_giohang = get_fruit_info()
        money = input("Nhập số tiền: ")
        return_money = calculate_price(fruit, weight, money)
        if return_money is not None:
            if return_money < 0:
                print(f"Số tiền không đủ: {abs(return_money)}")
            elif return_money == 0:
                print("Số tiền chính xác")
            else:
                print(f"Số tiền thừa: {return_money}")
    elif choice == "2":
        fruit = input("Nhập tên trái cây: ")
        price = input("Nhập giá: ")
        add_fruit(fruit, price)
    elif choice == "3":
        print("Chương trình đã kết thúc")
        break
    else:
        print("Chức năng không tồn tại, vui lòng chọn lại")