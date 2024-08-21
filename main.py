from tkinter import *
from tkinter import messagebox
from math import floor
# ---------------------------- CONSTANTS ------------------------------- #
BLUE = "#1571be"
LIGHT_BLUE = "#57fffb"
BLACK = "#030305"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 


def reset_timer():
    window.after_cancel(str(timer))
    title_label.config(text="Timer", fg=LIGHT_BLUE)
    canvas.itemconfig(timer_text, text="00:00")
    tick_mark.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        title_label.config(text="Break", fg=BLUE)
        messagebox.showinfo(title="Long Break", message="Well Done!\nYou can take a break.")
        countdown(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=BLUE)
        messagebox.showinfo(title="Short Break", message="Well Done!\nYou can take a break.")
        countdown(short_break_sec)
    else:
        title_label.config(text="Work", fg=LIGHT_BLUE)
        messagebox.showinfo(title="Work", message="Time to start Working!")
        countdown(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(count):
    minutes = floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        mark = "Sessions Completed:\n" + "✔" * (floor(reps/2) + 1)
        tick_mark.config(text=mark)
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, background=BLACK)
window.resizable(False, False)

title_label = Label(text="Timer")
title_label.grid(column=1, row=0)
title_label.config(background=BLACK, foreground=LIGHT_BLUE, font=(FONT_NAME, 35, "bold"))

canvas = Canvas(width=360, height=360, background=BLACK, highlightthickness=0)
tomato = PhotoImage(file="pomodoro.png")
canvas.create_image(180, 180, image=tomato)
timer_text = canvas.create_text(180, 180, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(width=10, height=2, text="Start", command=start_timer, highlightthickness=0, bg=BLACK,
                      fg=LIGHT_BLUE, font=(FONT_NAME, 15, "bold"))
start_button.grid(column=0, row=2)

reset_button = Button(width=10, height=2, text="Reset", command=reset_timer, highlightthickness=0, bg=BLACK,
                      fg=LIGHT_BLUE, font=(FONT_NAME, 15, "bold"))
reset_button.grid(column=2, row=2)

tick_mark = Label(background=BLACK, foreground=LIGHT_BLUE, font=(FONT_NAME, 15, "bold"))
tick_mark.grid(column=1, row=3)

window.mainloop()
