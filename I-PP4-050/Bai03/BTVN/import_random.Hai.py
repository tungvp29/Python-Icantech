import random
class game:
    def __init__(self,type):
        self.scorelist=[]
        self.type=type
    @property
    def score(self):
        if self.type=="đồng xu":
            return random.randint(0,1)
        elif self.type=="xúc xắc":
            return random.randint(1,6)
    @property
    def quantity(self):
        return len(self.scorelist)
    @quantity.setter
    def quantity(self,newquantity):
        for y in range(newquantity):
            self.scorelist.append(self.score)
    @quantity.deleter
    def quantity(self):
        self.scorelist=[] 
    @property
    def totalscore(self):
        return sum(self.scorelist)
    def play(self,quantity):
        del self.quantity
        self.quantity=quantity  
        print(self.quantity,self.type,self.scorelist,self.totalscore)
if __name__ == "__main__":
    g1 = game("xúc xắc")
    g1.play(15)

    g2 = game("đồng xu")
    g2.play(2)
     