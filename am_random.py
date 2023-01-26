### PURPOSE
# Home-made random function

### IMPORTS
import time
from math import ceil

### MAIN
def random():
    # Two almost same values
    t_create = time.time_ns()
    result = ""

    # Add em
    t_create = t_create + time.time_ns()

    # Mod it
    t_create = t_create % time.time_ns()

    # Convert to string
    result = str(t_create)
    # Get last number of the long number lmao
    result = int(result[len(result) - 1])

    return result
