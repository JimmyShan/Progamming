## Get this question from an interview, which also appears elsewhere. Below is my solution (not my original naive solution). 

## Question: suppose we have a function random5 which can generate number 1 to 5 with equal probability, 
## write a function generate random numbers 1-7 with equal probability. 

import random
def random5():
    return random.randint(1, 5)

def random7():
    while True:
        a = random5()
        b = random5()
        c = 5 * (a - 1) + b
        if c <= 21:
            break
        
    return c%7 + 1

### Test:
import collections
print(collections.Counter([random7() for _ in range(100000)]))
