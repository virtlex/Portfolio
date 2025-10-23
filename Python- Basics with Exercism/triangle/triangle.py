def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b >= c and a+c >= b and b+c >= a and a != 0 and b != 0 and c != 0:
        if a == b == c:
            return True
        else:
            return False
    else:
        return False   


def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b >= c and a+c >= b and b+c >= a and a != 0 and b != 0 and c != 0:
        if a == b or b == c or a == c:
            return True
        else:
            return False
    else:
        return False   



def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]
    if a+b >= c and a+c >= b and b+c >= a and a != 0 and b != 0 and c != 0:
        if a != b and b != c and a != c:
            return True
        else:
            return False
    else:
        return False


print(isosceles([1, 1, 3]))