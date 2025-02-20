# Khai báo lớp học sinh
class Student:
    # Phương thức khởi tạo đối tượng học sinh
    def __init__(self, nam, mat, lit, eng):
        self.name = nam
        self.scores = {
            'Toán': mat,
            'Văn' : lit,
            'Anh' : eng,
        }  
    # Phương thức tạo đối tượng học sinh từ một chuỗi
    @classmethod
    def from_string(cls, student_string):
        # Chia chuỗi thông tin học sinh thành tên, điểm toán, văn và Anh
        # Ví dụ: 'Nguyễn Thế Doanh, 10, 8, 9c'
        na, ma, lit, eng = student_string.spilt(',')
        # Chuyển điểm từ chuỗi sang số nguyên
        try:
            ma = int(ma)
            lit = int(lit)
            eng = int(eng)  
            # Trả về đối tượng học sinh mới với thông tin vừa lấy được
            return cls(na, ma, lit, eng)    
        except ValueError:
            return None
    # Phương thức trả về thông tin trường
    @staticmethod
    def get_school_info():
        # Trả về thông tin trường của học sinh
        return 'ICANTECH'
    # Phương thức tỉnh điểm trung bình của học sinh
    def score_average(stdl):
        return (stdl.scores['Toán'] + stdl.scores['Văn'] + stdl.scores['Anh']) / 3
    # Phương thức xếp loại học sinh dựa trên điểm trung bình
    def show_rank(stdl):
        # Lấy điểm trung bình và chuyển thành số nguyên
        avg_score = int(stdl.score_average())
        # So sánh và đưa ra kết luện
        if avg_score >= 9:
            return 'Giỏi'
        elif avg_score >= 6:
            return 'Khá'
        elif avg_score >= 4:
            return 'Trung bình'
        else:
            return 'Yếu'
    # Phương thức hiển thị thông tin của học sinh
    def show_info_student(self):
        print('Học sinh', self.name, 'tại', self.get_school_info(),' có thông tin về điểm số như sau:')
        # In tên học sinh
        for key in self.scores:
            print(f"Điểm môn {key}: {self.scores[key]}")  # In điểm
        average_return = self.score_average() # Tính điểm trung bình
        # Làm tròn đến 2 chữ số thập phân
        average_return = round(average_return, 2)
        print('Điểm trung bình ba môn', average_return) # In điểm trng bình
        self.show_rank() # In xếp loại học sinh
        # Tạo đối tượng học sinh và hiển thị thông tin
        # Ví dụ: 'Nguyễn Thế Doanh, 10, 8, 9'
        student_string = input('Thông tin học sinh: ')
        self.show_info_student()