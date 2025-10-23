def square(number):
    if number in range (1,65):
        if number == 1:
            return 1
        elif number ==2:
            return 2
        else:
            grains = 2 ** (number-1) 
            return grains
    else:
        raise ValueError("square must be between 1 and 64")

    

def total():
    board = 3
    for i in range (3,65):
        board = board + 2 ** (i-1)
    return board

print(square(64))
print(total())
