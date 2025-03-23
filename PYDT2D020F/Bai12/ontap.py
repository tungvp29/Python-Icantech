# import os

# f = open('test.txt', 'r')
# print(f.read())
# f.close()

# # f = open('test.txt', 'w')
# # f.write('Hello, world!')
# # f.close()

# f = open('test.txt', 'a')
# f.write('Hello, world!')
# f.close()

lst = [1, 2, 3, 4, 5]
lst1 = ['a', 'b', 'c', 'd', 'e']
lst.append(6) # lst = [1, 2, 3, 4, 5, 6]
# lst + lst1 = [1, 2, 3, 4, 5, 'a', 'b', 'c', 'd', 'e']

lst2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]           # list 2 chieu

print(lst2[1][2]) # 6

tpl = (1, 2, 3, 4, 5)
print(tpl[1]) # 2

dct = {
    'name': 'Huy',
    'age': 18,
    'address': 'Hanoi'
}
print(dct['name']) # Huy


s = {1, 2, 3, 4, 5}
print(s[2]) # error

try:
    n = int(input('Nhập số phần tử: '))          #a
    print(n)
except:
    print('Lỗi')

#