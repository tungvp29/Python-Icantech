import random

def taoDanhSachNgauNhien(soPhanTu):
    danhSachNgauNhien = []
    for i in range(soPhanTu):
        danhSachNgauNhien.append(random.randint(1, 10000))  
    return danhSachNgauNhien

def timKiemTuanTu(danhSach, mucTieu):
    buoc = 0
    for i in range(len(danhSach)):
        buoc = buoc + 1
        if danhSach[i] == mucTieu:
            return i, buoc
    return None, buoc

def timKiemNhiPhan(danhSach, mucTieu):
    buoc = 0
    thap = 0
    cao = len(danhSach) - 1

    while thap <= cao:
        giua = (thap + cao) // 2
        buoc = buoc + 1
        if danhSach[giua] == mucTieu:
            return giua, buoc
        elif danhSach[giua] < mucTieu:
            thap = giua + 1
        else:
            cao = giua - 1
    return None, buoc

soPhanTu = int(input("Nhập số phần tử: "))
danhSachNgauNhien = taoDanhSachNgauNhien(soPhanTu)

print(f"Dãy số ngẫu nhiên là: {danhSachNgauNhien}")

mucTieu = int(input("Nhập số cần tìm: "))

ketQua1, buoc1 = timKiemTuanTu(danhSachNgauNhien, mucTieu)

danhSachDaSapXep = sorted(danhSachNgauNhien)

ketQua2, buoc2 = timKiemNhiPhan(danhSachDaSapXep, mucTieu)

if ketQua1 is not None:
    print(f"Bằng phương pháp tìm kiếm tuần tự, tìm thấy số {mucTieu} ở vị trí {ketQua1} với số bước {buoc1}")
else:
    print(f"Không tìm thấy số {mucTieu} bằng phương pháp tìm kiếm tuần tự.")

if ketQua2 is not None:
    print(f"Bằng phương pháp tìm kiếm nhị phân, tìm thấy số {mucTieu} ở vị trí {ketQua2} với số bước {buoc2}")
else:
    print(f"Không tìm thấy số {mucTieu} bằng phương pháp tìm kiếm nhị phân.")
