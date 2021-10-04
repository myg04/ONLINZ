def box_dimensions():
    while True:
        try:
            height = int(input("Hi {}, What is the height of your return box in cm? " .format(name)))
            if height > 5 and height < 100:
                break
            else:
                print("Please enter a height between 5 and 100 cm")
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            width = int(input("Hi {}, What is the width of your return box in cm? " .format(name)))
            if width > 5 and width < 100:
                break
            else:
                print("Please enter a width between 5 and 100 cm")
        except ValueError:
            print("Please enter a valid number")

    while True:
            try:
                depth = int(input("Hi {}, What is the depth of your return box in cm? " .format(name)))
                if depth > 5 and depth < 100:
                    break
                else:
                    print("Please enter a depth between 5 and 100 cm")
            except ValueError:
                print("Please enter a valid number")
    print("Your box dimensions are: \nHeight = {}cm \nWidth = {}cm \nDepth = {}cm" .format(height, width, depth))


       



name = input("Hello customer, what is your name?").title()
box_dimensions()