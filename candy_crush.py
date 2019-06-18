# Problem description: write a function to crush candies in a one-dimensional board. 
# In candy crush games, groups of like items are removed from the board. In this problem, 
# any sequence of 3 or more like items should be removed and any items adjacent to that sequence should be considered
# adjacent to each other. This process should be repeated as many times as possible. 

# Sample inputs, expected outputs:
# ABBBCC -> ACC
# ABCCCBB -> A 

def candy_crush(candies):
    
    print("candies:", candies)
    stack = []  
    count = []  
    
    for candy in candies:     
        
        if count and count[-1] >= 3 and candy != stack[-1]:
            for _ in range(count[-1]):
                stack.pop()
            count.pop()  
          
        if not stack or candy != stack[-1]:
            stack.append(candy)
            count.append(1)
        elif candy == stack[-1]:
            stack.append(candy)
            count[-1] += 1
        
    return ''.join(stack)


# ## Tests
print(candy_crush("ABBBCC")
print(candy_crush("ABCCCBB"))
print(candy_crush("AAAC"))
print(candy_crush("AAAAC"))
print(candy_crush("AACCCCCDEEBBBDEDF"))
