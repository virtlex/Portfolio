def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    factor = 0
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")
    for i in range(1,number):
        if number % i == 0:
            factor += i
    if factor == number:
        return "perfect"
    if factor >= number:
        return "abundant"
    if factor <= number:
        return "deficient"
        

        
#print(classify(-3))