class Dog:          #class = lớp
    leg = 4                               #attribute = thuộc tính
    breed = 'puddle'
    toc_do = 20
    
    def sua(self):                        #method = phương thức
        if self.breed == 'puddle':
            print('Gâu gâu')
        if self.breed == 'corgi':
            print('Gâu gâu gâu')
    def chay():
        pass
    def nam():
        pass

dog1 = Dog()        #object = đối tượng
dog2 = Dog()
dog2.breed = 'corgi'

print(f'dog1: {dog1.leg} chân, giống {dog1.breed}')
dog1.sua()

print(f'dog2: {dog2.leg} chân, giống {dog2.breed}')
dog2.sua()

class Car:
    sobanh = 0
    mau = ''
    toc_do = 0
    loaixe = ''

    def khoidong(self):
        self.toc_do = 10

    def phanh(self):
        self.toc_do = 0
        
    def mo_cua():
        pass
    def re_trai():
        pass
    def re_phai():
        pass
    def di_lui():
        pass