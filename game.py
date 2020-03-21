from sense_hat import SenseHat
from time import sleep
import random
from electronicDie import RollDice

class TwoPlayerGame():
    player1_score = 0
    player2_score = 0

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2



def main(self):

    rollDice = RollDice()
    rollDice.sense.clear()
    playerTurn = 0
    
    while True:
        x, y, z = rollDice.sense.get_accelerometer_raw().values()

        x = abs(x)
        y = abs(y)
        z = abs(z)

        if x > 2 or y > 2 or z > 2:
            score = rollDice.dice_roll()
            if(playerTurn%2==0):
                self.player1_score+=score
            else:
                self.player2_score+=score
            print("You Scored:", score)
            sleep(2)
            rollDice.sense.clear()
        


if __name__ == '__main__':
    main()