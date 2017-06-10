import datetime
from sense_hat import SenseHat
sense = SenseHat()
currentDT = datetime.datetime.now()

while True:
    temp = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    date = currentDT.strftime("%m/%d/%Y")
    time = currentDT.strftime("%I:%M:%S %p")

    temp = round(t, 1)
    p = round(p, 1)
    h = round(h, 1)

    msg = "Time = {0}, Date = {1}, Temperature = {2}, Pressure = {3}, Humidity = {4}".format(time, date, temp, p, h)

    sense.show_message(msg, scroll_speed=0.05)