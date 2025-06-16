class HinhTron:
    def __init__(self, ban_kinh):
        self.ban_kinh = ban_kinh
        self.pi = 3.14
    
    @property                           #getter
    def dien_tich(self):
        if self.ban_kinh is not None:
            return self.pi * self.ban_kinh ** 2
        else:
            return "Bán kính chưa được khởi tạo."
    
    @dien_tich.setter                    #setter
    def dien_tich(self, dien_tich_moi):
        self.ban_kinh = (dien_tich_moi / self.pi) ** 0.5
    
    @dien_tich.deleter                   #deleter
    def dien_tich(self):
        print("Đang xóa diện tích...")
        self.ban_kinh = None  # Xóa bán kính khi xóa diện tích

hinhtron1 = HinhTron(ban_kinh = 3)
print(f"Bán kính hình tròn 1: {hinhtron1.ban_kinh}")
hinhtron1.ban_kinh = 5  # Thay đổi bán kính
print(f"Bán kính hình tròn 1 sau khi thay đổi: {hinhtron1.ban_kinh}")
print(f"Dien tich hinh tron 1: {hinhtron1.dien_tich}")
hinhtron1.dien_tich = 10  # Thay đổi diện tích
print(f"Dien tich hinh tron 1 sau khi thay đổi: {hinhtron1.dien_tich}")
print(f"Bán kính hình tròn 1 sau khi thay đổi diện tích: {hinhtron1.ban_kinh}")

del hinhtron1.dien_tich
print(hinhtron1.dien_tich)
hinhtron1.ban_kinh = 4  
print('Dien tich:', hinhtron1.dien_tich)
