#Work in progress

from tkinter import *
import csv
import random

# Import and list questions from data.csv
quiz = dict(csv.reader(open("data.csv", encoding='utf-8')))
quizList = list(quiz.keys())
# Set up tkinter junk
root = Tk()
# Window settings
root.title("Kana Quiz")
root.geometry("300x200")
# Get quiz variable
question = random.choice(quizList)
answer = quiz[question]
# Make a label for the kana
label = Label(text=question)
label.config(font=("Courier", 60))
label.pack()
# Answer box
a = Entry(root)
a.pack()

# Label for feedback
fb_label = Label(text="Unanswered")
fb_label.pack()

def submit_a(root):
    a_s = a.get()
    print ("a_s is:", a_s)

    if a_s == (answer):
        print("correct")
        fb_label.config(text='Correct')

    else:
        print("incorrect,", (answer))
        fb_label.config(text='Incorrect')




a.bind("<Return>", submit_a)


root.mainloop()
