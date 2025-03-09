
def save_file(data):
    f = open('shape.out', 'w')
    f.write(data)
    f.close()
    print('Hình vẽ đã được lưu lại!')

def get_data(list):
    data = ''
    for i in range(len(list)):
        for j in range(len(list[i])):
            data += list[i][j] + ' '
        data += '\n'
    return data

def menu():
    print('1. Vẽ hình vuông')
    print('2. Vẽ hình chữ nhật')
    print('3. Vẽ hình tam giác vuông cân')
    print('4. Vẽ cây thông Noel')
    print('5. Thoát')

def veHinhVuong(n, kyHieu = '*'):
    square = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(kyHieu)
        square.append(row)
    return square
    
def veHinhChuNhat(dai, rong):
    rectangle = []
    for i in range(dai):
        row = []
        for j in range(rong):
            row.append('*')
        rectangle.append(row)
    return rectangle

def veHinhTamGiac(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(n):
            if j <= i:
                row.append('*')
            else:
                row.append(' ')
        triangle.append(row)
    return triangle

def veCayThongNoel(n):
    tree = []
    for i in range(n):
        row = []
        for j in range(n):
            if j <= i:
                row.append('*')
            else:
                row.append(' ')
        tree.append(row)
    return tree

while True:
    menu()
    choice = int(input('Mời bạn chọn chức năng: '))
    if choice == 1:
        n = int(input('Nhập cạnh hình vuông: '))
        kyHieu = input('Nhập ký hiệu vẽ: ')
        ketqua = veHinhVuong(n, kyHieu)
        data = get_data(ketqua)
        print(data)
        save_file(data)
    elif choice == 2:
        dai = int(input('Nhập chiều dài hình chữ nhật: '))
        rong = int(input('Nhập chiều rộng hình chữ nhật: '))
        ketqua = veHinhChuNhat(dai, rong)
        data = get_data(ketqua)
        print(data)
        save_file(data)
    elif choice == 3:
        n = int(input('Nhập chiều cao của tam giác vuông cân: '))
        ketqua = veHinhTamGiac(n)
        data = get_data(ketqua)
        print(data)
        save_file(data)
    elif choice == 4:
        n = int(input('Nhập chiều cao của cây thông Noel: '))
        ketqua = veCayThongNoel(n)
        data = get_data(ketqua)
        print(data)
        save_file(data)
    elif choice == 5:
        print('Cảm ơn bạn đã sử dụng chương trình!')
        break
    else:
        print('Chức năng không tồn tại! Mời bạn chọn lại.')