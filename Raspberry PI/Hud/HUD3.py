# Importing Libs
from tkinter import *
import random
from PIL import ImageTk, Image

# Initializing Variables
steering_correction = 0
distance_value = 0
cart_on = 0
cart_auto = 0
cart_mode = 0
rpm_motor = 0
rpm_cvt_out = 0
rpm_clutch_out = 0
aux_temp_motor = 0
aux_temp_bat_1 = 0
aux_temp_bat_2 = 0
aux_temp_fuse = 0
aux_temp_motor_cont = 0
aux_temp_brake_FL = 0
aux_temp_brake_FR = 0
aux_temp_brake_BL = 0
aux_temp_brake_BR = 0
aux_temp_rpi = 0
aux_cur_bat = 0
aux_gps_lon = 0
aux_gps_lat = 0
aux_g_force_x = 0
aux_g_force_y = 0
aux_g_force_z = 0
usr_wheel = 0
usr_accel = 0
usr_brake = 0


# Basic HUD
def basicHud(): 
    # Initializing Behaviours
    def basicHudUpdate():
        # Creating These Variables For Debugging Use
        temperatureCheck = random.randint(0, 1)
        engineCheck = random.randint(0, 1)
        
        cart_mode = random.randint(0, 2)
        cart_speed = random.randint(0, 50)
        battery_percentage = random.randint(0,100)

        # Updating Information On The Information Label
        infoLabel.config(fg = "white", bg = "black", text="Speed:\n{speedValue} KPH\nMode:\n{cartMode}\nBattery:\n{batteryPercentage}%".format(speedValue=cart_speed, cartMode=cart_mode, batteryPercentage=battery_percentage))

        # Temperature Check Light
        if temperatureCheck == 0:
            temperatureCheckImage = ImageTk.PhotoImage(Image.open("temperatureCheckFalse.png"))
            temperatureCheckLight.configure(image=temperatureCheckImage)
            temperatureCheckLight.image = temperatureCheckImage
        elif temperatureCheck == 1:
            temperatureCheckImage = ImageTk.PhotoImage(Image.open("temperatureCheckTrue.png"))
            temperatureCheckLight.configure(image=temperatureCheckImage)
            temperatureCheckLight.image = temperatureCheckImage

        # Engine Check Light
        if engineCheck == 0:
            engineCheckImage = ImageTk.PhotoImage(Image.open("engineCheckFalse.jpg"))
            engineCheckLight.configure(image=engineCheckImage)
            engineCheckLight.image = engineCheckImage
        elif engineCheck == 1:
            engineCheckImage = ImageTk.PhotoImage(Image.open("engineCheckTrue.jpg"))
            engineCheckLight.configure(image=engineCheckImage)
            engineCheckLight.image = engineCheckImage

        # Updating Map Image
        mapImage = ImageTk.PhotoImage(Image.open("map.png"))
        mapLabel.configure(image=mapImage)
        mapLabel.image=mapImage

        # Re-Calling This Function To Form A Infinate Update Loop
        basicHudWindow.after(1000, basicHudUpdate) 

    
    # Initializing Window
    basicHudWindow = Tk()
    basicHudWindow.geometry("800x480")
    basicHudWindow.attributes('-fullscreen', True)
    basicHudWindow.configure(background='black')

    # Setting Up Information Label
    infoLabel = Label(basicHudWindow, text="Speed: ", font=("Helvetica", 18))
    infoLabel.place(x = 660, y = 150)

    # Setting Up Engine Check Light
    engineCheckImage = ImageTk.PhotoImage(Image.open("engineCheckFalse.jpg"))
    engineCheckLight = Label(image=engineCheckImage, bg="black")
    engineCheckLight.place(x = 650, y = 20)

    # Setting Up Temperature Check Light
    temperatureCheckImage = ImageTk.PhotoImage(Image.open("temperatureCheckFalse.png"))
    temperatureCheckLight = Label(image=temperatureCheckImage, bg="black")
    temperatureCheckLight.place(x = 650,y = 350)

    # Setting Up Map Image
    mapImage = ImageTk.PhotoImage(Image.open("map.png"))
    mapLabel = Label(image=mapImage, bg="black")
    mapLabel.place(x=0, y=0)

    # Creating Button To Swap HUD Mode
    hudSwap = Button(basicHudWindow, text="Switch", bg = "white", command=basicHudWindow.destroy)
    hudSwap.place(x = 10, y = 400)
    hudSwap.config(height = 4, width = 10)

    # Starting The Update Loop For This HUD Window
    basicHudUpdate()

    # Starting The Main Loop For This HUD Window
    basicHudWindow.mainloop()


