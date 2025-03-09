Location_data = (
    ('Ha Noi', 100000),
    ('Hai Phong', 200000),
    ('Da Nang', 300000),
    ('Ho Chi Minh', 700000),
    ('Can Tho', 940000),
    ('Hue', 530000),
    ('Ha Giang', 310000))
def display_location_info():
    pass
def count_locations():
    print('Số lượng địa phương: ', len(Location_data))
def check_location_exists():
    pass
def menu():
    print('1. Hiển thị thông tin địa phương')
    print('2. Đếm số lượng địa phương')
    print('3. Kiểm tra vị trí hiện tại')
    print('4. Thoát')
while True:
    menu()
    choice = input('Chọn chức năng: ')
    if choice == '1':
        display_location_info()
    elif choice == '2':
        count_locations()
    elif choice == '3':
        check_location_exists()
    elif choice == '4':
        break
    else:
        print('Chức năng không tồn tại, chọn cái khác đi: ')

