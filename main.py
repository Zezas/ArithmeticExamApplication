# write your code here
import math
import random


def choose_level():
    while True:
        try:
            level = int(input("Which level do you want? Enter a number:\n1 - simple operations with numbers 2-9\n2 - integral squares of 11-29\n"))
            return level
        except ValueError:
            print("Incorrect format.")


def new_task(level):
    if level == 1:
        calc = str(random.randint(2, 9)) + str(random.choice([" + ", " - ", " * "])) + str(random.randint(2, 9))
        return calc
    elif level == 2:
        calc = str(random.randint(11, 29))
        return calc


def is_right_answer(level, calc, answer):
    if level == 1 and calc == answer:
        return True
    elif level == 2 and math.pow(calc, 2) == answer:
        return True
    else:
        return False


max_tasks = 5
right_answer = 0
chosen_level = choose_level()
save_options = ["yes", "YES", "y", "Yes"]

for __ in range(max_tasks):
    challenge = new_task(chosen_level)
    print(challenge)
    challenge = eval(challenge)
    while True:
        try:
            result = int(input())
            break
        except ValueError:
            print("Incorrect format.")

    if is_right_answer(chosen_level, challenge, result):
        print("Right!")
        right_answer += 1
    else:
        print("Wrong!")

print(f"Your mark is {right_answer}/{max_tasks}.")
save_to_file = input("Would you like to save your result to the file? Enter yes or no.\n")
if save_to_file in save_options:
    name = input("What is your name?\n")
    results = open("results.txt", "a")
    if chosen_level == 1:
        results.write(f"{name}: {right_answer}/{max_tasks} in level 1 (simple operations with numbers 2-9).\n")
    elif chosen_level == 2:
        results.write(f"{name}: {right_answer}/{max_tasks} in level 2 (integral squares 11-29).\n")
    results.close()
    print('The results are saved in "results.txt"')