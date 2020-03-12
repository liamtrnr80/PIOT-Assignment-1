from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

sense.clear()

b = [0, 0, 0]
w = [150, 150, 150]

dice = [
    [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
    ],
    [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
    ],
    [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
    ],
    [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
    ],
    [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
    ],
    [
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w,
        w,w,w,w,w,w,w,w
    ]
]

def dice_roll():
    n = random.randint(3, 9)
    while n != 0:
        sense.set_pixel(random.choice(dice))
        n -= 1
        sleep(.2)
        

while True:
    x, y, z = sense.get_accelerometer_raw().values()

    x = abs(x)
    y = abs(y)
    z = abs(z)

    if x > 2 or y > 2 or z > 2:
        dice_roll()
        sleep(2)