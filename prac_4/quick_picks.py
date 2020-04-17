"""Lottery Ticket generator program """
import random

quick_pick_number = int(input("How many quick pick?"))
while quick_pick_number < 0: # test input number if number less than 0
    print("Invalid number")
    quick_pick_number = int(input("Please enter your number"))

for number1 in range(quick_pick_number):  #present the row equal with the input number
    lottery_number = []

    for number2 in range(6): #present 6 number on the line
        number = random.randint(1, 45)

        while number in lottery_number: # check number if the number repeated
            number = random.randint(1,45)
        lottery_number.append(number)
    lottery_number.sort()
    print(" ".join("{:5}".format(number) for number in lottery_number))






