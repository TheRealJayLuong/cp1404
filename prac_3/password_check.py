MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

# showing instruction when entering password
def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
#
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = get_password()
    while not is_valid_password(password):
        print("Invalid password!")
        password = get_password()

    asterisks(password)


def asterisks(password):
    """print as many "*" as there are character in the password """
    print("Your {}-character password is valid: {}".format(len(password), "*" * len(password)))


def get_password():
    password = input("> ")
    return password


def is_valid_password(password):
    """Determine if the provided password is valid."""
    if len(password)< MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
# count each kind of character
    for char in password:
        if char.isdigit():
            count_digit +=1
        elif char.islower():
            count_lower +=1
        elif char.isupper():
            count_upper +=1
        elif char in SPECIAL_CHARACTERS:
            count_special +=1
# result return false when user input 0
    if count_lower ==0 or count_upper ==0 or count_digit ==0:
        return False
# result return false when user input 0
    elif SPECIAL_CHARACTERS ==0:
        return False

    else:
        return True




    # if we get here (without returning False), then the password must be valid
    return True
main()