class Game:
    tien = 5000
    soluong = 0

    def __init__(self, ten):
        #thêm cây mới
        self.ten = ten
        self.nuoc = 0
        self.anh_sang = 0
        Game.tien -= 200
        Game.soluong += 1

    @property
    def tinh_trang(self):
        if (self.nuoc == None and self.anh_sang == None):
            return 'đã bán'
        elif (self.nuoc == 0 and self.anh_sang == 0):
            return 'hạt mầm'
        elif (self.nuoc > 0 and self.anh_sang > 0):
            return 'sống'
        else:
            return 'chết'

    @property
    def gia_thanh(self):
        if (self.nuoc == None and self.anh_sang == None):
            return 0
        return max(0, self.nuoc + self.anh_sang * 10)
        
    @gia_thanh.setter
    def gia_thanh(self, value):     #value = nuoc_tang_them, anh_sang_tang_them
        nuoc_tang_them, anh_sang_tang_them = value
        if (nuoc_tang_them > 100 or anh_sang_tang_them > 10):
            self.nuoc = -1
            self.anh_sang = -1
        elif self.check_tinh_trang():
            self.nuoc += nuoc_tang_them
            self.anh_sang += anh_sang_tang_them

    @gia_thanh.deleter
    def gia_thanh(self):
        Game.tien += self.gia_thanh
        self.nuoc = None
        self.anh_sang = None

    @staticmethod
    def cham_cay():
        ten = input('Nhập tên cây: ')
        for cay in games:
            if cay.ten == ten and cay.check_tinh_trang():
                nuoc_tang_them = int(input('Bạn muốn tưới bao nhiêu ml nước: '))
                anh_sang_tang_them = int(input('Bạn sẽ để cây ngoài trời mấy tiếng: '))
                if cay.nuoc is not None and cay.anh_sang is not None:
                    cay.gia_thanh = (nuoc_tang_them, anh_sang_tang_them)                    
                    return True
                else:
                    print('Cây đã chết hoặc đã bán')
                    return False                        
        print('Không tìm thấy cây hoặc cây không còn sống. Hãy nhập lại tên.')
        return False

    @staticmethod
    def ban_cay():
        ten = input('Nhập tên cây: ')
        for cay in games:
            if cay.ten == ten and cay.check_tinh_trang():
                del cay.gia_thanh
                break
        else:
            print('------Nhập lại tên cây------')
            return False
        return True

    def check_tinh_trang(self):
        if self.tinh_trang == 'sống' or 'hạt mầm':
            return True
        return False

    def get_info(self):
        return f'Cây {self.ten} có tình trạng là {self.tinh_trang}, chiều cao là {self.gia_thanh}mm, giá bán là {self.gia_thanh}đ.'

games = []
while True:
    print('Chọn một trong các chức năng sau:')
    print('1. Thêm cây mới')
    print('2. Chăm sóc cây')
    print('3. Bán cây')
    print('4. Xem danh sách các cây')
    print('5. Thoát')
    print(f'Tiền hiện tại: {Game.tien} đồng')
    
    choice = input('Chọn: ')
    if choice == '1':
        print('-------------------THÊM CÂY MỚI-------------------')
        ten = input('Nhập tên cây: ')
        games.append(Game(ten))
        print(f'Thêm cây {ten} thành công')
        print('--------------------------------------------------')
    elif choice == '2':
        print('-------------------CHĂM SÓC CÂY-------------------')
        Game.cham_cay()
        print('--------------------------------------------------')
    elif choice == '3':
        print('-------------------BÁN CÂY-------------------')
        Game.ban_cay()
        print('--------------------------------------------------')
    elif choice == '4':
        print('-------------------DANH SÁCH CÂY-------------------')
        for cay in games:
            print(f'{games.index(cay) + 1}. {cay.get_info()}')
        print('---------------------------------------------------')
    elif choice == '5':
        break
    else:
        print('Lựa chọn không hợp lệ. Hãy chọn lại.')