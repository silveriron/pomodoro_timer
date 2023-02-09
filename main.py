from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = "✓"

progress = 0
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    canvas.itemconfig(count_text, text="00:00")
    check_label.config(text="")

    global reps, progress
    reps = progress = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_count():
    global reps
    global progress
    reps += 1

    time = 0

    if reps % 8 == 0:
        time = LONG_BREAK_MIN * 60
        title_label.config(text="Break", fg=RED)
        reps == 0
        progress = 0
    elif reps % 2 == 1:
        time = WORK_MIN * 60
        title_label.config(text="Work", fg=GREEN)
    elif reps % 2 == 0:
        time = SHORT_BREAK_MIN * 60
        title_label.config(text="Break", fg=PINK)
        progress += 1

    check_label["text"] = CHECK * progress
    count_down(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    minute = count // 60
    second = ("0" + str(count % 60))[-2:]
    canvas.itemconfig(count_text, text=f"{minute}:{second}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_count()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
check_label = Label(text="", fg=GREEN, bg=YELLOW)

start_button = Button(text="Start", bg="white", border=0, command=start_count)
reset_button = Button(text="Reset", bg="white", border=0, command=reset)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
count_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

title_label.grid(row=0, column=1)
canvas.grid(row=1, column=1)
start_button.grid(row=2, column=0)
reset_button.grid(row=2, column=2)
check_label.grid(row=3, column=1)

window.mainloop()
