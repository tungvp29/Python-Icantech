class Game:
    tien=5000
    so_luong=0
    def __init__(self,ten):
        self.ten=ten
        self.nuoc=0
        self.anh_sang=0
        Game.so_luong+=1
        Game.tien-=200
    @ property
    def tinh_trang(self):
        if(self.nuoc==None and self.anh_sang== None ):
            return "selled"
        elif(self.nuoc==0 and self.anh_sang==0 ):
            return "seed"
        elif(self.nuoc>0 and self.anh_sang>0 ):
            return "alive"
        else:
            return "dead"

    @ property
    def price(self): 
        if(self.nuoc==None and self.anh_sang== None ):
            return 0
        return max(0,self.nuoc +self.anh_sang*10)
    @ price.setter
    def price(self,value):
        (more_nuoc,more_anh_sang)=value
        if (more_nuoc>100 or more_anh_sang>10 ):
            self.nuoc=-1
            self.anh_sang =-1
        elif self.check_tinh_trang():
            self.nuoc+= more_nuoc
            self.anh_sang+= more_anh_sang
    @ price.deleter
    def price(self):
        Game.tien+=self.price
        self.nuoc=None
        self.anh_sang =None
    @staticmethod
    def cham_cay():
        ten=input("Input the name for your plant:")
        for i in range(Game.so_luong):
            if game[i].ten==ten and game[i].check_tinh_trang():
                more_nuoc=int(input("Input the amount of water you want to add:"))
                more_anh_sang=int(input("Input the time of sunlight you want to let your plant have:"))
                if game[i].nuoc is not None and game[i].anh_sang is not None:
                    game[i].price = (more_nuoc , more_anh_sang)
                    print (game[i])
                    return True 
                else:
                    print("The plant was selled or not existed.")
                    return False
        print("The plant was not existed or already dead.")
        return False
    @staticmethod
    def ban_cay():
        ten=input("Name the sell plant:")
        for i in range(Game.so_luong):
            if game[i].ten==ten and game[i].check_tinh_trang():
                del game[i].price
                break
        else:
            print("========Pls type again the name========")
            return False
        return True
    def check_tinh_trang(self):
        if self.tinh_trang=='alive' or'seed':
            return True
        else:
            return False
    def get_info(self):
        return f"Cây{self.ten} có tình trạng là{self.tinh_trang},chieu cao la:{self.price}mm "
game=[]
while True:
        print("Choose one of these action")
        print("1.Add new plant")
        print("2.Care for the plant")
        print("3.Sell the plant")
        print("4.See the lists of the plants")
        print("5.Leave the shop")
        print(f"You are having${Game.tien}")
        choice=input("Choose one of these action (1-5):")
        if choice=="1":
            name=input("Pls name your plant: ")
            game.append(Game(ten=name))
            print(f"You have name the plant{name}")
        elif choice=="2":
            Game.cham_cay()
        elif choice=="3":
            Game.ban_cay()
        elif choice=="4":
            for i in range(Game.so_luong):
                print(f"{i+1}.{game[i].get_info()}")
        elif choice=="5":
            break
        else:
            print("Your option is invalid ")
        

