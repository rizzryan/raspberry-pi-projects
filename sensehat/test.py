import datetime
from sense_hat import SenseHat
from random import randint
sense = SenseHat()


while True:
    temp = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
    currentDT = datetime.datetime.now()
    date = currentDT.strftime("%m/%d/%Y")
    time = currentDT.strftime("%I:%M:%S %p")

    temp = round(temp, 1)
    p = round(p, 1)
    h = round(h, 1)

    textval1 = randint(0, 255)
    textval2 = randint(0, 255)
    textval3 = randint(0, 255)

    backval1 = randint(0, 255)
    backval2 = randint(0, 255)
    backval3 = randint(0, 255)

    text = (textval1, textval2, textval3)
    back = (backval1, backval2, backval3)

    msg = "Time = {0}, Date = {1}, Temperature = {2}, Pressure = {3}, Humidity = {4}".format(time, date, temp, p, h)

    sense.show_message(msg, scroll_speed=0.05, text_color = text, back_color = back)