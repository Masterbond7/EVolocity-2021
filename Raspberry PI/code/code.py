# Importing Libs
import json
from datetime import datetime
from flask import Flask, render_template, Response, send_file
import cv2
from threading import Thread


# Initializing Functions
def updateMovementController():
    print("MVMNT|{steer},{accel},{brake}".format(steer=usr_wheel, accel=usr_accel, brake=usr_brake))
def runFlask():
    app.run(host='0.0.0.0', debug=False, threaded=True)

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
           "Steering wheel position: "+str(usr_wheel)+"<br>"+                \
           "Throttle position: "+str(usr_accel)+"<br>"+                      \
           "Brake position: "+str(usr_brake)
           
    ##return open("save_data.txt", 'r').read()

@app.route("/gps_coords")
def gps_coords():
    return str(aux_gps_lon)+","+str(aux_gps_lat)  ##open("gps.txt", 'r').read()


# Initializing Variables
ard_input = "|"
started_datetime = datetime.now()

# AI Camera
steering_correction = 0

# Distance Sensors
distance_value = 0

# Switch Board
cart_on = 0
cart_auto = 0
cart_mode = 1 # 0 = Auto, 1 = Sport, 2 = Economy
cart_mode_txt = "SPORT"

# Gearbox Controller
rpm_motor = 0
rpm_cvt_out = 0
rpm_clutch_out = 0

# Aux Sensors
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

# User Inputs
usr_wheel = 0
usr_accel = 0
usr_brake = 0


# Starting Flask
flaskThread = Thread(target=runFlask)
flaskThread.start()


# Main Loop
while True:
    # Main Code Loop
    try:
        # Handle Arduino Input
        dissected_ard_input = ard_input.split("|")
        dissected_vars = dissected_ard_input[1].split(",")

        # AI Camera
        if dissected_ard_input[0] == "AIC":
            steering_correction = int(dissected_vars[0])
            
        # Distance Sensors
        if dissected_ard_input[0] == "DIST":
            distance_value = int(dissected_vars[0])

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
            rpm_motor = int(dissected_vars[0])
            rpm_cvt_out = int(dissected_vars[1])
            rpm_clutch_out = int(dissected_vars[2])

        # Aux Sensors
        if dissected_ard_input[0] == "AUX":
            aux_temp_motor = int(dissected_vars[0])
            aux_temp_bat_1 = int(dissected_vars[1])
            aux_temp_bat_2 = int(dissected_vars[2])
            aux_temp_fuse = int(dissected_vars[3])
            aux_temp_motor_cont = int(dissected_vars[4])
            aux_temp_brake_FL = int(dissected_vars[5])
            aux_temp_brake_FR = int(dissected_vars[6])
            aux_temp_brake_BL = int(dissected_vars[7])
            aux_temp_brake_BR = int(dissected_vars[8])
            aux_temp_rpi = int(dissected_vars[9])
            aux_cur_bat = int(dissected_vars[10])
            aux_gps_lon = int(dissected_vars[11])
            aux_gps_lat = int(dissected_vars[12])
            aux_g_force_x = int(dissected_vars[13])
            aux_g_force_y = int(dissected_vars[14])
            aux_g_force_z = int(dissected_vars[15])

        # User Inputs
        if dissected_ard_input[0] == "USR":
            usr_wheel = int(dissected_vars[0])
            usr_accel = int(dissected_vars[1])
            usr_brake = int(dissected_vars[2])
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
        log_file.write(str(usr_wheel)+",")
        log_file.write(str(usr_accel)+",")
        log_file.write(str(usr_brake)+"\n")
        log_file.close()
        
        
        # Reset Arduino Input Variable
        ard_input = "|"


    # Code for console input
    except:
        ard_input = input("SERIAL_INPUT: ")
