import subprocess
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def open_file():
    file = filedialog.askopenfile(parent=master,mode="rb",title="Select a file")
    if file != None:
        content = file.read()
        text.insert("1.0",content)
        file.close()

def save():
    file = filedialog.asksaveasfile(mode="w")
    if file != None:
        data = text.get("1.0", END)
        file.write(data)
        file.close()

def abort_app():
    master.destroy()

def button_callback():
    data = text.get("1.0", END)
    for line in data.splitlines():
        log = subprocess.check_output(line, shell=True)
        output.insert(END,log)
        output.insert(END,"\n \n")
        output.see(END)

    output.insert(END, "\n----------------------------------------------\n")
    # log = subprocess.check_output(data, shell=True)
    # output.insert(END,log)
    # output.insert(END, "\n----------------------------------------------\n")
    # output.see(END)


master = Tk()
master.title("Batch commands")
master.geometry('800x483')
master.resizable(True, False)

text_scroll = Scrollbar(master)
text_scroll.pack(side = RIGHT, fill=Y)

# out_scroll = Scrollbar(master)
# out_scroll.pack(side = RIGHT)

text = Text(master, height=15, yscrollcommand = text_scroll.set)
text.pack(side = TOP, fill = X)
text_scroll.config(command = text.yview )

output = Text(master, height=13, background = '#DDD')
output.pack(side = TOP, fill = X)


button = Button(master, text ="Run", command = button_callback)
button.pack(fill=X)

menu = Menu(master, tearoff=0)
master.config(menu=menu)

FileMenu = Menu(menu, tearoff = 0)
FileMenu.add_command(label="Open File", command=open_file)
FileMenu.add_command(label="Save As", command=save)
FileMenu.add_separator()
FileMenu.add_command(label="Exit", command=abort_app)
menu.add_cascade(label="File", menu=FileMenu)

master.mainloop()