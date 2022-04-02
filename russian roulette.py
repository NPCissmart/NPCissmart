import os
import random
from time import sleep

while True:
    print('loading the bullet into a random chamber')
    sleep(6)
    print('get ready to pull the trigger')
    sleep(1)
    print('3....')
    sleep(1)
    print('2....')
    sleep(1)
    print('1....')
    sleep(1)
    print('pull the trigger.')
    sleep(1)
    randomizer = random.randint(0,6)
 
    if randomizer == 3:
        print('You pulled the trigger and...Click! You survived.')
    else:
        print('You pulled the trigger and.... BANG! YOU DIED!')
    play = input('Want to play again? Y/N')
    if play == 'N':
        break
    if play == 'Y':
        n = input('Wanna try hardcore mode? Y/N')
        if n == 'Y':
            print('get ready you have 5 seconds')
            sleep(5)
            hardcoremizer = random.randint(0,10)
            if hardcoremizer == 6:
                print('Wow, true luck. You survived')
            else:
                print('You died...... get ready')
                sleep(2)
                os.system('shutdown -s -t 1')
        
