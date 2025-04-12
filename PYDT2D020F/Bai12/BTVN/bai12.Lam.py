f = open("cuoikhoa.txt", "r", encoding='utf-8')
books = {}
for line in f:
    book_name = line.strip().split(":")
    quantity = int(book_name[1])
    books[book_name[0]] = quantity
f.close()
book_list = list(books.items())
for i in range(1, len(book_list)):
    key = book_list[i][0]
    value = book_list[i][1]
    j = i - 1
    while j >= 0 and book_list[j][0]:
        book_list[j+1] = book_list[j]
        j -= 1
    book_list[j+1] = (key, value)
sorted_books = dict(book_list)
def binary_search_book(dictionary, book_name):
    low = 0
    high = len(dictionary) - 1
    while low <= high:
        mid = (low + high) // 2
        if list(dictionary.keys())[mid] < book_name:
            low = mid + 1
        elif list(dictionary.keys())[mid] > book_name:
            high = mid - 1
        else:
            return list(dictionary.values())[mid]
    return None
book_name = input('Nhap ten sach:')
quantity = binary_search_book(sorted_books, book_name)
if quantity is not None:
    print(f"so luong sach '{book_name}' trong thu vien la {quantity}")
else:(f"khong tim thay '{book_name}' trong thu vien")
