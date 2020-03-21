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



def main():

    rollDice = RollDice()
    diceGame = TwoPlayerGame("John", "Sevan")
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
                diceGame.player1_score+=score
                print(diceGame.player1, "has a score of", diceGame.player1_score)
            else:
                diceGame.player2_score+=score
                print(diceGame.player2, "has a score of", diceGame.player2_score)
            
            sleep(2)
            rollDice.sense.clear()
            playerTurn+=1
        


if __name__ == '__main__':
    main()