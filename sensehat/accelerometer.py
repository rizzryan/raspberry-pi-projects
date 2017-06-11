from sense_hat import SenseHat 

sense = SenseHat()

while True:
	acceleration = sense.get_acceleration_raw()
	x = acceleration['x']
	y = acceleration['y']
	z = acceleration['z']

	x = round(x, 0)
	y = round(y, 0)
	z = round(z, 0)

	sense.show_message("X-axis orientation: {0}, Y-axis orientation: {1}, Z-axis orientation: {2}", scroll_speed = 0.05).format(x, y, z)