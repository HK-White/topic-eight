# Excercise 3

grade = input("What is your grade? (A/B/C)")
sport = input("Are you in sports? (Yes/No)")
drama = input("Are you in drama? (Yes/No)")

# A Grades
if grade == "A":
    if sport == "Yes" and drama == "Yes":
        print("You get 20% off")

    elif sport == "Yes" and drama == "No":
        print("You get 20% off")
    else:
        print("You get 10% off")

# B Grades
elif grade == "B":
    if sport == "Yes" and drama == "Yes":
        print("You get 15% off")

    elif sport == "Yes" and drama == "No":
        print("Sorry No Discount")
    else:
        print("Sorry No Discount")

# C Grades
elif grade == "C":
    if sport == "Yes" and drama == "Yes":
        print("No discount")

    elif sport == "Yes" and drama == "No":
        print("Sorry No Discount")
    else:
        print("No discount, sorry!")