from tkinter import *

import calendar

# Function to Show calendar at given Year
def showCal():
    # Creating a Gui Window
    new_gui = Tk()

    # Setting The Background Color
    new_gui.config(bg = 'white')

    # Setting The Name
    new_gui.title("Tanish's Calendar")

    # Setting The Configuration
    new_gui.geometry("510x610")

    # Get Method returns Current Text as String
    fetch_year = int(year_field.get())

    # This Will return The Calendar of the given Year
    cal_content = calendar.calendar(fetch_year)

    # Creating label for Showing Content
    cal_year = Label(new_gui, text = cal_content ,fg = 'red', font = 'calibri 12 bold') 

    # Setting The Widgets In Grid
    cal_year.grid() 

    # Start The Gui
    new_gui.mainloop()

if __name__ == '__main__':
     # Create a GUI window
    gui = Tk()
     
    # Set the background colour of GUI window
    gui.config(background = "black")
 
    # set the name of tkinter GUI window
    gui.title("CALENDAR")
 
    # Set the configuration of GUI window
    gui.geometry("445x250")

    # Creating A Label
    cal = Label(gui, text = 'CALEDNAR',bg = 'dark gray',font = ('times' ,50 ,'bold')) 

    # Create a Enter Year : label
    year = Label(gui, text = "Enter Year", bg = "light green" , font = 'Arial 15 bold')

    # Create a text entry box for filling or typing the information. 
    year_field = Entry(gui)

    # Create a Show Calendar Button and attached to showCal function
    Show = Button(gui, text = "Show Calendar", fg = "white",bg = "violet", command = showCal,font = 'Arial 12 bold') 
    
    # Create a Exit Button and attached to exit function
    Exit = Button(gui, text = "Exit", fg = "white", bg = "violet", command = exit,font = 'arial 14 bold')

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure.
    cal.grid(padx = 35 , pady = 0)
 
    year.grid(padx = 45 , pady = 8)
 
    year_field.grid(padx = 0, pady = 0)
 
    Show.grid(padx = 40, pady = 10)
 
    Exit.grid(padx = 40, pady = 0)
     
    # start the GUI
    gui.mainloop()
