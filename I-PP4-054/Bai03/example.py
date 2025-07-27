import math

class HinhTron:
    name = ''
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
        self.pi = 3.14

    @property                       #getter
    def dien_tich(self):
        print('đang tính diện tích...')
        print('đang tính diện tích...')
        print('đang tính diện tích...')
        print('đang tính diện tích...')
        return self.ban_kinh * 2
    
    @dien_tich.setter              #setter
    def dien_tich(self, dienTichMoi):
        print('đang tính diện tích...')
        self.ban_kinh = math.sqrt(dienTichMoi / math.pi)
    
    @dien_tich.deleter              #deleter
    def dien_tich(self):
        self.ban_kinh = 10

hinh1 = HinhTron(5)
print('ban kinh: ', hinh1.ban_kinh)
hinh1.ban_kinh = 10
print('dien tich: ', hinh1.dien_tich)   #getter được kích hoạt
hinh1.dien_tich = 100                   #setter được kích hoạt
print('ban kinh: ', hinh1.ban_kinh)  
del hinh1.dien_tich                  #deleter được kích hoạt
print('ban kinh: ', hinh1.ban_kinh)  