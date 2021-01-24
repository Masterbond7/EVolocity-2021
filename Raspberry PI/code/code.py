# Importing Libs
import json
from datetime import datetime


# Initializing Functions
def updateMovementController():
    print("MVMNT|{steer},{accel},{brake}".format(steer=usr_wheel, accel=usr_accel, brake=usr_brake))

# Initializing Variables
ard_input = "|"
wheel_circumference = 1
started_datetime = datetime.now()

# AI Camera
steering_correction = 0

# Distance Sensors
distance_value = 0

# Switch Board
cart_on = 0
cart_auto = 0
cart_mode = 0 # 0 = Torque, 1 = Economy

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
            
            # Reading Mode Data
            mode_data_file = open('mode_config.json', 'r')
            mode_data = json.load(mode_data_file)
            mode_data = mode_data["mode"]

            # Giving Gearbox New RPM Ranges
            try:
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
        save_file = open("save_data.txt", "w")
        save_file.write("steering_correction:"+str(steering_correction)+"\n")
        save_file.write("distance_value:"+str(distance_value)+"\n")
        save_file.write("cart_on:"+str(cart_on)+"\n")
        save_file.write("cart_auto:"+str(cart_auto)+"\n")
        save_file.write("cart_mode:"+str(cart_mode)+"\n")
        save_file.write("rpm_motor:"+str(rpm_motor)+"\n")
        save_file.write("rpm_cvt_out:"+str(rpm_cvt_out)+"\n")
        save_file.write("rpm_clutch_out:"+str(rpm_clutch_out)+"\n")
        save_file.write("aux_temp_motor:"+str(aux_temp_motor)+"\n")
        save_file.write("aux_temp_bat_1:"+str(aux_temp_bat_1)+"\n")
        save_file.write("aux_temp_bat_2:"+str(aux_temp_bat_2)+"\n")
        save_file.write("aux_temp_fuse:"+str(aux_temp_fuse)+"\n")
        save_file.write("aux_temp_motor_cont:"+str(aux_temp_motor_cont)+"\n")
        save_file.write("aux_temp_brake_FL:"+str(aux_temp_brake_FL)+"\n")
        save_file.write("aux_temp_brake_FR:"+str(aux_temp_brake_FR)+"\n")
        save_file.write("aux_temp_brake_BL:"+str(aux_temp_brake_BL)+"\n")
        save_file.write("aux_temp_brake_BR:"+str(aux_temp_brake_BR)+"\n")
        save_file.write("aux_temp_rpi:"+str(aux_temp_rpi)+"\n")
        save_file.write("aux_cur_bat:"+str(aux_cur_bat)+"\n")
        save_file.write("aux_gps_lon:"+str(aux_gps_lon)+"\n")
        save_file.write("aux_gps_lat:"+str(aux_gps_lat)+"\n")
        save_file.write("aux_g_force_x:"+str(aux_g_force_x)+"\n")
        save_file.write("aux_g_force_y:"+str(aux_g_force_y)+"\n")
        save_file.write("aux_g_force_z:"+str(aux_g_force_z)+"\n")
        save_file.write("usr_wheel:"+str(usr_wheel)+"\n")
        save_file.write("usr_accel:"+str(usr_accel)+"\n")
        save_file.write("usr_brake:"+str(usr_brake)+"\n")
        save_file.close()
        
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
