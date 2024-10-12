# Excercise 2
event = input("Is the event formal? (True/False)")
temp = int(input("What is the temperature? (C)"))

if event == "True":
    if temp <= 15:
        print("Dress in a Warm/Formal Outfit")
    elif temp >= 16:
        print("Dress in a light formal suit")
elif event == "False":
    if temp <= 15:
        print("Wear a comfy sweater with jeans")
    
else:
    print("Wear a nice pair of shorts with a t-shirt!")