"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random

def main():
    """Get the score and show the result"""
    score = float(input("Enter the score: "))
    result = get_score(score)
    print(result)
# generate random score and print result
    random_score = random.randint(1,101)
    print(random_score)
    print(get_score(random_score))

def get_score(score):
    """Check out condition of each score given  """
    if score > 100:
        return "Invalid score"
    elif score > 90:
        return "Excellent"
    elif score > 50:
        return "Passable"
    elif score > 0 and score <= 50:
        return "Bad"
    else:
        return "Invalid score"


main()