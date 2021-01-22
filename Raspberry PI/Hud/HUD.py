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

weewoo = ImageTk.PhotoImage(Image.open("weewoo.jpg"))
weewooLabel = Label(image=weewoo, bg="black")
weewooLabel.place(x = 650, y = 20)

fire = ImageTk.PhotoImage(Image.open("fire.png"))
fireLabel = Label(image=fire, bg="black")
fireLabel.place(x = 650,y = 350)

gmap = ImageTk.PhotoImage(Image.open("map.png"))
gmapLabel = Label(image=gmap, bg="black")
gmapLabel.place(x = 0,y = 0)

def something():
    imgValue = random.randint(0,1)
    speedValue = random.randint(1, 10)
    modeValue = random.randint(1, 6)
    speed.config(fg = "white", bg = "black", text="Speed:\n" + str(speedValue) + "\nMode:\n" + str(modeValue) + ("\nBattery:\n63%"))

    #map
    #if imgValue == 0:
        #gmap2 = ImageTk.PhotoImage(Image.open("fire.png"))
        #gmapLabel.configure(image=gmap2)
        #gmapLabel.image = gmap2
    #elif imgValue == 1:
        #gmap2 = ImageTk.PhotoImage(Image.open("map.png"))
        #gmapLabel.configure(image=gmap2)
        #gmapLabel.image = gmap2

    #fire
    if imgValue == 0:
        fire2 = ImageTk.PhotoImage(Image.open("fire.png"))
        fireLabel.configure(image=fire2)
        fireLabel.image = fire2
    elif imgValue == 1:
        fire2 = ImageTk.PhotoImage(Image.open("fire2.png"))
        fireLabel.configure(image=fire2)
        fireLabel.image = fire2

    #weewoo
    if imgValue == 0:
        weewoo2 = ImageTk.PhotoImage(Image.open("weewoo.jpg"))
        weewooLabel.configure(image=weewoo2)
        weewooLabel.image = weewoo2
    elif imgValue == 1:
        weewoo2 = ImageTk.PhotoImage(Image.open("weewoo2.jpg"))
        weewooLabel.configure(image=weewoo2)
        weewooLabel.image = weewoo2

    root.after(1000, something) 




#my_button = Button(root, text="Click Me", command=something)
#my_button.pack(pady=10)

something()

#def task():
    







root.mainloop()

