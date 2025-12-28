# Math Quiz Game
# Random arithmetic quiz (+, -, *)
# Author: gimsinu631

import random

TOTAL_QUESTIONS = 5
MAX_NUMBER = 100
    
def make_question(num1, operator, num2):
    if operator == 1:
        print(f"{num1} + {num2} = ?")
        return num1 + num2
    elif operator == 2:
        print(f"{num1} - {num2} = ?")
        return num1 - num2
    else:
        print(f"{num1} * {num2} = ?")
        return num1 * num2

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print('correct')
        return True
    else:
        print('incorrect')
        return False
    
correct_count = 0

for _ in range(TOTAL_QUESTIONS):
    num1 = random.randint(1, MAX_NUMBER)
    operator = random.randint(1, 3)
    num2 = random.randint(1, MAX_NUMBER)
    correct_answer = make_question(num1, operator, num2)

    try:
        user_answer = int(input('Please enter the answer: '))
    except ValueError:
        print('Please enter a number only')
        continue

    is_correct = check_answer(user_answer, correct_answer)

    if is_correct:
        correct_count += 1

print(f"Total score: {correct_count}/5")
