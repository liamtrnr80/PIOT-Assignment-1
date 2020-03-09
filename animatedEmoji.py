from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

w = (150, 150, 150)
b = (142, 71, 0)
bro = (204, 102, 0)
y = (255, 192, 0)
e = (0, 0, 0)
p = (150,0,150)

emoji = [
    [
        w,w,w,w,b,w,w,w,
        w,w,w,b,b,w,w,w,
        w,w,b,b,b,b,w,w,
        w,b,e,b,e,b,w,w,
        w,b,b,b,b,b,b,w,
        b,b,e,e,e,e,b,b,
        b,b,b,b,b,b,b,b,
        w,w,w,w,w,w,w,w
    ],
    [
        w,y,y,y,y,y,y,w,
        y,y,y,y,y,y,y,y,
        y,e,e,y,y,e,e,y,
        y,e,e,y,y,e,e,y,
        y,y,y,y,y,y,y,y,
        y,e,y,y,y,y,e,y,
        y,y,e,e,e,e,y,y,
        w,y,y,y,y,y,y,w
    ],
    [
        w,p,p,p,p,p,p,w,
        p,p,p,p,p,p,p,p,
        p,e,p,p,p,p,e,p,
        p,e,e,p,p,e,e,p,
        p,p,p,p,p,p,p,p,
        p,p,p,p,p,p,e,p,
        p,p,e,e,e,e,p,p,
        w,p,p,p,p,p,p,w
    ]
]

n = 0

while True:
    if n == 0:
        sense.set_pixels(emoji[n])
        n = 1
        sleep(1)
    elif n == 1:
        sense.set_pixels(emoji[n])
        n = 2
        sleep(1)
    elif n == 2:
        sense.set_pixels(emoji[n])
        n = 0
        sleep(1)
