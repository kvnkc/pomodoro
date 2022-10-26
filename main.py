from cgitb import reset
import tkinter
from turtle import bgcolor

PINK = '#e2979c'
RED = '#e7305b'
GREEN = '#9bdeac'
YELLOW = '#f7f5dd'
FONT_NAME = 'Courier'
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = tkinter.Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = tkinter.Label(
    text='Timer', font=(FONT_NAME, 30, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
timer_label.grid(row=0, column=1)

check_mark_label = tkinter.Label(
    text='✓', font=(FONT_NAME, 14, 'bold'), fg=GREEN, bg=YELLOW, highlightthickness=0)
check_mark_label.grid(row=3, column=1)

canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = tkinter.PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)
canvas.create_text(100, 130, text='00:00', fill='white',
                   font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

start_button = tkinter.Button(text="Start")
start_button.grid(row=2, column=0)

reset_button = tkinter.Button(text='Reset')
reset_button.grid(row=2, column=2)

window.mainloop()
