from tkinter import *
from turtle import speed
from PIL import ImageTk, Image
import os
import random

# Tempory placeholder values {
temp = 67
engineOk = True

speed = 0
mode = "Economy"
batteryPercentage = 62
# } Tempory placeholder values

root = Tk()
root.attributes('-fullscreen', True)
root.title('Tkinter Window Demo')

def rootUpdate():

    # Blinky test {
    temp = random.randint(59, 60)
    engineOk = random.randint(0, 1)
    # } Blinky test

    infoText =  "Speed:\n" + str(speed) + " kph"\
                "\n\nMode:\n" + str(mode) + \
                "\n\nBattery:\n" + str(batteryPercentage) + " %"
    infoLabel.config(text=infoText)

    if temp < 60:
        temperatureCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/temperatureCheckFalse.png")))
        temperatureCheckLight.configure(image=temperatureCheckImage)
        temperatureCheckLight.image = temperatureCheckImage
    else:
        temperatureCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/temperatureCheckTrue.png")))
        temperatureCheckLight.configure(image=temperatureCheckImage)
        temperatureCheckLight.image = temperatureCheckImage

    if engineOk:
        engineCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/engineCheckFalse.jpg")))
        engineCheckLight.configure(image=engineCheckImage)
        engineCheckLight.image = engineCheckImage
    else:
        engineCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/engineCheckTrue.jpg")))
        engineCheckLight.configure(image=engineCheckImage)
        engineCheckLight.image = engineCheckImage

    print("Ran check")

    root.after(100, rootUpdate)


# Window setup {
root.geometry("800x480")
root.resizable(False, False)
root.configure(background='black')
# } Window setup

infoLabel = Label(root, justify='center', fg = "white", bg = "black", font=("Helvetica", 18))
infoLabel.place(x = 645, y = 140)

engineCheckLight = Label(bg="black")
engineCheckLight.place(x = 650, y = 20)

temperatureCheckLight = Label(bg="black")
temperatureCheckLight.place(x = 650,y = 350)

mapImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/map.png")))
mapLabel = Label(image=mapImage, bg="black")
mapLabel.place(x=0, y=0)

rootUpdate()


root.mainloop()
