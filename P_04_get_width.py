# Ask user for width and loop until they 
# enter a number that is more than zero
def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask user for Response and loop until they
            Response = float(input(question))

            # enter a number that is more than zero
            if Response > 0:
                return Response
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine Goes Here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

    print()

for item in range(0, 2):
    height = num_check("Height: ")
    print(height)