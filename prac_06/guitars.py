"""Guitar program"""
from guitar import Guitar

guitars = []


def main():
    """Guitar program is worked by Guitar class"""
    print("My guitars!")
    name = input("Name: ")
    while name != "":
        year = int(input("year: "))
        cost = float(input("Cost: $"))
        add_information = Guitar(name, year, cost)
        guitars.append(add_information)
        print(add_information, "added.")
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    if guitars:
        guitars.sort()  # sorting by year through the __lt__ method in Guitar class
        print("These are my guitars:")
        for thing, things in enumerate(guitars):  # display number of guitar
            vintage_string = ""
            if things.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(thing, things.name,
                                                                      things.year, things.cost,
                                                                      vintage_string))
    else:
        print("No guitars")


main()
