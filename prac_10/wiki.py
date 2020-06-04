"""
Display simple program with Wikipedia
"""
import wikipedia

wiki = wikipedia.search("Trump")
print(wiki)
print("-----------")
wiki1 = wikipedia.summary("Google")
print(wiki1)
print("-----------")
try:
    menu = "{} - Searching wiki \n{} - Summary information".format("Se", "Su")
    print(menu)
    get_input = input(">>>>>>> ")
    while get_input != "q":
        if get_input == "Se":
            searching = input("Enter your words: ")
            print(wikipedia.search(searching))
            print(menu)
            get_input = input(">>>>>>> ")
        elif get_input == "Su":
            get_summary = input("Enter your words: ")
            print(wikipedia.summary(get_summary))
            print(menu)
            get_input = input(">>>>>>> ")
        elif get_input == "":
            quit()
        else:
            print("Invalid menu choice")
            print(menu)
            get_input = input(">>>>>>> ")
except wikipedia.exceptions.DisambiguationError as e:
    print(e.options)