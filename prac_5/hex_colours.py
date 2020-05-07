"""Select hexadecimal colour code in dictionary"""
CODE_TO_COLOURS = {"BlueViolet": "#8a2be2", "burlywood": "#deb887", "CadetBlue": "#5f9ea0", "chocolate": "#d2691e",
                   "coral": "#ff7f50", "CornflowerBlue": "#6495ed", "DarkGoldenrod": "#b8860b", "DarkGreen": "#006400",
                   "DarkKhaki": "#bdb76b", "DarkOrange": "#ff8c00"}
print(CODE_TO_COLOURS)
COLOUR_CODE = input("Enter your colour")
while COLOUR_CODE != "Q":
    if COLOUR_CODE in CODE_TO_COLOURS:
        print("{} is {}".format(COLOUR_CODE, CODE_TO_COLOURS[COLOUR_CODE]))
    elif COLOUR_CODE == "":
        quit()
    else:
        print("Invalid colour name")
    COLOUR_CODE = input("Enter your colour")
