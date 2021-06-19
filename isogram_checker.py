def is_isogram(string):
    string = string.lower()
    if string == "":
        return True
    for letter in string:
        if string.count(letter) > 1: 
            return False
    return True
