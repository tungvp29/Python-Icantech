class Student:
    name = ''
    scores = {}                 #{'Văn': 0, 'Toán': 0, 'Anh': 0}

    def __init__(self, name, math, literature, english):
        self.name = name
        self.scores = {
            'Văn': math,
            'Toán': literature,
            'Anh': english
        }

    @classmethod
    def from_string(cls, student_string):
        name, math, literature, english = student_string.split(',')
        return cls(name, int(math), int(literature), int(english))
        # return Student(name, int(math), int(literature), int(english))

    @staticmethod
    def get_school_info():
        return "Trường học: Icantech Academy"

    def scoreAvarage(self):
        sum(self.scores.values())  # Tính tổng điểm các môn
        # return (std1.scores['Văn'] + std1.scores['Toán'] + std1.scores['Anh']) / 3
        return sum(self.scores.values()) / len(self.scores)  # Tính điểm trung bình
    def showRank(self):
        avgScore = self.scoreAvarage()
        if avgScore >= 9:
            return 'Giỏi'
        elif avgScore >= 6:
            return 'Khá'
        elif avgScore >= 4:
            return 'Trung bình'
        else:
            return 'Yếu'
    
    def showInfoStudent(self):
        print('Tên học sinh: ', self.name, self.get_school_info())
        for key in self.scores:
            print(f'Điểm môn {key}: {self.scores[key]}')
        avgScore = self.scoreAvarage()
        avgRound = round(avgScore, 2)
        print(f'Điểm trung bình: {avgRound}')
        print('Xếp loại: ', self.showRank())
        print('--------------------------')

std1 = Student('Nguyên Lâm', 8, 7, 9)
# std1.name = 'Nguyên Lâm'
# std1.scores = {'Văn': 8, 'Toán': 7, 'Anh': 9}
std1.showInfoStudent()

# std2 = Student()
# std2.name = 'Bình Minh'
# std2.scores = {'Văn': 5, 'Toán': 6, 'Anh': 4}
# std2.showInfoStudent()

# std3 = Student()
# std3.name = 'Xuân Huy'
# std3.scores = {'Văn': 10, 'Toán': 9, 'Anh': 8}
# std3.showInfoStudent()

input_data = input('Nhập thông tin học sinh (Tên, Điểm Văn, Điểm Toán, Điểm Anh): ')
std1 = Student.from_string(input_data)
std1.showInfoStudent()
