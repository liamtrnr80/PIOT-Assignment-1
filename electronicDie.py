from sense_hat import SenseHat
from time import sleep
import random

class RollDice:
    sense = SenseHat()
    b = [0, 0, 0]
    w = [150, 150, 150]
    n = random.randrange(0,5)
    dice = [
            [
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,b,b,w,w,w,
                w,w,w,b,b,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w
            ],
            [
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,w,w,w,
                w,b,b,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,b,b,w,
                w,w,w,w,w,b,b,w,
                w,w,w,w,w,w,w,w
            ],
            [
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,w,w,w,
                w,b,b,w,w,w,w,w,
                w,w,w,b,b,w,w,w,
                w,w,w,b,b,w,w,w,
                w,w,w,w,w,b,b,w,
                w,w,w,w,w,b,b,w,
                w,w,w,w,w,w,w,w
            ],
            [
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w,
                w,w,w,w,w,w,w,w,
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w,
                w,w,w,w,w,w,w,w
            ],
            [
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w,
                w,w,w,b,b,w,w,w,
                w,w,w,b,b,w,w,w,
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w,
                w,w,w,w,w,w,w,w
            ],
            [
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w,
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w,
                w,w,w,w,w,w,w,w,
                w,b,b,w,w,b,b,w,
                w,b,b,w,w,b,b,w
            ]
        ]

    # def __init__(self):
        
    def dice_roll(self):
        n = random.randint(3, 9)
        while n != 0:
            self.sense.set_pixels(random.choice(self.dice))
            n -= 1
            sleep(.2)

def main():
    print("Sense hat main")
    rollDice = RollDice()

    rollDice.sense.clear()
    while True:
        x, y, z = rollDice.sense.get_accelerometer_raw().values()

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 2 or y > 2 or z > 2:
            rollDice.sense.set_pixels(random.choice(rollDice.dice))
            sleep(2)
            rollDice.sense.clear()


if __name__ == '__main__':
    main()