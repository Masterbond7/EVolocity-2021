# Importing Libs
import json
from datetime import datetime
from flask import Flask, render_template, Response, send_file
import cv2
from threading import Thread
from tkinter import *
import random
from PIL import ImageTk, Image
import gc
import os

# Initializing Variables
ard_input = "|"
wheel_circumference = 1                 # in meters
started_datetime = datetime.now()

# AI Camera
steering_correction = 0#

# Distance Sensors
distance_value = 0#

# Switch Board
cart_on = 0#
cart_auto = 0#
cart_mode = 1 # 0 = Auto, 1 = Sport, 2 = Economy
cart_mode_txt = "SPORT"

# Gearbox Controller
rpm_motor = 0
rpm_cvt_out = 0
rpm_clutch_out = 0

# Aux Sensors
aux_temp_motor = 0#
aux_temp_bat_1 = 0#
aux_temp_bat_2 = 0#
aux_temp_fuse = 0#
aux_temp_motor_cont = 0#
aux_temp_brake_FL = 0#
aux_temp_brake_FR = 0#
aux_temp_brake_BL = 0#
aux_temp_brake_BR = 0#
aux_temp_rpi = 0#
aux_cur_bat = 0
aux_gps_lon = 0#
aux_gps_lat = 0#
aux_g_force_x = 0#
aux_g_force_y = 0#
aux_g_force_z = 0#
aux_battery_voltmeter = 0

# User Inputs
usr_wheel = 0
usr_accel = 0
usr_brake = 0


# Initializing Functions
def updateMovementController():
    print("MVMNT|{steer},{accel},{brake}".format(steer=usr_wheel, accel=usr_accel, brake=usr_brake))
def runFlask():
    app.run(host='0.0.0.0', debug=False, threaded=True)
def runHud():
    while True:
        basicHud()
        detailedHud()
def close_tkinter(window):
    window.destroy()
    gc.collect()

def estimate_battery(aux_battery_voltmeter):
    return -99999
def calculate_speed(wheel_circumference, rpm):
    return ((wheel_circumference/1000)*60)*rpm

# Initializing Camera
vc = cv2.VideoCapture(0)

# Initializing Flask
app = Flask(__name__)

# Creating Flask
@app.route('/')
def index():
    return render_template("index.html")
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')
def gen():
    while True:
        rval, frame = vc.read()
        byteArray = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + byteArray + b'\r\n')

@app.route('/text_data')
def text_data():
    return "AI wheel adjustment: "+str(steering_correction)+"<br>"+          \
           "Distance from object: "+str(distance_value)+"<br>"+              \
           "Motor powered: "+str(bool(cart_on))+"<br>"+                      \
           "Autonomous driver: "+str(bool(cart_auto))+"<br>"+                \
           "Cart mode: "+cart_mode_txt+"/"+str(cart_mode)+"<br>"+            \
           "Motor RPM: "+str(rpm_motor)+"<br>"+                              \
           "Gearbox RPM: "+str(rpm_cvt_out)+"<br>"+                          \
           "Clutch RPM: "+str(rpm_clutch_out)+"<br>"+                        \
           "Motor temperature: "+str(aux_temp_motor)+"<br>"+                 \
           "Battery pack #1 temperature: "+str(aux_temp_bat_1)+"<br>"+       \
           "Battery pack #2 temperature: "+str(aux_temp_bat_2)+"<br>"+       \
           "Fuse temperature: "+str(aux_temp_fuse)+"<br>"+                   \
           "Motor controller temperature: "+str(aux_temp_motor_cont)+"<br>"+ \
           "Front-Left brake temperature: "+str(aux_temp_brake_FL)+"<br>"+   \
           "Front-Right brake temperature: "+str(aux_temp_brake_FR)+"<br>"+  \
           "Back-Left brake temperature: "+str(aux_temp_brake_BL)+"<br>"+    \
           "Back-Right brake temperature: "+str(aux_temp_brake_BR)+"<br>"+   \
           "CPU temperature: "+str(aux_temp_rpi)+"<br>"+                     \
           "Power Consumption: "+str(aux_cur_bat)+"<br>"+                    \
           "GPS Longitude: "+str(aux_gps_lon)+"<br>"+                        \
           "GPS Latitude: "+str(aux_gps_lat)+"<br>"+                         \
           "X-Axis G-Force: "+str(aux_g_force_x)+"<br>"+                     \
           "Y-Axis G-Force: "+str(aux_g_force_y)+"<br>"+                     \
           "Z-Axis G-Force: "+str(aux_g_force_z)+"<br>"+                     \
           "Battery voltage: "+str(aux_battery_voltmeter)+"<br>"+            \
           "Steering wheel position: "+str(usr_wheel)+"<br>"+                \
           "Throttle position: "+str(usr_accel)+"<br>"+                      \
           "Brake position: "+str(usr_brake)
           
    ##return open("save_data.txt", 'r').read()

