class Dog:
    leg = 4
    breed = ''

    def show(self):
        print(f'Chó giống {self.breed} có {self.leg} chân')

class Cat:
    leg = 4
    breed = ''

    def hienthi(self):
        print(f'Mèo giống {self.breed} có {self.leg} chân')

cho1 = Dog()
cho1.breed = 'Phú Quốc'
chan = cho1.leg
cho1.show()
# print(f'Chó {cho1.breed} có {chan} chân')

cho2 = Cat()
cho2.breed = 'Abyssinian'
cho2.leg = 3
cho2.hienthi()
# print(f'Chó {cho2.breed} có {cho2.leg} chân')

