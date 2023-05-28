import os
from tkinter import filedialog
from tkinter import *

def rename_files(sort_by):
    for count, filename in enumerate(sorted(os.listdir(folder_selected), key=sort_by)):
        dst = name_var.get() + '_' + str(count).zfill(4) + ".png"
        src = os.path.join(folder_selected, filename)
        dst = os.path.join(folder_selected, dst)
        os.rename(src, dst)

def sort_by_name(file):
    return file

def sort_by_date(file):
    return os.path.getctime(os.path.join(folder_selected, file))

def open_folder():
    global folder_selected
    folder_selected = filedialog.askdirectory()

root = Tk()
root.geometry("400x200")

name_var = StringVar(root)
name_entry = Entry(root, textvariable=name_var)
name_entry.pack()

sort_var = StringVar(root)
sort_var.set("name")

sort_option = OptionMenu(root, sort_var, "name", "date")
sort_option.pack()

open_button = Button(root, text="Open Folder", command=open_folder)
open_button.pack()

rename_button = Button(root, text="Rename Files", command=lambda: rename_files(sort_by_name if sort_var.get() == "name" else sort_by_date))
rename_button.pack()

root.mainloop()
