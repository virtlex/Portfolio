import string

def rotate(text, key):
    ROT_text = ""
    alphabet  = list(string.ascii_lowercase)
    alphabet_upper  = list(string.ascii_uppercase)
    ROT_alphabet= alphabet[key:] + alphabet[:key]
    ROT_alphabet_upper= alphabet_upper[key:] + alphabet_upper[:key]
    #print(ROT_alphabet)
    for char in text:
        if char == " ":
            ROT_text += " "
            continue
        if char == "!":
            ROT_text += "!"
            continue
        if char == "'":
            ROT_text += "'"
            continue
        if char == ".":
            ROT_text += "."
            continue
        if char == ",":
            ROT_text += ","
            continue
        if char.isnumeric():
            ROT_text += char
            continue
        if char.isupper():
            index = alphabet_upper.index(char)
            ROT_text += ROT_alphabet_upper[index]
        else:
            index = alphabet.index(char)
            ROT_text += ROT_alphabet[index]
    #print(ROT_text)
    return ROT_text

#rotate("O m G 1 2 3.1!'", 5)