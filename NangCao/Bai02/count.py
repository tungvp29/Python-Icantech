n = int(input())
A = list(map(int, input().split()))

# count = [0] * len(set(A))
print( set(A))
count = {element: 0 for element in set(A)}

for x in A:
    count[x] += 1

for key, value in count.items():
    if value > 0:
        print(key, value)