import random

class Game:
    def __init__(self,type='xuc xac'):
        self.type = type
        self.score_list = []
    
    @property
    def score(self):
        if(self.type == 'dong xu'):
            return random.randint(0,1)
        elif(self.type == 'xuc xac'):
          return random.randint(1,6)
    
    @property
    def quantity(self):
        return len(self.score_list)
    
    @quantity.setter
    def quantity(self,new_quantity):
        for _ in range(new_quantity):
            self.score_list.append(self.score)

    @quantity.deleter
    def quantity(self):
        self.score_list = []

    def total_score(self):
        return sum(self.score_list)
    
    def play(self,quantity=0):
        del self.quantity
        self.quantity = quantity
        print(f"diem {self.quantity} lan gieo {self.type}: {self.score_list}\n Tong diem {self.type}: {self.total_score()}")

game1 = Game(type='dong xu')
game1.play(quantity=5)
game2 = Game(type='xuc xac')
game2.play(quantity = 3)
    