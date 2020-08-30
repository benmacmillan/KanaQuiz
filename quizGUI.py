from tkinter import *
import csv
import random

# tkinter setup and window config
root = Tk()
root.title("Kana Quiz")
root.geometry("300x200")
root.iconbitmap('ico.ico')
root.resizable(width=False, height=False)
# Import and list questions from data.csv
quiz = dict(csv.reader(open("data.csv", encoding='utf-8')))
quizList = list(quiz.keys())
# Quiz variable
question = random.choice(quizList)
answer = quiz[question]
# Kana label display
k_label = Label(text=question)
k_label.config(font=("MS Gothic", 60))
k_label.pack(pady=30)
# Answer box
a = Entry(root)
a.pack()
# Label for input feedback
fb_label = Label(text="Unanswered")
fb_label.pack()

def randomkana():
    global question
    global answer
    global a
    question = random.choice(quizList)
    answer = quiz[question]
    k_label.config(text=question)
    a.delete(0, 'end')
def submit_a(root):
    a_s = a.get()
    if a_s == answer:
        print("correct")
        fb_label.config(text='Correct', fg='blue')
        randomkana()
    else:
        print("incorrect,", answer)
        fb_label.config(text='Incorrect', fg='red')
a.bind("<Return>", submit_a)
root.mainloop()