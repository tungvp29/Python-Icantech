import random

class HocSinh:
    soluong=0
    def __init__(self, ten):
        self.ten = ten
        HocSinh.soluong += 1

    @classmethod
    def soLuongHs(cls):
        return cls.soluong
    
hs1 = HocSinh("Nguyen Van A")
hs2 = HocSinh("Tran Thi B")
hs3 = HocSinh("Le Van C")
print(hs1.soluong)
print(hs2.soluong)
print(hs3.soluong)

print(f"Số lượng học sinh đã tạo: {HocSinh.soLuongHs()}")  # Số lượng học sinh đã tạo: 2