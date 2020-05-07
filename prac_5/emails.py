
def main():
    """Store users'emails and names in dictionary """
    creating_dict = {}
    email = input("Email: ")

    while email != "":
        name = get_name(email)
        get_your_name = input("Is your name is {}? (Y/n)".format(name))

        if get_your_name.upper() != "Y" and get_your_name != "":
            name = input("Name: ")
        creating_dict[email] = name
        email = input("Email: ")

    for email, name in creating_dict.items():
        print(" {} ({}) ".format(name, email))


def get_name(email):
    """Display the name from email"""

    part = email.split("@")[0]
    parts = part.split('.')
    name = " ".join(parts).title()
    return name


main()


