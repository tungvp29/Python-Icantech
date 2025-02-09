#mở file
f = open('tracnghiem.txt', 'r', encoding='utf-8')

#đọc nội dung
list = f.readlines()
f.close()
#hỏi câu hỏi 1 > 4
dapAn1, dapAn2, dapAn3, dapAn4 = '', '', '', ''
#lưu câu trả lời vào các biến đáp án
cauTL1 = input(list[0])
if (cauTL1 == '1'):
    dapAn1 = 'Đúng'
else:
    dapAn1 = 'Sai'

cauTL2 = input(list[1])
if (cauTL2 == '2'):
    dapAn2 = 'Đúng'
else:
    dapAn2 = 'Sai'

cauTL3 = input(list[2])
if (cauTL3 == '3'):
    dapAn3 = 'Đúng'
else:
    dapAn3 = 'Sai'

cauTL4 = input(list[3])
if (cauTL4 == '4'):
    dapAn4 = 'Đúng'
else:
    dapAn4 = 'Sai'

#ghi nội dung vào file ketqua.txt
f = open('ketqua.txt', 'w', encoding='utf-8')
f.write('Câu 1: ' + dapAn1 + '\n')
f.write('Câu 2: ' + dapAn2 + '\n')
f.write('Câu 3: ' + dapAn3 + '\n')
f.write('Câu 4: ' + dapAn4 + '\n')
f.close()