@app.route("/gps_coords")
def gps_coords():
    return str(aux_gps_lon)+","+str(aux_gps_lat)  ##open("gps.txt", 'r').read()


# Creating Basic HUD
def basicHud(): 
    # Initializing Behaviours
    def basicHudUpdate():
        # Creating These Variables For Debugging Use
        temperatureCheck = random.randint(0, 1)
        engineCheck = random.randint(0, 1)

        # Updating Information On The Information Label
        infoLabel.config(fg = "white", bg = "black", text="Speed:\n{speedValue} KPH\nMode:\n{cartMode}\nBattery:\n{batteryPercentage}%".format(speedValue=cmp_cart_speed, cartMode=cart_mode_txt, batteryPercentage=cmp_battery_percentage))

        # Temperature Check Light
        if temperatureCheck == 0:
            temperatureCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/temperatureCheckFalse.png")))
            temperatureCheckLight.configure(image=temperatureCheckImage)
            temperatureCheckLight.image = temperatureCheckImage
        elif temperatureCheck == 1:
            temperatureCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/temperatureCheckTrue.png")))
            temperatureCheckLight.configure(image=temperatureCheckImage)
            temperatureCheckLight.image = temperatureCheckImage

        # Engine Check Light
        if engineCheck == 0:
            engineCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/engineCheckFalse.jpg")))
            engineCheckLight.configure(image=engineCheckImage)
            engineCheckLight.image = engineCheckImage
        elif engineCheck == 1:
            engineCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/engineCheckTrue.jpg")))
            engineCheckLight.configure(image=engineCheckImage)
            engineCheckLight.image = engineCheckImage

        # Updating Map Image
        mapImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/map.png")))
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
    infoLabel.place(x = 653, y = 150)

    # Setting Up Engine Check Light
    engineCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/engineCheckFalse.jpg")))
    engineCheckLight = Label(image=engineCheckImage, bg="black")
    engineCheckLight.place(x = 650, y = 20)

    # Setting Up Temperature Check Light
    temperatureCheckImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/temperatureCheckFalse.png")))
    temperatureCheckLight = Label(image=temperatureCheckImage, bg="black")
    temperatureCheckLight.place(x = 650,y = 350)

    # Setting Up Map Image
    mapImage = ImageTk.PhotoImage(Image.open(os.path.join(os.getcwd(), "hudImages/map.png")))
    mapLabel = Label(image=mapImage, bg="black")
    mapLabel.place(x=0, y=0)

    # Creating Button To Swap HUD Mode
    hudSwap = Button(basicHudWindow, text="Switch", bg = "white", command=lambda: close_tkinter(basicHudWindow))
    hudSwap.place(x = 10, y = 400)
    hudSwap.config(height = 4, width = 10)

    # Starting The Update Loop For This HUD Window
    basicHudUpdate()

    # Starting The Main Loop For This HUD Window
    basicHudWindow.mainloop()


