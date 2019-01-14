import csv
import random
# Import and list questions from data.csv
quiz = dict(csv.reader(open("data.csv", encoding='utf-8')))
quizList = list(quiz.keys())

print ("Python Kana Quiz")
print ("respond to the kana with the correct latin character")
print ("answer 'quit' to end")

while True:
    question = random.choice(quizList)
    answer = quiz[question]

    print (question)
    questionAsk = input()

    if questionAsk == (answer):
        print("correct")
        continue
    elif questionAsk == ("quit"):
        exit()
    else:
        print("incorrect,", (answer))
        continue
