# Excercise 1
mood = input("How are you feeling today? ")
weather = input("It is sunny? (True/False) ")

if weather == "False":
    weather = False
    if mood == "happy":
        print("Watch a romance movie!")
    elif mood == "sad":
        print("Watch a drama")
    else:
        print("Watch an adventure movie!")

else:
    weather = True
    if mood == "happy":
        print("Watch a comedy movie!")
    else:
        print("Watch a drama")

# Figured out through trial and error.