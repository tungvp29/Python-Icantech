#tạo class
class Student:
    #thuộc tính
    name = ''
    group = ''
    scores = {}         #dictionary: {'toan': 10, 'ly': 9, 'hoa': 8, }

    #phương thức
    #tính điểm trung bình
    def tinhdiemtrungbinh(self):
        diemtrungbinh = sum(self.scores.values()) / len(self.scores)
        return round(diemtrungbinh, 2)
        # return round((self.scores['toan'] + self.scores['ly'] + self.scores['hoa']) / 3, 2)
    #tính xếp hạng
    def xephang(self):
        diemtrungbinh = self.tinhdiemtrungbinh()
        if diemtrungbinh >= 9:
            return 'Xuất sắc'
        elif diemtrungbinh >= 8:
            return 'Giỏi'
        elif diemtrungbinh >= 7:
            return 'Khá'
        elif diemtrungbinh >= 5:
            return 'Trung bình'
        else:
            return 'Yếu'

    def DiemCaoNhat(self):
        max_score = max(self.scores.values())
        return max_score
    
    def CacMonGioiNhat(self):
        max_score = self.DiemCaoNhat()
        for mon, diem in self.scores.items():
            if diem == max_score:
                print(mon, end=', ')
        print()

    #in thông tin
    def inthongtin(self):
        print('Thông tin sinh viên: ')
        print(f'Họ tên: {self.name}')
        print('Điểm:')
        for mon in self.scores:
            print(f'    {mon}: {self.scores[mon]}')
        # for mon, diem in self.scores.items():
        #     print(f'    {mon}: {diem}') 
        print(f'Điểm trung bình: {self.tinhdiemtrungbinh()}')
        print(f'Điểm cao nhất: {self.DiemCaoNhat()}')
        print('Các môn giỏi nhất: ', end='')
        self.CacMonGioiNhat()
        print(f'Xếp hạng: {self.xephang()}')
        print('-'*20)
    

#tạo đối tượng
std1 = Student()
std1.name = 'Nguyễn Văn A'
std1.group = '10A1'
std1.scores = {'toán': 10, 'lý': 9, 'hóa': 8}

std2 = Student()
std2.name = 'Trần Thị B'
std2.group = '9B2'
std2.scores = {'toán': 7, 'văn': 7, 'anh': 4}

std3 = Student()
std3.name = 'Lê Văn C'
std3.group = '11C3'
std3.scores = {'văn': 9, 'sửa': 9, 'địa': 9}

#danh sách sinh viên
danh_sach_sinh_vien = [std1, std2, std3]
for std in danh_sach_sinh_vien:
    std.inthongtin()