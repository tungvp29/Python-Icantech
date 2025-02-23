import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

n = int(input("Nhap so luong phan tu can sap xep:"))

arr = []
for i in range(n):
    arr.append(random.randint(1, 999))
print(f"Danh sach {n} phan tu ngau nhien ban dau: \n{arr}")

arr_bubble_sort = arr.copy()
start_time = time.time()
bubble_sort(arr_bubble_sort)
end_time = time.time()
print(f"Thoi gian sap xep bang Bubble sort: {end_time - start_time:9f}giay")

arr_insertion_sort = arr.copy()
start_time = time.time()
insertion_sort(arr_insertion_sort)
end_time = time.time()
print(f"Thoi gian sap xep bang Insertion sort: {end_time - start_time:9f}giay")
