# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask user for response and loop until they
            response = float(input(question))

            # enter a number that is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine starts here...

keep_going = ""
while keep_going == "":
    # Get width and height
    width = num_check("Width: ")
    print(width)
    height = num_check("Height: ")
    print(height)

    # Calculate  area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Area: {area} square units")
    print(f"Perimeter: {perimeter} units")

    # Ask user if they want to keep going
    keep_going = input("press enter if you want to continue and any key to quit. ")
    print()
print("Thank you for using the area / perimeter calculator")