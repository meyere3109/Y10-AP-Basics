# ask the user for their name
username = input("What is your name? ")

# ask the user for their favourite number (integer)
fav_num = int(input("What is your favourite number? "))

# Double, halve and square the user's favourite number
double = fav_num * 2
half = fav_num / 2
square = fav_num * fav_num

# Greet the user
print(f" \nHi {username}, your favourite number is {fav_num}")

# Output the result of doubling, halving and
# squaring their favourite integer
print(f"Double {fav_num} is {double}")
print(f"Half {fav_num} is {half}")
print(f"{fav_num} squared is {square}")
print()
print("Have a nice day")
