#open file
f = open('cuoikhoa.txt', 'r', encoding='utf-8')
#đọc dữ liệu lưu vào dictionary
books = {}
for line in f:
    tensach = line.strip().split(':')
    soluong = int(tensach[1])
    books[tensach[0]] = soluong
f.close()

#sắp xếp lại dictionary theo tên sách
bookList = list(books.items())

for i in range(1, len(bookList)):
    tensach = bookList[i][0]
    soluong = bookList[i][1]
    j = i - 1
    while j >= 0 and bookList[j][0] > tensach:
        bookList[j + 1] = bookList[j]
        j -= 1
    bookList[j + 1] = (tensach, soluong)
sortedBooks = dict(bookList)
#tìm kiếm sách theo tên trong dictionary
def binary_search_book(dict, bookname):
    low = 0
    high = len(dict) - 1
    while low <= high:
        mid = (low + high) // 2
        if list(dict.keys())[mid] == bookname:
            return list(dict.values())[mid]
        elif list(dict.keys())[mid] < bookname:
            low = mid + 1
        else:
            high = mid - 1
    return None

bookname = input('Nhập tên sách cần tìm: ')
soluong = binary_search_book(sortedBooks, bookname)
if soluong == None:
    print('Không tìm thấy sách')
else:
    print(f'Số lượng sách {bookname} còn lại là: {soluong}')