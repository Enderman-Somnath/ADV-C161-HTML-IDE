#Linking
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from tkinter import filedialog
import os
root = Tk()

#Configuring Window
root.geometry("1280x768")
root.title("Notepad")
root.configure(background="yellow")

exit1 = ImageTk.PhotoImage(Image.open("exit.png"))
open1 = ImageTk.PhotoImage(Image.open("open.png"))
savefile = ImageTk.PhotoImage(Image.open("save.png"))

label1filename = Label(root,text="File Name",fg="white",bg="#333",bd=0)
label1filename.place(relx=0.4,rely=0.1,anchor=CENTER)
input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.1,anchor=CENTER)
my_text = Text(root)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)

name = ""
my_text = Text(root,height=35,width=80)
my_text.place(relx=0.5,rely=0.5,anchor=CENTER)
#Functions
def opentxt():
    global name
    my_text.delete(1.0,END)
    input_file_name.delete(0,END)
    text_file = filedialog.askopenfilename(title="Open Text File",
                                           filetypes=(("Text Files","*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formatted_name = name.split('.')[0]
    input_file_name.insert(END,formatted_name)
    root.title(formatted_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    my_text.insert(END,paragraph)
    text_file.close()
#Buttons
OpenButton = Button(root,image=open1,command=opentxt)
OpenButton.place(rely=0.1,relx=0.1,anchor=CENTER)
SaveButton = Button(root,image=savefile)
SaveButton.place(rely=0.1,relx=0.2,anchor=CENTER)
ExitButton = Button(root,image=exit1)
ExitButton.place(rely=0.1,relx=0.3,anchor=CENTER)
root.mainloop()
