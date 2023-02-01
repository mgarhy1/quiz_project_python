# ask user to enter their name
name = input("what is your name? ")
# print greetings
print(f"welcome to quiz {name} \nplease answer the following questions \n")
# score counter
score = 0
# questions add or change from here
q1 = '2+2 = ? '
q2 = '4+3 = ? '
q3 = '4+5 = ? '
# answers add or change from here
ans1 = "4"
ans2 = "7"
ans3 = "9"
# change the success score here for the exam min passing score
success_score = 2
# each right question points change according right answers points
score_points = 1

# questions and answers tuple & list
questions = [(q1, ans1), (q2, ans2), (q3, ans3)]
# for loop to take user answers and compare them with the right answers
for quest, correct_answer in questions:
    # user answer input
    answer = input(f"{quest}")
    # check if user answer is correct
    if answer == correct_answer:
        # add to score if answer is correct
        score += score_points
        # print total score
        print("correct", "you score", score)
    # if user answer is incorrect
    else:
        # if answer is wrong it will print wrong and quit or continue
        print("wrong")
        # quit once answer is wrong (remove break to continue)
        break
# when sum of right answers is equal or greater than the minimum score to pass
if score >= success_score:
    print(f"your score is: {score}")
    print("passed")
# when sum of right answers is less than the minimum score to pass
else:
    print(f"your score is: {score}")
    print("failed")
