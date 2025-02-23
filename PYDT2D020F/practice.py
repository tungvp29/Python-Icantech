import random, time

def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]

def insertion_sort(lst):    #sắp xếp chèn
    for i in range(1, len(lst)):
        x = lst[i]
        pos = i - 1
        while pos >= 0 and x < lst[pos]:
            lst[pos + 1] = lst[pos]
            pos -= 1
        lst[pos + 1] = x

lst1 = []
n = int(input("Nhập số phần tử: "))
for i in range(n):
    lst1.append(random.randint(0, 1000))

bubble_arr = lst1.copy()
start_time = time.time()
bubble_sort(bubble_arr)
end_time = time.time()
print(f"Thời gian sắp xếp bằng Bubble Sort: {end_time - start_time}")

insertion_arr = lst1.copy()
start_time = time.time()
insertion_sort(insertion_arr)
end_time = time.time()
print(f"Thời gian sắp xếp bằng Insertion Sort: {end_time - start_time}")

srt_arr = lst1.copy()
start_time = time.time()
srt_arr.sort()
end_time = time.time()
print(f"Thời gian sắp xếp bằng hàm sort: {end_time - start_time}")