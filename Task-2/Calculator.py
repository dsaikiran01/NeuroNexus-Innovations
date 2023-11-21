#Calculator

from tkinter import *

app = Tk()
app.title("Calculator")
app.iconbitmap(".\\Calculator_icon.ico")
app.configure(bg="black")

#display
entries = Entry(app, width=30, borderwidth=5, font="bold", bg="#9cb0b4")
entries.grid(row=0, column=0, columnspan=4)

##functions
#clear contents
def clear_display():
    entries.delete(0, END)

#entering a number
def button_click_enter(number):
    current = entries.get()
    clear_display()
    entries.insert(0, str(current) + str(number))

#symbols button: All operations compiled
def operations(option):
    global first_number, operation, current
    current = entries.get()
    first_number = int(current)
    operation_menu = ["addition", "subtraction", "multiplication", "division"]
    clear_display()
    operation = operation_menu[option]
    return operation

#symbols button: equal
def equal():
    second_number = entries.get()
    clear_display()
    global operation
    if operation == "addition":
        entries.insert(0, first_number + int(second_number))
    elif operation == "subtraction":
        entries.insert(0, first_number - int(second_number))
    elif operation == "multiplication":
        entries.insert(0, first_number * int(second_number))
    elif operation == "division":
        try:
            if second_number == "0":
                entries.insert(0, "undefined")
        except:
            entries.insert(0, first_number / int(second_number))
    


##buttons
button_1 = Button(app, text="1", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(1))
button_2 = Button(app, text="2", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(2))
button_3 = Button(app, text="3", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(3))
button_4 = Button(app, text="4", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(4))
button_5 = Button(app, text="5", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(5))
button_6 = Button(app, text="6", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(6))
button_7 = Button(app, text="7", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(7))
button_8 = Button(app, text="8", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(8))
button_9 = Button(app, text="9", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(9))
button_0 = Button(app, text="0", width=7, height=4, font="bold", fg="#03ccfe", bg="#3c4b5a", command=lambda: button_click_enter(0))

button_add = Button(app, text="+", width=7, height=4, font="bold", fg="#070707", bg="#0c9bf2", command=lambda: operations(0))
button_sub = Button(app, text="-", width=7, height=4, font="bold", fg="#070707", bg="#0c9bf2", command=lambda: operations(1))
button_mul = Button(app, text="x", width=7, height=4, font="bold", fg="#070707", bg="#0c9bf2", command=lambda: operations(2))
button_div = Button(app, text="/", width=7, height=4, font="bold", fg="#070707", bg="#0c9bf2", command=lambda: operations(3))
button_cld = Button(app, text="AC", width=7, height=4, font="bold", fg="#070707", bg="#04AF70", command=clear_display)
button_eql = Button(app, text="=", width=7, height=4, font="bold", fg="#070707", bg="#111ef1", command=equal)

#buttons position
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_cld.grid(row=1, column=3)

button_6.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_4.grid(row=2, column=2)
button_add.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_div.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_sub.grid(row=4, column=1)
button_mul.grid(row=4, column=2)
button_eql.grid(row=4, column=3)

#window holder
app.mainloop()