# Creating More Detailed HUD
def detailedHud():
    # Initializing Behaviours
    def detailedHudUpdate():
        stats.config(fg = "white", bg = "black",
        text="--------------Driving--------------"
        + "\nSpeed: " + str(cmp_cart_speed)
        + "\nPower: " + str(cart_on)
        + "\nMode: " + str(cart_mode)
        + "\nBattery: " + str(cmp_battery_percentage) + "%"
        + "\nClutch RPM: " + str(rpm_clutch_out)
        + "\nMotor RPM: " + str(rpm_motor)
        + "\nGearbox RPM: " + str(rpm_cvt_out)
        + "\nSteering Correction: " + str(steering_correction)
        + "\nDistance Value: " + str(distance_value)
        + "\n\n---------------------------------------"
        )

        stats2.config(fg = "white", bg = "black",
        text="----------Temperature----------"
        + "\nMotor Temp: " + str(aux_temp_motor)
        + "\nBattery 1 Temp: " + str(aux_temp_bat_1)
        + "\nBattery 2 Temp: " + str(aux_temp_bat_2)
        + "\nFuse Temperature: " + str(aux_temp_fuse)
        + "\nMotor Controller Temp: " + str(aux_temp_motor_cont)
        + "\nFront-Left Brake Temp: " + str(aux_temp_brake_FL)
        + "\nFront-Right Brake Temp: " + str(aux_temp_brake_FR)
        + "\nBack-Left Brake Temp: " + str(aux_temp_brake_BL)
        + "\nBack-Right Brake Temp: " + str(aux_temp_brake_BR)
        + "\nRaspberry Pi Temp: " + str(aux_temp_rpi)
        + "\n---------------------------------------"
        )


        stats3.config(fg = "white", bg = "black",
        text="----------------Map----------------"
        + "\nLongitude :" + str(aux_gps_lon)
        + "\nLatitude: " + str(aux_gps_lat)
        + "\n---------Other Sensors---------"
        + "\nDistance Value: " + str(distance_value)
        + "\nG-Force X: " + str(aux_g_force_x)
        + "\nG-Force Y: " + str(aux_g_force_y)
        + "\nG-Force Z: " + str(aux_g_force_z)#
       	+ "\n\n\n\n---------------------------------------"
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
    hudSwap = Button(detailedHudWindow, text="Switch", bg = "white", command=lambda: close_tkinter(detailedHudWindow))
    hudSwap.place(x = 10, y = 400)
    hudSwap.config(height = 4, width = 10)

    # Starting The Update Loop For This HUD Window
    detailedHudUpdate()

    # Starting The Main Loop For This HUD Window
    detailedHudWindow.mainloop()


# Initializing Complex Variables
cmp_battery_percentage = estimate_battery(aux_battery_voltmeter)
cmp_cart_speed = calculate_speed(wheel_circumference, rpm_clutch_out)


# Starting Flask Thread
flaskThread = Thread(target=runFlask)
flaskThread.start()

# Starting HUD Thread
hudThread = Thread(target=runHud)
hudThread.start()

# Getting The Data From The Arduinos And Interpreting It
while True:
    # Main Code Loop
    try:
        # Handle Arduino Input
        dissected_ard_input = ard_input.split("|")
        dissected_vars = dissected_ard_input[1].split(",")

        # AI Camera
        if dissected_ard_input[0] == "AIC":
            steering_correction = float(dissected_vars[0])
            
        # Distance Sensors
        if dissected_ard_input[0] == "DIST":
            distance_value = float(dissected_vars[0])

        # Switch Board
        if dissected_ard_input[0] == "SWTCH":
            cart_on = int(dissected_vars[0])
            cart_auto = int(dissected_vars[1])
            cart_mode = int(dissected_vars[2])

            # Logic To Override Mode To AUTO If AUTO Switch Is Flicked (MODE OVERRIDE)
            if cart_auto == 1: cart_mode = 0
            
            # Reading Mode Data
            mode_data_file = open('mode_config.json', 'r')
            mode_data = json.load(mode_data_file)
            mode_data = mode_data["mode"]

            # Giving Gearbox New RPM Ranges And Getting Mode's name
            try:
                cart_mode_txt = mode_data[cart_mode]['modeName']
                gbox_minRPM = mode_data[cart_mode]['minRPM']
                gbox_maxRPM = mode_data[cart_mode]['maxRPM']
                print("GBOX|{newMin},{newMax}".format(newMin=gbox_minRPM, newMax=gbox_maxRPM))
            except:
                print("Invalid mode. Mode out of range")


        # Gearbox Controller
        if dissected_ard_input[0] == "GBOX":
            rpm_motor = float(dissected_vars[0])
            rpm_cvt_out = float(dissected_vars[1])
            rpm_clutch_out = float(dissected_vars[2])

        # Aux Sensors
        if dissected_ard_input[0] == "AUX":
            aux_temp_motor = float(dissected_vars[0])
            aux_temp_bat_1 = float(dissected_vars[1])
            aux_temp_bat_2 = float(dissected_vars[2])
            aux_temp_fuse = float(dissected_vars[3])
            aux_temp_motor_cont = float(dissected_vars[4])
            aux_temp_brake_FL = float(dissected_vars[5])
            aux_temp_brake_FR = float(dissected_vars[6])
            aux_temp_brake_BL = float(dissected_vars[7])
            aux_temp_brake_BR = float(dissected_vars[8])
            aux_temp_rpi = float(dissected_vars[9])
            aux_cur_bat = float(dissected_vars[10])
            aux_gps_lon = float(dissected_vars[11])
            aux_gps_lat = float(dissected_vars[12])
            aux_g_force_x = float(dissected_vars[13])
            aux_g_force_y = float(dissected_vars[14])
            aux_g_force_z = float(dissected_vars[15])
            aux_battery_voltmeter = float(dissected_vars[16])

        # User Inputs
        if dissected_ard_input[0] == "USR":
            usr_wheel = float(dissected_vars[0])
            usr_accel = float(dissected_vars[1])
            usr_brake = float(dissected_vars[2])
            updateMovementController()


        # Save Data
        log_file = open("log_file_{datetime}.txt".format(datetime=started_datetime.strftime("%d-%b-%Y-%H.%M.%S")), 'a')
        log_file.write(str(steering_correction)+",")
        log_file.write(str(distance_value)+",")
        log_file.write(str(cart_on)+",")
        log_file.write(str(cart_auto)+",")
        log_file.write(str(cart_mode)+",")
        log_file.write(str(rpm_motor)+",")
        log_file.write(str(rpm_cvt_out)+",")
        log_file.write(str(rpm_clutch_out)+",")
        log_file.write(str(aux_temp_motor)+",")
        log_file.write(str(aux_temp_bat_1)+",")
        log_file.write(str(aux_temp_bat_2)+",")
        log_file.write(str(aux_temp_fuse)+",")
        log_file.write(str(aux_temp_motor_cont)+",")
        log_file.write(str(aux_temp_brake_FL)+",")
        log_file.write(str(aux_temp_brake_FR)+",")
        log_file.write(str(aux_temp_brake_BL)+",")
        log_file.write(str(aux_temp_brake_BR)+",")
        log_file.write(str(aux_temp_rpi)+",")
        log_file.write(str(aux_cur_bat)+",")
        log_file.write(str(aux_gps_lon)+",")
        log_file.write(str(aux_gps_lat)+",")
        log_file.write(str(aux_g_force_x)+",")
        log_file.write(str(aux_g_force_y)+",")
        log_file.write(str(aux_g_force_z)+",")
        log_file.write(str(aux_battery_voltmeter)+",")
        log_file.write(str(usr_wheel)+",")
        log_file.write(str(usr_accel)+",")
        log_file.write(str(usr_brake)+"\n")
        log_file.close()
        
        
        # Reset Arduino Input Variable
        ard_input = "|"


    # Code for console input
    except:
        ard_input = input("SERIAL_INPUT: ")
