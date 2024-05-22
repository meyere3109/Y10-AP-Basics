error = "Please enter a number that is more than zero\n"
while True:

    try:
        # Ask user for width and loop until they
        width = float(input("Width: "))

        # enter a number that is more than zero
        if width > 0:
            break
        else:
            print(error)

    except ValueError:
        print(error)
