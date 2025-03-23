import datetime as dt
import random as r
import math as m
Operations = ['+', '-']
count = 0
def gen_quiz():
    number1 = r.randint(0, 20)
    number2 = r.randint(0, 20)
    op = r.choice(Operations)
    quiz = f"{number1} {op} {number2}"
    return quiz

def time_diff(first_time, last_time):
    diff = last_time - first_time
    second_in_day = 24 * 60 * 60
    time_ans = divmod(diff.days * second_in_day + diff.seconds, 60)
    return time_ans 

def score(time_ans, count):
    if (time_ans[-2] == 0):
        print(f"Ban tra loi dung {count} cau trong thoi gian {time_ans[-1]} giay")
    else:
        print(f"Ban tra loi dung {count} cau trong thoi gian {time_ans[-2]} phut {time_ans[-1]} giay")
start = input("Nhap Y de bat dau")
if start == 'Y' or start == 'y':
    start_time = dt.datetime.now()
    while True:
        quiz = gen_quiz()
        print(quiz)
        answer = input("Nhap cau tra loi: ")
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
    print("Goodbye")