# More Detailed HUD
def detailedHud():
    # Initializing Behaviours
    def detailedHudUpdate():
        stats.config(fg = "white", bg = "black",
        text="--------------Driving--------------"
        + "\nSpeed: " + str(usr_accel)
        + "\nPower: " + str(cart_on)
        + "\nMode: " + str(cart_mode)
        + "\nBattery: " + str(random.randint(0, 100)) + "%"
        + "\nRPM: " + str(rpm_motor)
        + "\nSteering Correction: " + str(steering_correction)
        + "\nDistance Value: " + str(distance_value)
        )

        stats2.config(fg = "white", bg = "black",
        text="----------Temperature----------"
        + "\nMotor Temp: " + str(aux_temp_motor)
        + "\nBattery 1 Temp: " + str(aux_temp_bat_1)
        + "\nBattery 2 Temp: " + str(aux_temp_bat_2)
        + "\nFuse Temperature: " + str(aux_temp_fuse)
        + "\nMotor Controller Temp: " + str(aux_temp_motor_cont)
        + "\nFront Left Brake Temp: " + str(aux_temp_brake_FL)
        + "\nFront Right Brake Temp: " + str(aux_temp_brake_FR)
        + "\nBack Left Brake Temp: " + str(aux_temp_brake_BL)
        + "\nBack Right Brake Temp: " + str(aux_temp_brake_BR)
        + "\nRaspberry Pi Temp: " + str(aux_temp_rpi)
        )


        stats3.config(fg = "white", bg = "black",
        text="----------------Map----------------"
        + "\nLongitude :" + str(aux_gps_lon)
        + "\nLatitude: " + str(aux_gps_lon)
        + "\n---------Other Sensors---------"
        + "\nDistance Value: " + str(distance_value)
        )

        # Re-Calling This Function To Form A Infinate Update Loop
        detailedHudWindow.after(1000, detailedHudUpdate)
        

    # Initializing Window
    detailedHudWindow = Tk()
    detailedHudWindow.geometry("800x480")
    detailedHudWindow.attributes('-fullscreen', True)
    detailedHudWindow.configure(background='black')

    # Creating Stat Labels
    stats = Label(detailedHudWindow, fg = "white", bg = "black", text="Speed: ", justify=LEFT, font=("Helvetica", 14))
    stats.place(x = 10 , y = 100)
    stats2 = Label(detailedHudWindow, fg = "white", bg = "black", text="Speed: ", justify=LEFT, font=("Helvetica", 14))
    stats2.place(x = 280, y = 100)
    stats3 = Label(detailedHudWindow, fg = "white", bg = "black", text="Speed: ", justify=LEFT, font=("Helvetica", 14))
    stats3.place(x = 550, y = 100)

    # Creating Button To Swap HUD Mode
    hudSwap = Button(detailedHudWindow, text="Switch", bg = "white", command=detailedHudWindow.destroy)
    hudSwap.place(x = 10, y = 400)
    hudSwap.config(height = 4, width = 10)

    # Starting The Update Loop For This HUD Window
    detailedHudUpdate()

    # Starting The Main Loop For This HUD Window
    detailedHudWindow.mainloop()


# Main Program Loop To Make Sure A HUD Window Is Always Open
while True:
    basicHud()
    detailedHud()
