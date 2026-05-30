city = input("Enter your city name:")
temp = float(input("Enter today temparature in C:"))

#part 2 if STATEMENT
if temp > 35:
    print("it is very hot today!")

#part 3 - if-else
if temp > 25:
    print("Great day to go outside!")
else:
    print("Grab a jacket before you go out!")

#part 4 - if-elif-else
if temp > 35:
    print("Great day to go outside!")
elif temp > 25:
    print("weather Warm and Sunny")
elif temp > 15:
    print("weather: Cool and Breezy")
else:
    print("Weather: Cold - stay warm!")

# PART 5 - datetime MODULE
import datetime
import calendar

now = datetime.datetime.now()
print("city", city)
print("Time now:", now)

print(calendar.calendar(now.year))

