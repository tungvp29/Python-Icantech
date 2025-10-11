class Student:
    name = ''
    scores = {}                 #{'Văn': 0, 'Toán': 0, 'Anh': 0}
    school = ''
    age = None
    def scoreAvarage(std1):
        sum(std1.scores.values())  # Tính tổng điểm các môn
        # return (std1.scores['Văn'] + std1.scores['Toán'] + std1.scores['Anh']) / 3
        return sum(std1.scores.values()) / len(std1.scores)  # Tính điểm trung bình
    def showRank(std1):
        avgScore = std1.scoreAvarage()
        if avgScore >= 9:
            return 'Giỏi'
        elif avgScore >= 6:
            return 'Khá'
        elif avgScore >= 4:
            return 'Trung bình'
        else:
            return 'Yếu'
    
    def showInfoStudent(std1):
        print('Tên học sinh: ', std1.name)
        for key in std1.scores:
            print(f'Điểm môn {key}: {std1.scores[key]}')
        avgScore = std1.scoreAvarage()
        avgRound = round(avgScore, 2)
        print(f'Điểm trung bình: {avgRound}')
        print('Xếp loại: ', std1.showRank())
        print('--------------------------')

std1 = Student()
std1.name = 'Nguyên Lâm'
std1.scores = {'Văn': 8, 'Toán': 7, 'Anh': 9}
std1.showInfoStudent()

std2 = Student()
std2.name = 'Bình Minh'
std2.scores = {'Văn': 5, 'Toán': 6, 'Anh': 4}
std2.showInfoStudent()

std3 = Student()
std3.name = 'Xuân Huy'
std3.scores = {'Văn': 10, 'Toán': 9, 'Anh': 8}
std3.showInfoStudent()
