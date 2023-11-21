from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

app = Tk()
app.title("To-Do List")
app.iconbitmap(".\\to_do_list_icon.ico")
app.configure(bg="#878383")

#font for the app
app_font = Font(
    family="Courier New Regular",
    weight="bold",
    size=20
)

#adding a for interface
app_frame = Frame(app)
app_frame.pack(pady=30) #pady for space below the application

#adding the listbox
app_list_box = Listbox(
    app_frame,
    font=app_font,
    width=25,
    height=5,
    bg="#d7d2d2",
    fg="#464646",
    highlightthickness=0,
    selectbackground= "#a6a6a6", 
    activestyle="none"
)
app_list_box.pack(side=LEFT, fill=BOTH)

#adding a scroll bar
app_scroll_bar = Scrollbar(app_frame)
app_scroll_bar.pack(side=RIGHT, fill=BOTH)

#add list entry box
list_entry_box = Entry(app, font=("Courier New bold", 24), bg="#9cb0b4")
list_entry_box.pack(pady=20)

#adding a frame for all the buttons
button_frame = Frame(app, bg="#878383")
button_frame.pack(pady=20)

#button functions
def delete():
    app_list_box.delete(ANCHOR)

def add():
    app_list_box.insert(END, list_entry_box.get())
    list_entry_box.delete(0, END)

def cross_off():
    #for crossing item
    app_list_box.itemconfig(
        app_list_box.curselection(), fg="#dedede"
    )
    #remove selection bar after crossing off
    app_list_box.select_clear(0, END)

def uncross_off():
    app_list_box.itemconfig(
        app_list_box.curselection(), fg="#464646"
    )
    app_list_box.select_clear(0, END)

def delete_cross_off():
    count = 0
    while count < app_list_box.size():
        if app_list_box.itemcget(count, "fg") == "#dedede":
            app_list_box.delete(app_list_box.index(count))
        else:
            count += 1

def save_list():
    #poping dialog box
    filename = filedialog.asksaveasfilename(
        initialdir="./data",
        title="Save File",
        filetypes=(("Dat Files", "*.dat"), ("All Files", "*.*"))
    )
    if filename:
        if filename.endswith(".dat"):
            pass
        else:
            filename = f"{filename}.dat"
    
    #deleting cross off items before saving
    delete_cross_off()

    #take remaining list and save
    remaining_list = app_list_box.get(0, END)
    output_file = open(filename, 'wb')
    pickle.dump(remaining_list, output_file)

def open_list():
    filename = filedialog.askopenfilename(
        initialdir=".\data",
        title="Open File",
        filetypes=(
            ("Dat Files", "*.dat"), ("All Files", "*.*")
        )
    )
    if filename:
        #delete current open list
        app_list_box.delete(0, END)

        input_file = open(filename, 'rb')
        to_do_list = pickle.load(input_file)
        for item in to_do_list:
            app_list_box.insert(END, item)

def clear_list():
    app_list_box.delete(0, END)

#Create Menu
menu_box = Menu(app)
app.config(menu=menu_box)

#Add items to the menu
file_menu = Menu(menu_box, tearoff=False)
menu_box.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="Save List", command=save_list)
file_menu.add_command(label="Open List", command=open_list)
file_menu.add_separator() #for adding the line separator
file_menu.add_command(label="Clear List", command=clear_list)
file_menu.add_separator()
file_menu.add_command(label="Quit", command=app.destroy)

#buttons
button_delete = Button(button_frame, text="Delete", fg="#060606", bg="#878383", command=delete)
button_add = Button(button_frame, text="Add", fg="#060606", bg="#878383", command=add)
button_cross_off = Button(button_frame, text="Cross Off", fg="#060606", bg="#878383", command=cross_off)
button_uncross = Button(button_frame, text="Uncross", fg="#060606", bg="#878383", command=uncross_off)
button_delete_cross_off = Button(button_frame, text="Delete Crossed Off", fg="#060606", bg="#878383", command=delete_cross_off)

#button positions
button_delete.grid(row=0, column=0)
button_add.grid(row=0, column=1, padx=10)
button_cross_off.grid(row=0, column=2)
button_uncross.grid(row=0, column=3, padx=10)
button_delete_cross_off.grid(row=0, column=4)

#app holder
app.mainloop()
