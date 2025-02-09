def count_word(filename):
    #tạo dictionary để lưu các từ và số lần xuất hiện
    dict = {}
    # f = open(filename, 'r', encoding='utf-8')
    # text = f.read()     #đọc toàn bộ nội dung của file
    # f.close()
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
    except TypeError:
        print("Kiểu dữ liệu không phù hợp")
        return None
    except FileNotFoundError:
        print("File không tồn tại")
        return None

    words = text.split()    #tách nội dung thành các từ
    for word in words:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

def dem_dong(ten_tap_tin): 
    with open(ten_tap_tin, 'r') as file: 
        cac_dong = file.readlines() 
    return len(cac_dong)
def dem_ky_tu(ten_tap_tin):
    pass

def count_line_char(filename):
    dong = dem_dong(filename)
    ky_tu = dem_ky_tu(filename)
    return (dong, ky_tu)

def search_keyword(ten_tap_tin, tu_khoa): 
    with open(ten_tap_tin, 'r', encoding='utf-8') as file: 
        van_ban = file.read() 
    return tu_khoa in van_ban

#hàm menu
def menu():
    print('======   Menu   ======')
    print('1. Đếm số lần xuất hiện của từng từ')
    print('2. Đếm số dòng và số ký tự')
    print('3. Tìm kiếm từ khóa')
    print('4. Thoát')
    print('======================')

#vòng lặp while
while True:
    menu()
    choice = input("Chọn chức năng: ")
    if choice == "1":
        tenFile = input("Nhập tên file: ")
        ketqua = count_word(tenFile)
        for key, value in ketqua.items():
            print(f"Từ '{key}' xuất hiện {value} lần")
    elif choice == "2":
        count_line_char()
    elif choice == "3":
        tenFile = input("Nhập tên file: ")
        tuKhoa = input("Nhập từ khóa cần tìm: ")
        if search_keyword(tenFile, tuKhoa):
            print(f'{tuKhoa} có xuất hiện trong file {tenFile}')
    elif choice == "4":
        print("Chương trình đã kết thúc")
        break
    else:
        print("Chức năng không tồn tại, vui lòng chọn lại!")