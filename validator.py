# ------------------------------------
#   Name: Zi Xue Lim
#   ID : 1573849
#   Cmput 274, Fall 2019
#   Weekly Assignment 1 : Password Validaion and Generator
# ------------------------------------
import random
def validate(password):
    validSpecialChar = 0
    result = "Secure"
    lengthPass = len(password)
    uncertain = 0
    # analyse password
    if lengthPass < 8 or password.find(" ") != -1 or \
            password.find("-") != -1 or password.find("_") != -1:
        result = "Invalid"
        uncertain = 1
        # check if length of password is less than 8 or has invalid characters
    elif password.isupper() or password.islower():
        result = "Insecure"
        uncertain = 1
        # check if password has all uppercase or all lower
    else:
        if not any(x.isdigit() for x in password):
            uncertain = 1
            result = "Insecure"  # check if only numbers in password
    """ for loop checks counts for special char, if 0 its is insecure"""
    if uncertain == 0:
        for p in range(0, lengthSpeciChar):
            if listChar[p] in password:
                validSpecialChar = validSpecialChar + 1
        if validSpecialChar == 0:
            result = ("Insecure")
    return result  # returns either "Secure","Insecure", or "invalid"
    pass
def generate(n):
    password = []  # building up password
    """first command adds randome captial in position 0 in password then a
    random lower case letter is added to position 1 then a random
    char from listChar array in main function is added then a randome number
    from 0-9 is added to password in position 3. After that
    from position 4 till n, random char added"""
    password.append(chr(random.randint(65, 90)))
    password.append(chr(random.randint(97, 122)))
    password.append(listChar[random.randint(0, lengthSpeciChar)])
    password.append(str(random.randint(0, 9)))
    for x in range(4, n):
        randomAlphaNum = random.randint(0, 3)
        if randomAlphaNum == 0:
            password.append(chr(random.randint(65, 90)))
        elif randomAlphaNum == 1:
            password.append(chr(random.randint(97, 122)))
        elif randomAlphaNum == 2:
            password.append(listChar[random.randint(0, lengthSpeciChar)])
        else:
            password.append(str(random.randint(0, 9)))
    random.shuffle(password)
    # shuffle the password so the first 4 char arent always in the same order
    password = "".join(password)  # combine to a string
    return password  # return a secure password generated to main function
    pass
if __name__ == "__main__":
    """ global variable so can acess from all
    functions listChar and lengthSpecialChar"""
    listChar = ["!", "#", "$", "%", "&", "'",
                "(", ")", "*", "+", ",", ".", "/",
                ":", ";", "<", "=", ">", "?", "@",
                "[", "]", "^", "`", "{", "|", "}", "~"]
    lengthSpeciChar = len(listChar)
    password = generate(10)
    print("Password gen:" + password)
    print(validate(password))