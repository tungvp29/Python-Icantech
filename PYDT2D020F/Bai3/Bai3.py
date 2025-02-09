#Tra cứu mã vùng địa phương
Location_data = (
    ('Ha noi', 100000),
    ('Hai Phong', 200000),
    ('Da Nang', 300000),
    ('Ho Chi Minh', 700000),
    ('Can Tho', 940000),
    ('Hue', 530000),
    ('Ha Giang', 310000),
)

def menu():
    print('1. Hiển thị thông tin địa phương')
    print('2. Đếm số lượng địa phương')
    print('3. Kiểm tra địa phương tồn tại')
    print('4. Thoát')

def display_location_info():
    diaPhuong = input('Nhập tên địa phương cần tìm: ')
    for location in Location_data:
        if location[0] == diaPhuong:
            print(f'Mã vùng của {diaPhuong} là: ', location[1])
            break
    else:
        print(f'Không tìm thấy {diaPhuong}')  

def count_locations():
    print('Số lượng địa phương: ', len(Location_data))

def check_location_exists():
    diaPhuong = input('Nhập tên địa phương cần tìm: ')
    #comprehension trong python
    if any(diaPhuong == location[0] for location in Location_data):
        print(f'{diaPhuong} tồn tại')
    else:
        print(f'{diaPhuong} không tồn tại')

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
        print('Chức năng không tồn tại, vui lòng chọn lại!')
    #các elif khác
