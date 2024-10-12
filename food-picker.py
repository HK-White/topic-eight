# Excercise 5
sugar = input("Do you want sugar? (Yes/No)")
veggies = input("Do you want veggies? (Yes/No)")

if veggies == "Yes" and sugar == "Yes":
    print("You should try our veggie cake! It has sugar and veggies!")
elif veggies == "Yes" and sugar == "No":
    print("Try our yummy fruit salad! No sugar added!")
elif veggies == "No" and sugar == "No":
    print("You should try our world-famous sugar and veggie-free ice cream!")
else:
    print("Since none of the other options meet your preferences, I would suggest our chocalete brownie!")