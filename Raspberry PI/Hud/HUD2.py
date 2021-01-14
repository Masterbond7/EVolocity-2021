from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.title('Car Stats')
root.geometry("800x480")
root.configure(background='black')

#my_img = ImageTk.PhotoImage(Image.open("engine.jpg"))
#my_label = Label(image=my_img, bg="black")
#my_label.place(rely=1.0, relx=1.0, x=0, y=0, anchor=SE)

speed = Label(root, text="Speed: ", font=("Helvetica", 18))
speed.place(x = 660, y = 150)

engine = ImageTk.PhotoImage(Image.open("weewoo.jpg"))
engineLabel = Label(image=engine, bg="black")
engineLabel.place(x = 650, y = 20)

green = ImageTk.PhotoImage(Image.open("fire.png"))
greenLabel = Label(image=green, bg="black")
greenLabel.place(x = 650,y = 350)

def something():
    imgValue = random.randint(0,1)
    speedValue = random.randint(1, 10)
    modeValue = random.randint(1, 6)
    speed.config(fg = "white", bg = "black", text="Speed:\n" + str(speedValue) + "\nMode:\n" + str(modeValue) + ("\nBattery:\n63%"))
    
        

    root.after(100, something) 




#my_button = Button(root, text="Click Me", command=something)
#my_button.pack(pady=10)

something()

#def task():
    







root.mainloop()

