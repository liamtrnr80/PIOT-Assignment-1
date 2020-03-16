from sense_hat import SenseHat
from time import sleep

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

class Emoji():

    def printEmoji(self, n, sense):
        sense.set_pixels(emoji[n])
        sleep(1)

def main():
    sense = SenseHat()
    emoji = Emoji()

    n = 0

    while True:
        if n == 0:
            emoji.printEmoji(n, sense)
            n = 1
        elif n == 1:
            emoji.printEmoji(n, sense)
            n = 2
        else:
            emoji.printEmoji(n, sense)
            n = 0

if __name__ == '__main__':
    main()