def fibonacci(n):
    if n == 0:
        return 0
    if (0 < n <= 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(9))

#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

def giaiThua(n):
    #n! = n * (n - 1)!
    #n! = n * (n-1)!
    if n == 0:
        return 1
    return n * giaiThua(n - 1)

