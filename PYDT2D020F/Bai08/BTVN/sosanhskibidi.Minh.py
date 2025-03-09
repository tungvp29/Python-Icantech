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

[3942, 1687, 1116, 4043, 7221, 6752, 228, 9054, 7941, 9519, 9600, 4059, 8555, 5566, 4464, 6326, 7656, 1054, 2293, 4465, 9555, 5190, 9479, 3498, 6190, 2562, 3318, 9588, 5973, 5880, 6668, 3945, 6193, 8897, 6455, 8499, 1358, 7143, 3537, 7754, 592, 7118, 8937, 2780, 8431, 4958, 5926, 8677, 5242, 9680, 8214, 2548, 8884, 8577, 2163, 6411, 7437, 1358, 9143, 6868, 6964, 879, 4456, 7987, 4048, 2096, 4767, 212, 233, 3952, 5895, 7220, 9402, 1261, 7983, 2957, 2400, 9594, 5189, 8237, 9991, 2681, 9407, 707, 7954, 902, 6128, 9322, 9846, 3139, 8976, 7403, 3770, 4600, 8710, 4353, 2422, 8258, 6798, 5546]