import smbus
import time
import threading
import subprocess

bus = smbus.SMBus(1)
address = 0x11
pre_data = -1
pre_data_brk = -1
trans_amm = 0

engineSound = subprocess.Popen(['play', 'v8.mp3'])

while True:

	# Pedals
	try:
		pedal_data = bus.read_i2c_block_data(0x13, 0x0B, 3)
		#print("Accelerator: {0}, Brake: {1}, Handbrake: {2}".format(pedal_data[0], pedal_data[1], pedal_data[2]))
		time.sleep(35/1000)

		if (not pre_data_brk == pedal_data[1]) and (not int(int(pre_data_brk)*(180/256)) == int(int(pedal_data[1])*(180/256))):
			bus.write_byte(0x14,int(int(pedal_data[1])*(180/256)))
	except:
		print("Cock pedals");time.sleep(0.05)

	# Checks if the sound effect is playing then kills it if the accelerator is pressed
	try:
		poll = engineSound.poll()
	except:
		print("Pedal check had an unhappy")

	print(pedal_data[0])

	if pedal_data[0] >= 5:
		try:
			engineSound.kill()
			print("\"Succesful kill\"")
		except:
			print("Pedal kill had an unhappy")

	time.sleep(2)

	try:
		engineSound.kill()
	except:
		print("WHY WONT YOU DIE?")