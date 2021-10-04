def box_dimensions():
    while True:
        try:
            global user_height
            user_height = int(input("Hi {}, What is the height of your return box in cm? " .format(name)))
            if user_height > 5 and user_height < 100:
                break
            else:
                print("Please enter a height between 5 and 100 cm")
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            global user_width
            user_width = int(input("Hi {}, What is the width of your return box in cm? " .format(name)))
            if user_width > 5 and user_width < 100:
                break
            else:
                print("Please enter a width between 5 and 100 cm")
        except ValueError:
            print("Please enter a valid number")

    while True:
            try:
                global user_depth
                user_depth = int(input("Hi {}, What is the depth of your return box in cm? " .format(name)))
                if user_depth > 5 and user_depth < 100:
                    break
                else:
                    print("Please enter a depth between 5 and 100 cm")
            except ValueError:
                print("Please enter a valid number")
    print("Your box dimensions are: \nHeight = {}cm \nWidth = {}cm \nDepth = {}cm" .format(user_height, user_width, user_depth))
    
    return user_height, user_width, user_depth

def calc_volume(height, width, depth):
    global volume
    volume = height * width * depth
    print("Your box volume is {} cm\u00b3" .format(volume))
    return volume


#main program
name = input("Hello customer, what is your name?").title()
box_dimensions()
calc_volume(user_height, user_width, user_depth)

#base rates for shipping
if volume <= 6000:
    rate = 8.00
elif volume > 6000 and volume < 100000:
    rate = 12.00
elif volume >= 100000:
    rate = 15.00
else:
    print("Please contact staff")
