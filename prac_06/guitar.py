"""Guitar class"""
class Guitar:
    def __init__(self, name="", year=0, cost=0):
        """storing information about guitars"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display guitar's information"""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get age of guitar based on the current year"""
        return 2020 - self.year

    def is_vintage(self):
        """Checking condition if guitar is vintage or not based on age"""
        return self.get_age() >= 50

    def __lt__(self, other):
        """Checking condition when user input the year"""
        return self.year < other.year
