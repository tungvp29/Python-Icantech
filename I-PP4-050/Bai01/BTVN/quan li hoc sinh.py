class HocSinh:
    def __init__(self, ten, diem_toan, diem_ly, diem_hoa):
        self.ten = ten
        self.diem_toan = diem_toan
        self.diem_ly = diem_ly
        self.diem_hoa = diem_hoa

    def tinh_diem_trung_binh(self):
        return (self.diem_toan + self.diem_ly + self.diem_hoa) / 3

    def xep_loai(self):
        diem_tb = self.tinh_diem_trung_binh()
        if diem_tb >= 8.5:
            return "Giỏi"
        elif diem_tb >= 6.5:
            return "Khá"
        elif diem_tb >= 5.0:
            return "Trung bình"
        else:
            return "Yếu"
    def hien_thi_thong_tin(self):
        print(f"\n Thông tin học sinh:")
        print(f" Tên: {self.ten}")
        print(f" Điểm Toán: {self.diem_toan}")
        print(f" Điểm Lý: {self.diem_ly}")
        print(f" Điểm Hóa: {self.diem_hoa}")
        print(f" Điểm trung bình: {self.tinh_diem_trung_binh():.2f}")
        print(f" Xếp loại: {self.xep_loai()}")
ten = input("Nhập tên học sinh: ")
toan = float(input("Nhập điểm Toán: "))
ly = float(input("Nhập điểm Lý: "))
hoa = float(input("Nhập điểm Hóa: "))
hs = HocSinh(ten, toan, ly, hoa)
hs.hien_thi_thong_tin()