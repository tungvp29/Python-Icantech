class Student:
    def __init__(self, nam, mat, lit, eng):
        self.name = nam
        self.scores = {
            'Toán': mat,
            'Văn': lit,
            'Anh': eng,
        }
    @classmethod
    def from_string(cls, student_string):
        nam, mat, lit, eng = student_string.split(',')
        mat = int(mat)
        lit = int(lit)
        eng = int(eng)
        return cls(nam, mat, lit, eng)
    @staticmethod
    def get_school_info():
        return 'ICANTECH'
    def score_avarage(self):
        return (self.scores['Toán']+self.scores['Văn']+self.scores['Anh'])/3
    def show_rank(self):
        avg_score = int(self.score_avarage())
        if avg_score >= 9:
            return 'Giỏi'
        elif avg_score >= 6:
            return 'Khá'
        elif avg_score >= 4:
            return 'Yếu'
        else:
            return 'Ngu'
    def show_info_student(self):
        print('Họ tên hs: ', self.name, 'tại ', self.get_school_info(), 'có điểm như sau: ')
        for key in self.scores:
            print(f'Điểm môn {key}; {self.scores[key]}')
        average_return= (self.score_avarage())
        average_return= round(average_return, 2)
        print('Điểm trung bình 3 môn: ', average_return)
        self.show_rank()
student_string = input('Thông tin: ')
std1 = Student.from_string(student_string)
std1.show_info_student()

std2 = Student('Nguyen Van A', 8, 7, 9)
std2.show_info_student()