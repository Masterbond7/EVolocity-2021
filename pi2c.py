import smbus
import time
import threading
import subprocess

bus = smbus.SMBus(1)
address = 0x11
pre_data = -1
pre_data_brk = -1
trans_amm = 0

def engine_effect():
	engineSound = subprocess.Popen(['play', '-q', 'v8.mp3']) # Starts engine sound effect
	time.sleep(2)

while True:
	# Steering wheel
	try:
		steering_data = bus.read_i2c_block_data(0x11, 0x0B, 3) # Steering, 0x0B, 3 bytes
		button_bytes = ((steering_data[2]<<8)+steering_data[1]) #.to_bytes(2, byteorder="big")
		buttons_pushed = []

		# Convert button bytes to buttons
		if button_bytes >= 8192: button_bytes -= 8192; buttons_pushed.append("X-Box button"); engine_effect() # NOTE: max has silly sleep statement in this function
		if button_bytes >= 4096: button_bytes -= 4096; buttons_pushed.append("Right Paddle")
		if button_bytes >= 2048: button_bytes -= 2048; buttons_pushed.append("Left Paddle")
		if button_bytes >= 1024: button_bytes -= 1024; buttons_pushed.append("Y")
		if button_bytes >= 512: button_bytes -= 512; buttons_pushed.append("X")
		if button_bytes >= 256: button_bytes -= 256; buttons_pushed.append("A")
		if button_bytes >= 128: button_bytes -= 128; buttons_pushed.append("B")
		if button_bytes >= 64: button_bytes -= 64; buttons_pushed.append("UNDEFINED 3")
		if button_bytes >= 32: button_bytes -= 32; buttons_pushed.append("UNDEFINED 2")
		if button_bytes >= 16: button_bytes -= 16; buttons_pushed.append("UNDEFINED 1")
		if button_bytes >= 8: button_bytes -= 8; buttons_pushed.append("D-Pad Down")
		if button_bytes >= 4: button_bytes -= 4; buttons_pushed.append("D-Pad Right")
		if button_bytes >= 2: button_bytes -= 2; buttons_pushed.append("D-Pad Left")
		if button_bytes >= 1: button_bytes -= 1; buttons_pushed.append("D-Pad Up")

		buttons_pushed = ", ".join(buttons_pushed)
		angle=int(steering_data[0]/(256/90)*-1)+45
		if angle == -44: continue
		angle-=1 #maybe

		print("Steering angle: {0}, Buttons pushed: {1}, Signals Transmitted: {2}".format((angle), buttons_pushed, trans_amm), end=" ") #steer,button1,button2))
		#time.sleep(1/25)
		#time.sleep(50/1000)
		#time.sleep(35/1000)

		if (not pre_data == steering_data[0]) and (not int(int(pre_data)*(180/256)) == int(int(steering_data[0])*(180/256))) and (int(steering_data[0]>=0) and int(steering_data[0]<=180)): 
			bus.write_byte(0x12,int(int(steering_data[0])*(180/256))) # Steering servo
			trans_amm += 1
		pre_data = steering_data[0]

	except Exception as e:
		print("Oh no, anyway.");time.sleep(0.05)
		print(e)
	
	# Pedals
	try:
		pedal_data = bus.read_i2c_block_data(0x13, 0x0B, 3)
		print("Accelerator: {0}, Brake: {1}, Handbrake: {2}".format(pedal_data[0], pedal_data[1], pedal_data[2]))
		time.sleep(35/1000)

		if (not pre_data_brk == pedal_data[1]) and (not int(int(pre_data_brk)*(180/256)) == int(int(pedal_data[1])*(180/256))):
			#bus.write_byte(0x14,180-int(int(pedal_data[0])*(180/256))) # accelerator
			bus.write_byte(0x14,int(int(pedal_data[1])*(180/256)))
	except:
		print("Cock pedals");time.sleep(0.05)

	try:
		# Kills the engine sound effect if the accelerator is pressed
		if pedal_data[0] >= 5:
			try:
				engineSound.kill()
			except:
				pass
	except: pass
