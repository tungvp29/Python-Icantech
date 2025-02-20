class Student:
    name = ''
    scores = {}

    def score_average(self):  # Corrected: self as parameter
        if not self.scores: #check if scores is empty
            return 0
        diemtrungbinh = sum(self.scores.values()) / len(self.scores)
        return diemtrungbinh

    def show_rank(self):  # Corrected: self as parameter
        avg_score = self.score_average() # Use the method, not the class
        if avg_score >= 9:
            return 'Xuất sắc'
        if avg_score >= 8:
            return 'Giỏi'
        if avg_score >= 6:
            return 'Khá' # Changed to "Khá" for better classification
        if avg_score >= 5:
            return 'Trung bình'
        else:
            return 'Chưa Đạt'

    def show_info_student(self):  # Corrected: self as parameter
        print('Họ và tên học sinh:', self.name)
        for key in self.scores:
            print(f"Điểm môn {key}: {self.scores[key]}")
        average_return = self.score_average() # Use the method, not the class
        average_return = round(average_return, 2)
        print('Điểm trung bình ba môn:', average_return)
        print('Học sinh xếp loại', self.show_rank()) # Use the method, not the class


stdl = Student()
stdl.name = 'Hà Minh Hiếu'
stdl.scores = {'Toán': 10, 'Văn': 9, 'Anh': 8}
stdl.show_info_student()