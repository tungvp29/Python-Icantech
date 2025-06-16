class Student:
    siSo = 0
    def __init__(self, name = '', toan = 0, ly = 0, hoa = 0):
        self.name = name
        self.toan = int(toan)
        self.ly = int(ly)
        self.hoa = int(hoa)
        Student.siSo += 1

    @classmethod
    def from_string(cls, input_string):
        na, to, ly, ho = input_string.split(',')
        return cls(name = na, toan = to, ly = ly, hoa = ho)
    
    @staticmethod
    def getSchoolInfo():
        return 'Trường THPT Chuyên Lê Quý Đôn - Đà Nẵng'
    
    def scoreAvarage(self):        
        # return (self.scores['Văn'] + self.scores['Toán'] + self.scores['Anh']) / 3
        return (self.toan + self.ly + self.hoa) / 3  # Tính điểm trung bình
    
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
    @property
    def showInfoStudent(self):
        print('Tên học sinh: ', self.name)
        
        print(f'Điểm môn Toán: {self.toan}')
        print(f'Điểm môn Lý: {self.ly}')
        print(f'Điểm môn Hóa: {self.hoa}')
        avgScore = self.scoreAvarage()
        avgRound = round(avgScore, 2)
        print(f'Điểm trung bình: {avgRound}')
        print('Xếp loại: ', self.showRank())
        print(self.getSchoolInfo())
        print('--------------------------')

print(f"Số lượng học sinh đã tạo: {Student.siSo}")

stu1 = Student.from_string('Nguyen Van A,8,7,9')
stu1.showInfoStudent()

stu2 = Student('Tran Thi B', 6, 8, 7)
stu2.showInfoStudent()

stu3 = Student()
stu3.name = 'Le Van C'
stu3.toan = 5
stu3.ly = 6
stu3.hoa = 4
stu3.showInfoStudent()

print(f"Số lượng học sinh đã tạo: {Student.siSo}")