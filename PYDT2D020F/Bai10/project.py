def Create5(soTang, len):
  #số khoảng trắng trước mỗi dòng tam giác
  space = (soTang - len) * 10
  #print(space, len, soTang)
  #Vẽ hình tam giác và khoảng trắng
  for i in range(5):
    print(" " * (space - (soTang - len)), end = "")    #Khoảng trắng từ lề đến hcn chứa tam giác
    print("  " * (5 - i), end = "")  #Khoảng trắng từ mép hcn đến cạnh tam giác
    for j in range(len):
      print("* " * (i * 2 + 1), end = "")    #Các hình tam giác cân màu đen
      print("  " * ((4 - i) * 2), end = "")  #các hình tam giác ngược màu trắng
    print()    #xuống dòng tiếp theo
  #biến len đếm tầng hiện tại đang vẽ, nếu chưa đủ số tầng thì gọi lại hàm vẽ Create()
  if (len != soTang):
    Create5(soTang, len + 1)
    
def Create3(soTang, len):
  #số khoảng trắng trước mỗi dòng tam giác
  space = (soTang - len) * 5

  #Vẽ hình tam giác và khoảng trắng
  for i in range(3):
    print(" " * (space), end = "")    #Khoảng trắng từ lề đến hcn chứa tam giác
    print("  " * (3 - i), end = "")  #Khoảng trắng từ mép hcn đến cạnh tam giác
    for j in range(len):
      print("* " * (i * 2 + 1), end = "")    #Các hình tam giác cân màu đen
      print("  " * ((2 - i) * 2), end = "")  #các hình tam giác ngược màu trắng
    print()    #xuống dòng tiếp theo
  #biến len đếm tầng hiện tại đang vẽ, nếu chưa đủ số tầng thì gọi lại hàm vẽ Create()
  if (len != soTang):
    Create3(soTang, len + 1)
# Create3(4, 1)
#Hàm xóa màn hình
def ClearScreen():
  print("\033[H\033[J", end="")

def ReturnMessage():
  print('---------------------')
  input('Nhấn Enter để quay lại.')
  
def Menu():
  print('1. Tam giác 3 tầng')
  print('2. Tam giác 5 tầng')
  print('3. Thoát chương trình:  ')

#Vòng lặp chính
while True:
  ClearScreen()
  Menu()
  choice = input('Chọn chức năng chương trình: ')
  if choice == "1":
    #Vẽ tam giác sierpinski 3 tầng
    try:
      ClearScreen()
      st = int(input('Nhập số tầng của tam giác: '))
      Create3(st, 1)
      ReturnMessage()
    except ValueError:
      print('Dữ liệu không phù hợp, vui lòng thử lại!')
      ReturnMessage()
    except:
      print('Lỗi không xác định, vui lòng thử lại sau!')
      ReturnMessage()

  elif choice == "2":
    #Vẽ tam giác sierpinski 5 tầng
    try:
      ClearScreen()
      st = int(input('Nhập số tầng của tam giác: '))
      Create5(st, 1)
      ReturnMessage()
    except ValueError:
      print('Dữ liệu không phù hợp, vui lòng thử lại!')
      ReturnMessage()
    except:
      print('Lỗi không xác định, vui lòng thử lại sau!')
      ReturnMessage()

  elif choice == "3":
    break
  else:
    print('Lựa chọn không phù hợp, vui lòng thử lại!')
  