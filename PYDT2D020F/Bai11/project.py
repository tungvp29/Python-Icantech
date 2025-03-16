import datetime as dt
import random as r
import math as m

Operations = ['+', '-', 'x', 'chia lấy dư', 'chia lấy nguyên', '^', 'V']
count = 0

#hàm tạo câu hỏi ngẫu nhiên
def gen_quiz():
    number1 = r.randint(0, 20)
    number2 = r.randint(0, 20)
    op = r.choice(Operations)
    quiz = generate_function(number1, op, number2)
    return quiz

def generate_function(num1, op, num2):
    if op == 'x':
        return f"{num1} * {num2}"
    elif op == 'chia lấy dư':
        return f"{num1} % {num2}"
    elif op == 'chia lấy nguyên':
        return f"{num1} // {num2}"
    elif op == '^':
        return f'm.pow({num1}, {num2})'
    elif op == 'V':
        return f'm.sqrt({num1})'
    else:
        return f"{num1} {op} {num2}"

#hàm tính thời gian trả lời
def time_diff(first_time, last_time):
    diff = last_time - first_time
    seconds_in_day = 24 * 60 * 60
    time_ans = divmod(diff.days * seconds_in_day + diff.seconds, 60)
    return time_ans

#hàm in kết quả trả lời và thời gian
def score(time_ans, count):
    if (time_ans[-2] == 0):
        print(f'Bạn trả lời đúng {count} câu trong thời gian {time_ans[-1]} giây')
    else:
        print(f'Bạn trả lời đúng {count} câu trong thời gian {time_ans[-2]} phút {time_ans[-1]} giây')

#vòng lặp 
start = input("Nhập Y để bắt đầu: ")
if start == 'Y' or start == 'y':
    start_time = dt.datetime.now()
    while True:
        quiz = gen_quiz()
        print(quiz)
        answer = input("Nhập câu trả lời: ")
        result = eval(quiz)
        if int(answer) == result:
            count += 1
            continue
        else:
            end_time = dt.datetime.now()
            time_ans = time_diff(start_time, end_time)
            score(time_ans, count)
            break
else:
    print('Hẹn gặp lại!')
        