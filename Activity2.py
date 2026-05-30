from datetime import datetime

name = input("enter your name:")
mood = input("How are you feeling today? (Happy,sad,stressed/tired):").lower()
energy = int(input("Enter your energy level (1-10):"))
if mood == "happy":
    print("You are feeling great!")
elif mood == "sad":
    print("Try talking to a friend, listening to music< or taking a short walk")
elif mood == "stressed":
    print("Take short breaks, stay organized, and practice deep breathing")
elif mood == "stressed":
    print("Get some rest, drink water, and avoid overworking yourself.")

else:
    print("Have a balance day and take care of yourself")