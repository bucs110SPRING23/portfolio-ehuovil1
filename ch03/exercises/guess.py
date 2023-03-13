import random
import math

cpuguess = int(random.randint(1,10))
guesses = 0
for i in range (1, 10000):
    userinput = int(input("Choose a number 1-10"))
    if userinput == cpuguess:
        guesses += 1
        print("Correct!, the correct answer was " + str(cpuguess) +  " and it took you " + str(guesses) + " tries")
        break
    elif userinput > cpuguess:
        print("Too High")
        guesses += 1
    elif userinput < cpuguess:
        print("Too Low")
        guesses += 1

    
        




