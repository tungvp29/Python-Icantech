import random

def sequential_search(arr, x):
    step = 0
    for i in range(len(arr)):
        step += 1   
        if arr[i] == x:
            return i, step
    return None, step

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    step = 0

    while low <= high:
        step += 1
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid, step
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None, step

# n = int(input("Nhập số phần tử: "))
arr = [5,4,3,2,1]
# for i in range(n):
#     arr.append(random.randint(0, 10000))

# arr.sort()

# print(f'Danh sách {n} phần tử ngẫu nhiên ban đầu: \n{arr}')
target = int(input("Nhập số cần tìm: "))

# vitri, sobuoc = sequential_search(arr, target)
vitri2, sobuoc2 = binary_search(arr, target)

# print(f'Với thuật toán tuần tự, vị trí của phần tử {target} trong mảng là {vitri} sau {sobuoc} bước')
print(f'Với thuật toán tìm kiếm nhị phân, vị trí của phần tử {target} trong mảng là {vitri2} sau {sobuoc2} bước')