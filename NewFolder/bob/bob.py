def response(hey_bob):
    hey_bob = hey_bob.strip()
    if hey_bob.isupper() and hey_bob[-1] =="?":
        return "Calm down, I know what I'm doing!"
    elif not hey_bob:
        return "Fine. Be that way!"
    elif hey_bob[-1] =="?":
        return "Sure."
    elif hey_bob.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."
    

print(response("t\t\t\t\t\t\t\t\t\t"))