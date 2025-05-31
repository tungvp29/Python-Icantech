import pandas as pd
a = ['Đạt', 'Khang', 'Trường']
mySeries = pd.Series(a)
print(mySeries)
print(mySeries[1])

# Gán nhãn (tạo chỉ số khác)
mySeries1 = pd.Series(a, index=['hs1', 'hs2', 'hs3'])
print(mySeries1)
print(mySeries1['hs1'])

dic={'táo':18,'Cam':22,'Nhãn':50,'lê':42}
dic1=pd.Series(dic)
print(dic1)
print(dic1['Cam'])
#DataFrame và danh sách 2 chiều
data={'Tên':['Khang','Trường','Đạt'],'Điểm':[9,10,9]}
frame1=pd.DataFrame(data)
print(frame1)
print(frame1.loc[[0,1]])#đưa ra hàng 0 và hàng 1 của Frame1
#đọc dữ liệu từ file csv
# data= pd.read_csv('b1.csv')
# print(data)
# print('_____________')
# print(data.info())
