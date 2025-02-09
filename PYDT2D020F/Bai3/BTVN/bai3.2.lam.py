LOCATION_DATA = (
    ("Ha Noi", "100000"),
    ("Ho Chi Minh", "700000"),
    ("Da Nang", "550000"),
    ("Can Tho", "900000"),
    ("Hai Phong", "180000"),
    ("Nha Trang", "650000"),
    ("Hue", "530000"),
    ("Quy Nhon", "590000"),
    ("Vung Tau", "790000"),
    ("Phu Quoc", "920000"),
)

def normalize(_str):
    return _str.lower().strip()

def display_menu():
    print("\n------MENU------")
    print("1. Hien thi thong tin dia phuong")
    print("2. Dem so luong dia phuong")
    print("3.Kiem tra dia phuong co ton tai trong danh sach hay khong")
    print("4.Thoat")
def display_location_info():
    postal_code = input("\nNhap ten dia phuong can tim: ") 

    for location in LOCATION_DATA:
        if normalize(location[0]) == normalize(postal_code):
            print(location[0], "co ma vung buu dien la:", location[1])
            break
    else:   #shift + tab
        print("khong tim thay vung buu dien tuong ung voi dia phuong da nhap")
def count_locations():
    print("\nSo luong dia phuong trong danh sach la:",len(LOCATION_DATA))

def check_location_exists():
    location_name = input("\nNhap ten dia phuong can kiem tra: ")

    if any(location_name in location for location in LOCATION_DATA):
        print("Dia phuong", location_name, "da co tung trong danh sach")
        print(f"Dia phuong {location_name} da co tung trong danh sach")
    else:
        print("Dia phuong", location_name, "khong co trong danh sach")

while True:
    display_menu()
    choice = input("\nNhap lua chon cua ban: ")
    if choice == "1":
        display_location_info()
    elif choice == "2":
        count_locations()
    elif choice == "3":
        check_location_exists()
    elif choice == "4":
        print("\nChuong trinh da ket thuc")
        break
    else:
        print("\nLua chon khong hop le, vui long nhap lai")