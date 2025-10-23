def is_valid(isbn):

    isbn = isbn.replace("-","")
    i=10
    code = 0
    if not isbn[:-1].isnumeric():
        return False
    if len(isbn) !=10:
        return False
    if not (isbn[-1].isdigit() or isbn[-1] == "X"):
        return False
    for digit in isbn:
        if digit == "X" and i == 1:
            digit = 10
        code += int(digit)*i
        i-=1
    if code %11 == 0:
        return True
    else:
        return False


#print(is_valid("3-598-21515-X"))
