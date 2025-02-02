def solve(heads, legs):
    # total = 35

    # 2x + 4y = 94
    # x + y = 35

    # 2x + 4y = 94
    # 2x + 2y = 70

    # 2y = 24
    # y = 12
    # x = 23
    
    # Calculate the number of rabbits
    numrabbits = int((legs - (2 * heads)) / 2)
    
    # Calculate the number of chickens by subtracting the number of rabbits from total heads
    numchickens = int(heads - numrabbits)

    print("Rabbits:", numrabbits)
    print("Chickens:", numchickens)
    

heads = int(input("Enter the amount of heads: "))
legs = int(input("Enter the amount of legs: "))
solve(heads, legs)
