def is_armstrong_number(number):
    power= len(str(number))
    name = str(number)
    i=0
    Armstrong = 0
    for i in range(power):
        Armstrong = Armstrong + int(name[i]) ** power
    if Armstrong == number:
        return True
    else:
        return False

print(is_armstrong_number(153))
