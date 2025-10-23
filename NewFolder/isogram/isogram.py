def is_isogram(string):
    string = string.lower().replace(" ","").replace("-","")
    #print (string)
    return len(set(string)) == len(string)

#print(is_isogram("six-year-old"))
