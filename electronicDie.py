from sense_hat import SenseHat
from time import sleep
import random

class RollDice:
    sense = SenseHat()
    dice_rolled=0
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
        rolling_counter=0
        while rolling_counter<12:
            self.sense.set_pixels(self.dice[rolling_counter%6])
            sleep(.1)
            rolling_counter+=1
        self.dice_rolled = random.randrange(0,6)
        self.sense.set_pixels(self.dice[self.dice_rolled])
        # print("You rolled a:", self.dice_rolled+1)
        return self.dice_rolled+1

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