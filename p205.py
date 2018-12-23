test = "Maleficient"

def to_alternating_case(string):
    result = ''
    for word in string:
        if word.isupper():
            result += word.lower()
        else:
            result += word.upper()
    return result

print to_alternating_case(test)
