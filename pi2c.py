import smbus
import time

bus = smbus.SMBus(1)
address = 0x11

while True:
	data = bus.read_i2c_block_data(address, 0x99, 3)
	button_bytes = ((data[2]<<8)+data[1]) #.to_bytes(2, byteorder="big")
	buttons_pushed = []

	# Convert button bytes to buttons
	if button_bytes >= 8192: button_bytes -= 8192; buttons_pushed.append("X-Box button")
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
	angle=int(data[0]/(256/90)*-1)+45
	if angle == -44: continue
	#angle-=1 #maybe

	print("Steering angle: {0}, Buttons pushed: {1}".format((angle), buttons_pushed)) #steer,button1,button2))
	time.sleep(1/60)
