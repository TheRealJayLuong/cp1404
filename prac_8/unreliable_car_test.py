from unreliable_car import UnreliableCar


def main():
    """Test unreliable car program"""
    my_unreliable_car = UnreliableCar("Ferrari", 100, 70)
    my_unreliable_car1 = UnreliableCar("Bugatti", 100, 10)

    for km in range(1, 8):
        print("Attempting to drive {}km:".format(km))
        print("{:5} drove {:2}km".format(my_unreliable_car.name, my_unreliable_car.drive(km)))
        print("{:5} drove {:2}km".format(my_unreliable_car1.name, my_unreliable_car1.drive(km)))

    print(my_unreliable_car)
    print(my_unreliable_car1)



main()
