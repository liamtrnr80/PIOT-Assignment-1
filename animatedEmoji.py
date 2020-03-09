from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (142, 71, 0)
bro = (204, 102, 0)
e = (0, 0, 0)

image = [
    e,e,e,e,b,e,e,e,
    e,e,e,bro,bro,e,e,e,
    e,e,b,b,b,b,e,e,
    e,bro,w,bro,w,bro,e,e,
    e,b,b,b,b,b,b,e,
    bro,bro,w,w,w,w,bro,bro,
    b,b,b,b,b,b,b,b,
    e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
    sleep(30)
    sense.clear()
    