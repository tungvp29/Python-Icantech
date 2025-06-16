class Student:
    student_list = []  
    def __init__(self, name, math, literature, english):
        self.name = name
        self.math = float(math)
        self.literature = float(literature)
        self.english = float(english)
        Student.student_list.append(self)
    def average_score(self):
        return round((self.math + self.literature + self.english) / 3, 2)
    def display_info(self):
        print(f"Họ tên: {self.name}")
        print(f"Điểm: Toán = {self.math}, Văn = {self.literature}, Anh = {self.english}")
        print(f"Điểm trung bình: {self.average_score()}")
        print("------")
    @staticmethod
    def student_count():
        return len(Student.student_list)
    @classmethod
    def class_average(cls):
        if len(cls.student_list) == 0:
            return 0
        total = sum(student.average_score() for student in cls.student_list)
        return round(total / len(cls.student_list), 2)
std1 = Student(" A", 9.0, 7.0, 9.0)
std2 = Student(" B", 6.0, 7.0, 8.0)
std3 = Student(" C", 5.0, 6.0, 6.5)
print("=== Danh sách học sinh ===")
for student in Student.student_list:
    student.display_info()
print(f"Tổng số học sinh: {Student.student_count()}")
print(f"Điểm trung bình của cả lớp: {Student.class_average()}")
