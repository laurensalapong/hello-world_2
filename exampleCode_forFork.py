user_name = input("Hello user. What is your name?\n")
user_grade = input("What grade would you like for this assignment?\n")

try:
    # Attempt to convert user_grade to an integer
    user_grade_int = int(user_grade)
    print("Sike, you thought. You get a Z.\nLol, you can't even get an F.")
except ValueError:
    # If conversion fails, proceed with the original string input
    print(user_name + ", your grade is a " + user_grade + ".")