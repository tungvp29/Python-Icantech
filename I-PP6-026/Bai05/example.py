import pytest

#Các hàm tính toán
def add(a, b):
    #Cộng 2 số a và b
    return a + b

def divide(a, b):
    #Chia a cho b
    return a / b

def sum(a, b):
    #Cộng 2 số a và b
    return a + b

def subtract(a, b):
    #Trừ b từ a
    return a - b

def average(a, b):
    #Tính trung bình cộng của 2 số
    return sum(a, b) / 2
#--------------------

#Test cases
def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_average():
    assert average(2, 4) == 3

def test_divide():
    assert divide(6, 2) == 3

def test_sum():
    assert sum(2, 3) == 5
#--------------------

if __name__ == "__main__":
    test_add()
    test_subtract()
    test_average()
    test_divide()
    test_sum()
    print("All tests passed.")