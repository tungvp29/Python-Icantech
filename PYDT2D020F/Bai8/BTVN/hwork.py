def bubble_sort(lst, value_index=1):    #sắp xếp nổi bọt
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j][value_index] < lst[j + 1][value_index]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def insertion_sort(lst, value_index=1):    #sắp xếp chèn
    for i in range(1, len(lst)):
        x = lst[i]
        pos = i - 1
        while pos >= 0 and x[value_index] > lst[pos][value_index]:
            lst[pos + 1] = lst[pos]
            pos -= 1
        lst[pos + 1] = x
    return lst

def in_danh_sach(lst):
    for i in range(len(lst)):
        print(f'{i+1}. {lst[i][0]}: {lst[i][1]}')

n = int(input('nhập số người:'))
arr = []
for i in range(n):
    player_name = input(f'nhập tên người thứ {i+1}:')
    player_score = int(input(f'nhập điểm người thứ {i+1}:'))
    arr.append((player_name, player_score))

# thứ hạng chưa sắp xếp:
print('Bảng xếp hạng ban đầu:')
in_danh_sach(arr)

# sắp xếp theo điểm giảm dần:
arr_sort = arr.copy()
# bubble_sort(arr_sort)
insertion_sort(arr_sort, 0)
print('Bảng xếp hạng sau khi sắp xếp:')
in_danh_sach(arr_sort)