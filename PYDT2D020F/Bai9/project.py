from sapxep import insertion_sort
from timkiem import binary_search
# from timkiem import *
# import timkiem

#from <tên file> import <tên hàm>
#from <tên file> import * (import tất cả các hàm trong file)

import random

n = int(input("Nhập số phần tử: "))
arr = []
for i in range(n):
    arr.append(random.randint(0, 1000))

insertion_sort(arr)
print(arr)
target = 5
vitri2, sobuoc2 = binary_search(arr, target)
print(f'Với thuật toán tìm kiếm nhị phân, vị trí của phần tử {target} trong mảng là {vitri2} sau {sobuoc2} bước')