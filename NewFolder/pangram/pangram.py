def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            return False
    return True
    

#print(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"))
