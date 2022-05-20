from tkinter import *
import base64

# Initialize Window
root = Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Data Flair - Decode and Encode Message")

Label(root , text = "Encode Decode" , font = "arial 20 bold").pack()
Label(root , text = "Data Flair" , font = "arial 20 bold").pack(side = BOTTOM)

# Define Variables
Text = StringVar()
private_key = StringVar()  #private_key variable store the private key used to encode and decode
mode = StringVar()  # mode is used to select that is either encoding or decoding
Result = StringVar()  # Store the Result

# Function To Encode
def Encode(key , message):
    enc = []

    for i in range(len(message)):
        key_c = key[i % len(key)]
        enc.append(chr((ord(message[i]) + ord(key_c)) % 256))   
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Functions To Decode
def Decode(key , message):
    dec = []
    message = base64.urlsafe_b64decode(message).decode()

    for i in range(len(message)):
        key_c = key[i % len(key)]
        dec.append(chr((256 + ord(message[i]) - ord(key_c)) % 256))
    return "".join(dec)

# Functions to Set Mode
def Mode():
    if(mode.get() == 'e'):
        Result.set(Encode(private_key.get(), Text.get()))
    elif(mode.get() == 'd'):
        Result.set(Decode(private_key.get(), Text.get()))
    else:
        Result.set('Invalid Mode')

# Functions to Exit Window
def Exit():
    root.destroy()

# Function to Reset Window
def Reset():
    Text.set("")
    private_key.set("")
    mode.set("")
    Result.set("")

# Labels And Buttons
Label(root, font = "arial 12 bold" , text = "MESSAGE").place(x = 60 , y = 60)
Entry(root, font = "arial 10" , textvariable = Text, bg = 'ghost white').place(x = 290 , y = 60)  # Entry() = used  to create an input text field

Label(root, font = "arial 12 bold" , text = "KEY").place(x = 60 , y = 90)
Entry(root, font = "arial 10" , textvariable = private_key, bg = 'ghost white').place(x = 290 , y = 90)

Label(root, font = "arial 12 bold" , text = "MODE(e - Encode , d - Decode").place(x = 60 , y = 120)
Entry(root, font = "arial 10" , textvariable = mode, bg = 'ghost white').place(x = 290 , y = 120)
Entry(root, font = "arial 10" , textvariable = Result, bg = 'ghost white').place(x = 290 , y = 150)

Button(root, font = 'arial 10 bold', text = "RESULT", padx = 2, bg = "Light Gray", command = Mode).place(x = 60 , y = 150)
Button(root, font = 'arial 10 bold', text = "RESET",width = 6,  padx = 2, bg = "LimeGreen", command = Reset).place(x = 80 , y = 190)
Button(root, font = 'arial 10 bold', text = "EXIT", padx = 2,pady = 2, width = 6,  bg = "OrangeRed", command = Mode).place(x = 180 , y = 190)

root.mainloop()


