import random
import os
from time import sleep
TheNumber = random.randint(0,100)

Guess = int(input("Enter a guess:\n"))

if Guess in range(0,100):
    if TheNumber == Guess:
        print("Number is :",TheNumber)
        sleep(2)
        os.system('cls')
        print("Hey, You got Right Answer!!")
    else :
        print("Number is :",TheNumber)
        sleep(2)
        os.system('cls')
        print("Better Luck Next Time :(")
else:
    print(Guess,"is out of Range")