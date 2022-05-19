# pip install pyperclip


from tkinter import *
import random , string

root = Tk()
root.geometry("400x200")
root.resizable(0,0)
root.title("Data flair - Password Generator")
root.config(bg ='light grey')

Label(root, text = "PASSWORD GENERATOR" , bg = 'pink', font = 'arial 15 bold').pack()

pass_label = Label(root, text = "PASSWORD LENGTH", font = 'arial 10 bold').pack()
pass_len = IntVar()
length = Spinbox(root, from_ = 8, to_ = 32, textvariable = pass_len , bg = 'light blue', width = 15).pack()

pass_str = StringVar()

def Generator():
    password = ''
    for x in range(0,4):
        Password = random.choice(string.ascii_uppercase)+ random.choice(string.ascii_lowercase) 
        random.choice(string.digits) + random.choice(string.punctuation)
        random.choice(string.digits) + random.choice(string.punctuation)
    for y in range(pass_len.get()-4):
        password = password + random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Button(root, text = "GENERATE PASSWORD", bg = 'red',  command = Generator).pack(pady = 5)
Entry(root, bg = 'light green', textvariable = pass_str).pack()

root.mainloop()