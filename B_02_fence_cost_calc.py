# Ask for width, length and cost
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
    height = num_check("Height: ")
    cost = num_check("$/m of fencing: ")

    # Calculate  perimeter
    perimeter = 2 * (width + height)

    # Calculate cost
    total = perimeter * cost

    # Output results
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Total cost of fencing: ${total:.2f}")

    # Ask user if they want to keep going
    keep_going = input("press enter if you want to continue and any key to quit. ")
    print()

print("Thank you for using the perimeter fencing costs calculator")
