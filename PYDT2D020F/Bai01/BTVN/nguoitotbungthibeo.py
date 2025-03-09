f = open('tracnghiem.txt' , "r", encoding = 'utf-8')
list = f.readlines()

totbung = input(list[0])
if (totbung == "1"):
    kqc1 = 'dung'
else:
    kqc1 = 'sai'

dangyeuvaytroi = input(list[1])
if (dangyeuvaytroi == '2'):
    kqc2 = 'dung'
else:
    kqc2 = 'sai'

thattha = input(list[2])
if (thattha == '3'):
    kqc3 = 'dung'
else:
    kqc3 = 'sai'

hayhot = input(list[3])
if (hayhot == '4'):
    kqc4 = 'dung'
else:
    kqc4 = "sai"
f.close()
f = open('tracnghiemketqua.txt', 'w')
f.write('cau1:{}\n'.format(kqc1))
f.write('cau2:{}\n'.format(kqc2))
f.write('cau3:{}\n'.format(kqc3))
f.write('cau4:{}\n'.format(kqc4))