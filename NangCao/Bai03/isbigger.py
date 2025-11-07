n = int(input())
numbers = [input().strip() for _ in range(n)]

# Hàm so sánh: trả về True nếu a nên đứng trước b
def is_bigger(a, b):
    return a + b > b + a

# Sắp xếp bubble sort (hoặc selection sort)
for i in range(n):
    for j in range(i+1, n):
        if not is_bigger(numbers[i], numbers[j]):
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(''.join(numbers))