class Student:
    name= ''
    score={}

    def score_average(self):
        return(self.score['Văn'] + self.score['Toán'] + self.score['Anh'])/3
    def show_rank(std):
        averageScore=std.score_average()
        if averageScore>= 9:
            return 'Giỏi'
        elif averageScore>= 6:
            return 'Khá'
        else:
            return 'Yếu'
    def showinfostudent(std):
        print('Tên học sinh: ', std.name )
        for key in std.score:
            print(f'Điểm môn {key}: {std.score[key]}')
        averagescore= std.score_average()
        averageround= round(averagescore,2)
        print(f'Điểm trung bình: {averageround}')
        print('Xếp loại: ', std.show_rank())

std1= Student()
std1.name= 'Gia Phát'
std1.score= {'Văn': 8, 'Toán': 10, 'Anh': 9}
std1.showinfostudent()