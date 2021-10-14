#Function that asks customer what height, width and depth their return box is and repeats until they enter valid input
def box_dimensions():
    while True:
        try:
            global user_height
            user_height = int(input("Hi {}, What is the height of your return box in cm? " .format(customer_name)))
            if user_height > 5 and user_height < 100:
                break
            else:
                print("Please enter your return boxes height between 5 and 100 cm (e.g. 10)")
        except ValueError:
            print("Please enter a valid number (e.g. 10)")

    while True:
        try:
            global user_width
            user_width = int(input("{}, What is the width of your return box in cm? " .format(customer_name)))
            if user_width > 5 and user_width < 100:
                break
            else:
                print("Please enter your return boxes width between 5 and 100 cm (e.g. 10)")
        except ValueError:
            print("Please enter a valid number (e.g. 10)")

    while True:
            try:
                global user_depth
                user_depth = int(input("{}, What is the depth of your return box in cm? " .format(customer_name)))
                if user_depth > 5 and user_depth < 100:
                    break
                else:
                    print("Please enter your return boxes depth between 5 and 100 cm (e.g. 10)")
            except ValueError:
                print("Please enter a valid number (e.g. 10)")
    print("Your return box dimensions are: \nHeight = {}cm \nWidth = {}cm \nDepth = {}cm" .format(user_height, user_width, user_depth))
    
    return user_height, user_width, user_depth

#calculates the volume of the customers return box and tells them
def calc_volume(height, width, depth):
    global volume
    volume = height * width * depth
    print("Your return box volume is {} cm\u00b3" .format(volume))
    return volume

#Asks customer where their returning their item from and tells them how much it will cost
def final_cost(customer_island):
    while True:
        try:

            if customer_island in island_rates:
                global final_rate
                final_rate = island_rates[customer_island] * rate
                print("You are returning an item from {} and it will cost $ {:.2f}".format(customer_island.title(), final_rate))
                break
            else:
                print("Please enter one of the following islands: \nNorth Island / Te Ika a Maui \nSouth Island / Te Wai Pounamu \nStewart Island / Rakiura  \n(e.g. North Island)")
                customer_island = (input("What Island in New Zealand are you returning your item from? ")).title()
        except ValueError:
            print("Please enter the Islands name with no special characters or numbers (e.g. North Island)")

#Directory of Islands and rate of shipping from there
island_rates = {'North Island':1, 'Te Ika a Maui': 1, 'South Island':1.5, 'Te Wai Pounamu':1.5, 'Stewart Island':2, 'Rakiura':2}



#main program

#Asks for customers name
customer_name = input("Hello customer, what is your name? ").title()
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


#Asks what Island is returning item from and total cost of shipping 
customer_island = (input("Options: \nNorth Island / Te Ika a Maui \nSouth Island / Te Wai Pounamu \nStewart Island / Rakiura \n(We are not accepting returns from other islands yet) \nWhat island in New Zealand are you returning your item from?   ")).title()
final_cost(customer_island)

#Ask for customer details
print("Please enter the following details to store in our system")
customer_lastname = input("What is your lastname? ").title()
customer_address = input("What is your adress? ").title()
customer_telephone = input("What is your telephone number? ")
final_details = [customer_name, customer_lastname, customer_telephone, customer_address, final_rate]


#final message with personal details and cost of returning item
print("Your First Name: {} \nYour Last Name: {} \nYour Telephone Number: {} \nYour address: {} \nYour Return Final Cost: ${:.2f}" .format(final_details[0], final_details[1], final_details[2], final_details[3], final_details[4]))



