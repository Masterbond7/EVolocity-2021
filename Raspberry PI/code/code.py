# Initializing Variables
ard_input = "|"

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
        
        
        # Reset Arduino Input Variable
        ard_input = "|"


    # Code for console input
    except:
        ard_input = input("SERIAL_INPUT: ")
