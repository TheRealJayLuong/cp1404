from silver_service_taxi import SilverServiceTaxi


def main():
    """Test silver service taxi program"""
    """Test SilverServiceTaxi"""
    my_silver_taxi = SilverServiceTaxi("Porsche 911", 200, 2)
    my_silver_taxi.drive(18)
    print("The fare for this trip is ${:.2f}".format(my_silver_taxi.get_fare()))
    print(my_silver_taxi)


main()