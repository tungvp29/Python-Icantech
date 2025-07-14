class Car():
    # Thuộc tính
    loai_xe = ''
    ghe = 0

    #Phương thức
    def khoi_dong(self):
        print(f'Khởi động xe {self.loai_xe}!')
    def phanh(self):
        print('Phanh xe')
        print('--'*10)

#Đối tượng khởi tạo từ class Car
xe1 = Car()
xe1.loai_xe = 'Honda'
xe1.ghe = 5
print(f'Loại xe: {xe1.loai_xe}' )
print(f'Số ghế: {xe1.ghe}' )
xe1.khoi_dong()
xe1.phanh()

xe2 = Car()
xe2.loai_xe = 'Toyota'
xe2.ghe = 7
print(f'Loại xe: {xe2.loai_xe}' )
print(f'Số ghế: {xe2.ghe}' )
xe2.khoi_dong()
xe2.phanh()

xe3 = Car()
xe3.kieu_xe = 'Mazda'
xe3.so_ghe = 4
print(f'Loại xe: {xe3.kieu_xe}' )
print(f'Số ghế: {xe3.so_ghe}' )
xe3.khoi_dong()



class Student():
    # Thuộc tính
    ten = ''
    diem = 0.0

    # Phương thức
    def DanhSachDiem():
        pass
    def DiemTrungBinh(self):
        pass
    def XepLoai(self):
        pass
    def HienThiThongTin(self):
        pass