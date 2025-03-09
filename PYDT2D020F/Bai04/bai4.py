import random

#cấu hình
CONSTANTS = (
    ('Số lượng câu hỏi', 5),
    ('Số lượng bảng cửu chương', 10),
    ('Điểm cho mỗi câu hỏi', 1)
)

#bảng xếp hạng
leaderboard = []

#hàm tạo câu hỏi
def generate_question():
    x = random.randint(1, CONSTANTS[1][1])
    y = random.randint(1, CONSTANTS[1][1])
    return (x, y, x * y)

#ham hiển thị câu hỏi
def ask_question(question):     #question = (5, 6, 30)
    x, y, answer = question
    user_answer = int(input(f"Đáp án của {x} x {y} là?"))
    if user_answer == answer:
        print("Chính xác!")
        return True
    else:
        print(f"Sai rồi! Đáp án là: {answer}")
        return False    

#hàm lưu leaderboard vào file
def save_leaderboard():
    with open('leaderboard.txt', 'w') as f:
        for item in leaderboard:
            f.write(f"{item[0]}:{item[1]}\n")

#hàm đọc leaderboard từ file
def load_leaderboard():
    global leaderboard
    try:
        with open('leaderboard.txt', 'r') as f:
            for line in f:
                score, name = line.strip().split(':')
                leaderboard.append((int(score), name))
    except FileNotFoundError:
        pass

def play_game():
    print('==============Game started==============')
    num_questions = CONSTANTS[0][1]
    points_per_question = CONSTANTS[2][1]    

    questions = []
    for i in range(num_questions):
        question = generate_question()
        questions.append(question)
    
    score = 0
    for question in questions:
        if ask_question(question) == True:
            score += points_per_question
    print('======   Game over   ======')

    #hiển thị tổng điểm
    print(f"Điểm của bạn: {score}")
    
    #lưu điểm vào bảng xếp hạng
    leaderboard.append((score, input("Nhập tên của bạn: ")))
    leaderboard.sort(reverse=True)
    save_leaderboard()
    
    #hiển thị bảng xếp hạng
    for i, score in enumerate(leaderboard):
        print(f"{i+1}. {score[1]}: {score[0]}")

    print('======================================')

#hàm xem bảng xếp hạng
def display_leaderboard():
    print('======   Bảng xếp hạng   ======')
    if len(leaderboard) == 0:
        print("Chưa có ai chơi game")
        pass
    for i, score in enumerate(leaderboard):
        print(f"{i+1}. {score[1]}: {score[0]}")
    print('===============================')

#hàm menu
def menu():
    print('======   Menu   ======')
    print('1. Chơi game')
    print('2. Xem bảng xếp hạng')
    print('3. Thoát')
    print('======================')

#vòng lặp while
while True:
    load_leaderboard()
    menu()
    choice = input("Chọn chức năng: ")
    if choice == "1":
        play_game()
    elif choice == "2":
        display_leaderboard()
    elif choice == "3":
        print("Chương trình đã kết thúc")
        break
    else:
        print("Chức năng không tồn tại, vui lòng chọn lại!")