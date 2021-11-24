import smbus
import time
bus = smbus.SMBus(1)

num = 0
op = 3

errors = 0

while True:
	try:
		bus.write_byte(0x12, num)
		num += op
		if num == 256 - (256%op): op *= -1
		if num == 0: op *= -1
		time.sleep(10/1000)
		print("Errors: {0}, Angle: {1}".format(errors, num))
	except Exception as e:
		print(e)
		errors+=1
