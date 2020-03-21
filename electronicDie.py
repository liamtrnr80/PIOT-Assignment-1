from sense_hat import SenseHat
from time import sleep
import random

class RollDice:
    sense = SenseHat()
    dice_roll = 0
    b = [0, 0, 0]
    w = [150, 150, 150]
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
        
    def dice_roll(self):
        x=0
        while x<12:
            self.sense.set_pixels(self.dice[x%6])
            sleep(.1)
            x+=1
        dice_roll = random.randrange(0,6)
        self.sense.set_pixels(self.dice[dice_roll])
        print("You rolled a:" , dice_roll+1)

    def get_dice_roll(self):
        return self.dice_roll

def main():

    rollDice = RollDice()

    rollDice.sense.clear()
    while True:
        x, y, z = rollDice.sense.get_accelerometer_raw().values()

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 2 or y > 2 or z > 2:
            rollDice.dice_roll()
            sleep(2)
            rollDice.sense.clear()
        


if __name__ == '__main__':
    main()