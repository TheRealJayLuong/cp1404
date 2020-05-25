
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

menu = "q)uit, c)hoose, d)rive"


def main():
    """Menu simulator program"""
    taxis_available = [Taxi("Prius 1", 100), SilverServiceTaxi("Lamborghini", 100, 2),
                       SilverServiceTaxi("Porsche 911", 200, 4)]
    total = 0
    print("Let's drive!")
    print(menu)
    get_menu = input(">>>>> ").lower()

    while get_menu != "q":
        if get_menu == "c":
            print("Taxis available:")
            display_taxi(taxis_available)
            taxi_choice = int(input("choose taxi: "))
            current_taxi = taxis_available[taxi_choice]

        elif get_menu == "d":
            current_taxi.start_fare()
            distance_driving = float(input("Drive how far? "))
            current_taxi.drive(distance_driving)
            price_for_trip = current_taxi.get_fare()
            print("Your {} trip cost you ${}".format(current_taxi.name, price_for_trip))
            total += price_for_trip
        else:
            print("Invalid menu choice")
        print("Bill to date: {}".format(current_taxi))
        print(menu)
        get_menu = input(">>>>> ").lower()

    print("Total trip cost: ${:.2f}".format(total))
    print("Taxis are now:")
    display_taxi(taxis_available)


def display_taxi(taxis_available):
    """Display number of taxis"""
    for number, quantity in enumerate(taxis_available):
        print("{} - {}".format(number, quantity))


main()