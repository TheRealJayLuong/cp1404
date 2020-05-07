"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

STATE_CODE = str.upper(input("Enter short state: "))
while STATE_CODE != "":
    if STATE_CODE in CODE_TO_NAME:
        print(STATE_CODE, "is", CODE_TO_NAME[STATE_CODE])
    else:
        print("Invalid short state")
    STATE_CODE = str.upper(input("Enter short state: "))
    break
print()
for names in CODE_TO_NAME:
    print("{:3}  {:3}  {:3}".format(names,"is",CODE_TO_NAME[names]))

