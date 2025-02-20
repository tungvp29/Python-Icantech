class HinhTron:
    def __init__(self, r = 0):      #khoi tao
        self.r = r
        self.pi = 3.14

    @property       # getter
    def tinh_dien_tich(self):
        return self.r ** 2 * self.pi 
    
    @tinh_dien_tich.setter      # setter
    def tinh_dien_tich(self, dien_tich_moi):
        self.r = (dien_tich_moi / self.pi) ** 0.5
    
    @tinh_dien_tich.deleter     # deleter
    def tinh_dien_tich(self):
        self.r = None

ht1 = HinhTron(5)
# print(ht1.tinh_dien_tich) # getter

# ht1.tinh_dien_tich = 100 # setter
# print(ht1.r) # 5.64         #getter

del ht1.tinh_dien_tich # deleter    
print(ht1.tinh_dien_tich)

