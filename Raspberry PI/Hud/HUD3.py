from tkinter import *
import random
from PIL import ImageTk, Image

#1#
def hud1():
    root = Tk()
    root.title('Car Stats')
    root.geometry("800x480")
    root.attributes('-fullscreen', True)
    root.configure(background='black')
    
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

    kil = Button(root, text="Switch", bg = "white", command=root.destroy)
    kil.place(x = 10, y = 400)
    kil.config(height = 4, width = 10)

    def something():
        imgValue = random.randint(0,1)
        speedValue = random.randint(1, 10)
        modeValue = random.randint(1, 6)
        speed.config(fg = "white", bg = "black", text="Speed:\n" + str(speedValue) + "\nMode:\n" + str(modeValue) + ("\nBattery:\n63%"))

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
            weewoo = ImageTk.PhotoImage(Image.open("weewoo.jpg"))
            weewooLabel.configure(image=weewoo)
            weewooLabel.image = weewoo
        elif imgValue == 1:
            weewoo2 = ImageTk.PhotoImage(Image.open("weewoo2.jpg"))
            weewooLabel.configure(image=weewoo2)
            weewooLabel.image = weewoo2

        root.after(1000, something) 

    something()
    
    root.mainloop()
    
#2#
def hud2():
    root = Tk()
    root.title('Car Stats')
    root.geometry("800x480")
    root.attributes('-fullscreen', True)
    root.configure(background='black')
    
    stats = Label(root, fg = "white", bg = "black", text="Speed: ", justify=LEFT, font=("Helvetica", 14))
    stats.place(x = 10 , y = 100)

    stats2 = Label(root, fg = "white", bg = "black", text="Speed: ", justify=LEFT, font=("Helvetica", 14))
    stats2.place(x = 280, y = 100)

    stats3 = Label(root, fg = "white", bg = "black", text="Speed: ", justify=LEFT, font=("Helvetica", 14))
    stats3.place(x = 550, y = 100)

    kil = Button(root, text="Switch", bg = "white", command=root.destroy)
    kil.place(x = 10, y = 400)
    kil.config(height = 4, width = 10)

    #####

    steering_correction=0 #
    distance_value=0 #
    cart_on=0 #
    cart_auto=0
    cart_mode=0 #
    rpm_motor=0 #
    rpm_cvt_out=0
    rpm_clutch_out=0
    aux_temp_motor=0#
    aux_temp_bat_1=0#
    aux_temp_bat_2=0#
    aux_temp_fuse=0#
    aux_temp_motor_cont=0#
    aux_temp_brake_FL=0#
    aux_temp_brake_FR=0#
    aux_temp_brake_BL=0#
    aux_temp_brake_BR=0#
    aux_temp_rpi=0#
    aux_cur_bat=0
    aux_gps_lon=0#
    aux_gps_lat=0#
    aux_g_force_x=0
    aux_g_force_y=0
    aux_g_force_z=0
    usr_wheel=0
    usr_accel=0#
    usr_brake=0

    #####


    def something2():
        stats.config(fg = "white", bg = "black",
        text="--------------Driving--------------"
        + "\nSpeed: " + str(usr_accel)
        + "\nPower: " + str(cart_on)
        + "\nMode: " + str(cart_mode)
        + "\nBattery: " + "1" + "%"
        + "\nRPM: " + str(rpm_motor)
        + "\nSteering Correction: " + str(steering_correction)
        + "\nDistance Value: " + str(distance_value)
        
        
        #+ "\n: " + str()
        #+ "\n: " + str()
        #+ "\n: " + str()

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
        

    something()




















    root.mainloop()

    #2#
while True:
    hud1()

    hud2()

#it works dont juge me
