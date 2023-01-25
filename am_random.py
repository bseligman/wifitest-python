### PURPOSE
# Home-made random function

### IMPORTS
import time
from math import ceil

### MAIN
def random():
    first = mrandom()
    second = mrandom()
    third = mrandom()

    return (first + second - third)

def mrandom():
    # Two almost same values
    t_create = time.localtime()
    """
    result = ""
    i_create = time()

    # Add em
    t_create = t_create + i_create

    # Divide with new given
    t_create = t_create / (time() * 2)

    # Mod it
    t_create = t_create % time()

    result = str(t_create)
    print(result)
    result = int(result[len(result) - 1])
    """

    return print( (t_create.tm_mon * st_create.tm_sec) % t_create.tm_sec)
