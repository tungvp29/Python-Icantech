giatraicay = {
    "tao": 40000,
    "chuoi": 15000,
    "cam": 90000,
    "xoai": 45000,
    "nho": 180000
}

def tinhtonggia(traicay, soluong):
    if traicay not in giatraicay:
        return "Loai trai cay khong co trong danh sach gia ban."
    try:
        tonggia = giatraicay[traicay] * soluong
        return tonggia
    except ValueError:
        return "Gia tri khong hop le."

def themtraicay(traicay, gia):
    giatraicay[traicay] = gia
    print(f"Da them {traicay} voi gia {gia} dong/kg")

def thaydoigia(traicay, gia):
    if traicay in giatraicay:
        giatraicay[traicay] = gia
        print(f"Da thay doi gia cua {traicay} thanh {gia} dong/kg")
    else:
        print("Loai trai cay khong co trong danh sach gia ban.")

def main():
    while True:
        print("======= MENU =======")
        print("1. Tinh gia tien")
        print("2. Them trai cay")
        print("3. Thay doi gia")
        print("4. Thoat")
        chon = input("Vui long chon mot tuy chon (1/2/3/4): ")
        
        if chon == "1":
            print("Chon loai trai cay:")
            for traicay, gia in giatraicay.items():
                print(f"- {traicay}: {gia} dong/kg")
            
            traicay = input("Nhap loai trai cay: ").lower()
            try:
                soluong = float(input("Nhap so luong (kg): "))
                tonggia = tinhtonggia(traicay, soluong)
                if isinstance(tonggia, str):
                    print(tonggia)
                else:
                    print(f"Tong gia tien: {tonggia} dong")
                    sotien = float(input("Nhap so tien khach hang tra (dong): "))
                    tienthua = sotien - tonggia
                    print(f"Tra lai khach hang so tien {tienthua} dong")
            except ValueError:
                print("Gia tri khong hop le.")
        elif chon == "2":
            traicay = input("Nhap loai trai cay moi: ").lower()
            try:
                gia = float(input("Nhap gia cua trai cay moi (dong/kg): "))
                themtraicay(traicay, gia)
            except ValueError:
                print("Gia tri khong hop le.")
        elif chon == "3":
            traicay = input("Nhap loai trai cay can thay doi gia: ").lower()
            try:
                gia = float(input("Nhap gia moi (dong/kg): "))
                thaydoigia(traicay, gia)
            except ValueError:
                print("Gia tri khong hop le.")
        elif chon == "4":
            print("Cam on ban. Tam biet!")
            break
        else:
            print("Tuy chon khong hop le.")
main()
