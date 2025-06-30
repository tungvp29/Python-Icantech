class Game:
    tien=10000
    so_luong=0
    def __init__(self,ten):
        self.ten=ten
        self.nuoc=0
        self.anh_sang=0
        Game.so_luong += 1
        Game.tien-=200
    @property
    def tinh_trang(self):
        if(self.nuoc==None and self.anh_sang==None):
            return 'da ban'
        elif(self.nuoc==0 and self.anh_sang==0):
            return'hat_mam'
        elif(self.nuoc>0 and self.anh_sang>0):
            return'song'
        else:
            return'chet'

    @property
    def gia_thanh(self):
        if (self.nuoc ==None and self.anh_sang==None):
            return 0
        return max(0,self.nuoc + self.anh_sang*10)
    @gia_thanh.setter
    def gia_thanh(self, value):
        nuoc_tang_them, anh_sang_tang_them = value
        if (nuoc_tang_them > 100 or anh_sang_tang_them > 10):
            self.nuoc=-1
            self.anh_sang=-1
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
        ten = input("ten cay ban muon cham la: ")
        for i in range(Game.so_luong):
            if games[i].ten == ten and games[i].check_tinh_trang():
                nuoc_tang_them = int(input("ban muoc tuoi bao nhieu ml nuoc?"))
                anh_sang_tang_them=int
                input("ban se de cay ngoai troi may tieng?")
                if games[i].nuoc is not None and games[i].anh_sang is not None:
                    games[i].gia_thanh = (nuoc_tang_them, anh_sang_tang_them)
                    print(games[i])
                    return True
                else:
                    print("cay da ban hoac khong ton tai. Hay nhap lai ten.") 
                    return False
        print("cay khong ton tai hoac khong con song. Hay nhap lai ten.") 
        return False 
    @staticmethod
    def ban_cay():
        ten=input("cay ban ten la: ")
        for i in range(Game.so_luong):
            if games[i].ten==ten and games[i].check_tinh_trang():
                del games[i].gia_thanh
            break
        else:
            print("hay nhap lai ten")
            return False
        return True
    def check_tinh_trang(self):
        if self.tinh_trang=='song'or 'hat mam':
            return True
        return False
    def get_info(self):
        return f"cay{self.ten,}co tinh trang{self.check_tinh_trang()}, chieu cao la:{self.gia_thanh} mm"
games=[]
while True:
    print("Chon mot trong cac tuy chon sau:")
    print("1. them cay moi")
    print("2. cham soc cay")
    print("3.ban cay")
    print("4.xem danh sach cac cay")
    print("5.thoat chuong trinh")
    print(f"ban dang co{Game.tien} dong")
    choice = input("nhap lua chon cua ban(1-5)")
    if choice == "1":
        ten=input("ban muon dat ten cay la")
        games.append(Game(ten))
        print(f"ban da them cay {ten}thanh cong")
    elif choice == "2":
        Game.cham_cay()
    elif choice == "3":
        Game.ban_cay()
    elif choice == "4":
        for i in range(Game.so_luong):
            print(f"{i+1}.{games[i].get_info()}")
    elif choice == "5":
        break
    else:
        print("lua chon khong hop le. Hay chon lai.")       