from tkinter import *
import random
from PIL import ImageTk, Image

root = Tk()
root.title('Car Stats')
root.geometry("800x480")
root.configure(background='black')


stats = Label(root, fg = "white", bg = "black", text="Speed: ", font=("Helvetica", 18))
stats.pack(side = LEFT)

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
aux_temp_bat_1=0
aux_temp_bat_2=0
aux_temp_fuse=0
aux_temp_motor_cont=0
aux_temp_brake_FL=0
aux_temp_brake_FR=0
aux_temp_brake_BL=0
aux_temp_brake_BR=0
aux_temp_rpi=0
aux_cur_bat=0
aux_gps_lon=0
aux_gps_lat=0
aux_g_force_x=0
aux_g_force_y=0
aux_g_force_z=0
usr_wheel=0
usr_accel=0 #
usr_brake=0

#####


def something():
    stats.config(fg = "white", bg = "black",
    text="Speed: " + str(usr_accel)
    + "\nPower: " + str(cart_on)
    + "\nMode: " + str(cart_mode)
    + "\nBattery: " + "1" + "%"
    + "\nRPM: " + str(rpm_motor)
    + "\nSteering Correction: " + str(steering_correction)
    + "\nDistance Value: " + str(distance_value)
    + "\nMotor Temperature: " + str(aux_temp_motor)
    + "\nDistance Value: " + str(distance_value)

    )
    

something()




















root.mainloop()
