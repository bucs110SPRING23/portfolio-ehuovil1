import random
import math

cpuguess = int(random.randint(1,10))


for i in range (3):
    userinput = int(input("Choose a number 1-10"))
    if userinput == cpuguess:
        print("correct!")
        break
    elif userinput > cpuguess:
        print("Too High")
    elif userinput < cpuguess:
        print("Too Low")
        




