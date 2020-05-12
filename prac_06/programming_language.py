"""Programming Language"""


class ProgrammingLanguage:
    """Storing programing language's information """

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.type = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Display program language's information"""
        return "{}, {} Typing, Reflection = {}, First appeared in {} ".format(self.name, self.type, self.reflection,
                                                                              self.year)

    def is_dynamic(self):
        """ Checking if language is dynamic"""
        return self.type == "Dynamic"


def checking_program():
    """Checking program language class"""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    program_languages = [ruby, python, visual_basic]
    print(ruby)
    print(python)
    print(visual_basic)
    print("-----------")
    print("The dynamically typed languages are:")
    for language in program_languages:
        if language.is_dynamic():
            print(language.name)


if __name__ == "__main__":
    checking_program()
