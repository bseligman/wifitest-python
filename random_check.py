### PURPOSE
# Checks random function for probability

### IMPORTS
from am_random import random

### MAIN
def RCheck():
    ### VARS
    RONE = 0
    RTWO = 0
    RTHREE = 0
    RFOUR = 0
    RFIVE = 0
    RSIX = 0
    RSEVEN = 0
    REIGHT = 0
    RNINE = 0

    for i in range(0, 100, 1):
        RAN = random()
        if(RAN == 1):
            RONE+= 1
        if(RAN == 2):
            RTWO+= 1
        if(RAN == 3):
            RTHREE+= 1
        if(RAN == 4):
            RFOUR+= 1
        if(RAN == 5):
            RFIVE+= 1
        if(RAN == 6):
            RSIX+= 1
        if(RAN == 7):
            RSEVEN+= 1
        if(RAN == 8):
            REIGHT+= 1
        if(RAN == 9):
            RNINE+= 1

    # Print Results
    print("-Test of Randomness in base 10-")
    print("1 = " + str(RONE/100) + "%")