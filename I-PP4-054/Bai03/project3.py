import random

class Game:
    # Constructor - Ham khoi tao
    def __init__(self, type='xúc xắc'):
        self.type = type
        self.score_list = []

    #static method
    @staticmethod
    def get_game_info():
        return 'Chào mừng đến với trò chơi xúc xắc và đồng xu'

    @property               # getter
    def score(self):
        if (self.type == 'xúc xắc'):
            return random.randint(1, 6)
        elif (self.type == 'đồng xu'):
            return random.randint(0, 1)
        
    @property               # getter
    def quantity(self):
        return len(self.score_list)
    
    @quantity.setter        # setter
    def quantity(self, new_quantity):
        for i in range(new_quantity):
            self.score_list.append(self.score)

    @quantity.deleter       # deleter
    def quantity(self):
        self.score_list = []

    @property               # getter
    def total_score(self):
        return sum(self.score_list)
    
    #avarage score
    @property
    def average_score(self):
        return self.total_score / self.quantity

    #min score
    @property
    def min_score(self):
        return min(self.score_list)

    #max score
    @property
    def max_score(self):
        return max(self.score_list)

    def play(self, quantity = 0):
        del self.quantity
        self.quantity = quantity
        print(f"Kết quả {self.type} sau {quantity} lần chơi: {self.score_list}")
        print(f"Tổng điểm: {self.total_score}")
        print(f"Điểm trung bình: {self.average_score}")
        print(f"Điểm thấp nhất: {self.min_score}")
        print(f"Điểm cao nhất: {self.max_score}")

game1 = Game('xúc xắc')
game1.play(5)
game2 = Game('đồng xu')
game2.play(3)


# print(game1.quantity())        #lấy dữ liệu ra => getter
# game1.quantity = 5        #thay đổi dữ liệu => setter
# del game1.quantity        #xóa dữ liệu => deleter
