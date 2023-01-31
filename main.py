# ask user to enter their name
name = input("what is your name? ")
# print greetings
print(f"welcome to quiz {name} \nplease answer the following questions \n")
# score counter
score = 0
# questions
q1 = '2+2 = ? '
q2 = '4+3 = ? '
q3 = '4+5 = ? '
# answers
ans1 = "4"
ans2 = "7"
ans3 = "9"
# questions and answers tuple
questions = [(q1, ans1), (q2, ans2), (q3, ans3)]

# for loop to take user answers and compair it with right answers
for quest, correct_answer in questions:
    # user answer input
    answer = input(f"{quest}")
    # check if user answer is correct
    if answer == correct_answer:
        # add to score if answer is correct
        score += 1
        # print total score
        print("correct", "score", score)
    else:
        # if answer is wrong it will print wrong and quit
        print("wrong")
        # quit once answer is wrong (remove to continue)
        break