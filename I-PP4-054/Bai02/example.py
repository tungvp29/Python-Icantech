class Dog:
    leg = 4
    sound = 'Gâu gâu'
    soluong = 0
    # breed = ''
    # fur = ''
    # face = ''

    def __init__(self, br = '', fu = '', fa = ''):
        self.breed = br
        self.fur = fu
        self.face = fa
        Dog.soluong += 1

    def doiThongTin(self):
        self.sound = 'Meo meo'

    @classmethod
    def soLuongCho(cls):
        # return cls.soluong 
        print(f'Số lượng chó hiện tại: {cls.soluong}')

    def show(self):
        print(f'Chó giống {self.breed} có {self.leg} chân')
        print(f'Chó có bộ lông {self.fur} và khuôn mặt {self.face}')
        print(f'Chó phát ra tiếng {self.sound}')
        print('--------------------------')

    @staticmethod
    def showSound():
        print(f'Chó phát ra tiếng Gâu gâu')

cho1 = Dog('Pitbull', 'ngắn', 'tròn')
cho1.doiThongTin()
cho1.show()

cho2 = Dog('Phú Quốc', 'dài', 'dễ thương')
cho2.show()

cho3 = Dog('Chihuahua', 'mềm', 'dễ thương')

cho4 = Dog('Corgi, mem, tròn')

Dog.soLuongCho()

print('cho1.soluong:', cho1.soluong)
print('cho2.soluong:', cho2.soluong)