def validateString(s):
    letter_flag = "no"
    number_flag = "no"
    for i in s:
        if i.isalpha():
            letter_flag = "Yes"
        if i.isdigit():
            number_flag = "Yes"
    return letter_flag and number_flag
print validateString('Helloworld.123')
