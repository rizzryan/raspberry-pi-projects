from sense_hat import SenseHat 

sense = SenseHat()

while True:
	acceleration = sense.get_accelerometer_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x = round(x, 0)
	y = round(y, 0)
	z = round(z, 0)

	message = "X-axis orientation: {0}, Y-axis orientation: {1}, Z-axis orientation: {2}".format(x, y, z)
	sense.show_message(message, scroll_speed = 0.05)
