from tkinter import *
from tkinter import messagebox
from random import *

window = Tk()
window.geometry('350x200')
window.title('Welcome to guessing game')

guess = 0
score = 10
target = 0


def random_number():
    global target
    target = randint(1,10)
    messagebox.showinfo(message='Random Number Generated; start guessing !! STARTING SCORE = 10')
    random_number_button['state']=DISABLED
    guess_button['state']=NORMAL

def add():
    return('The sum of target and guess is '+str(guess+target))
def sub():
    return('The difference of target and guess is '+str(target - guess))
def multiplication():
    return('The product of target and guess is '+str(guess * target))
def division():
    return('The division of target by guess is '+str(target/guess))

def greater_lesser():
    if target < guess:
        return ('Target is less than guess')
    elif target > guess:
        return ('Target is greater than guess')

def clues():
    switcher = {
       0: add(),
       1: sub(),
       2: multiplication(),
       3: division(),
       4: greater_lesser()
       }
    return switcher.get(randint(0,4))

def guess():
    global guess
    global score
    try:
        guess = 0
        guess = int(guess_entry.get())
    except:
        messagebox.showerror(message='Enter a number to guess and play')
        return
    if target == guess:
        messagebox.showinfo(message='Congratulations!!! you have guessed the correct number, your score is '+str(score))
        random_number_button['state']=NORMAL
        guess_button['state']=DISABLED
        return
    elif score == 0:
        messagebox.showwarning(message='Out of Guess Buddy! Better luck next time );')
        return
    else:
        score -= 1
        message = clues()
        messagebox.showinfo(message=message)

Label(window,text='Number guessing game \n guess a number between 1 to 10',font=('Ubuntu Mono',12)).pack()
random_number_button=Button(window,text='Generate Random Number',command=random_number)
random_number_button.pack()

Label(window,text='Enter your guess: ').pack()
guess_entry=Entry(window,width=3)
guess_entry.pack()

guess_button=Button(window,text='Guess Me',command=guess,state=DISABLED)
guess_button.pack()

window.mainloop()
