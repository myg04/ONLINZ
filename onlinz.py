#Function that asks customer what height, width and depth their return box is and repeats until they enter valid input
def box_dimensions():
    while True:
        try:
            global customer_height
            customer_height = int(input("Hi {}, what is the height of your return box in cm? " .format(customer_name)))
            if customer_height >= 5 and customer_height <= 100:
                break
            else:
                print("Please enter your return boxes height (e.g. 10)\nHeight Requirements: Minimum 5cm - Maximum 100 cm")
        except ValueError:
            print("Please enter boxes height in digit format (e.g. 10)")

    while True:
        try:
            global customer_width
            customer_width = int(input("{}, What is the width of your return box in cm? " .format(customer_name)))
            if customer_width >= 5 and customer_width <= 100:
                break
            else:
                print("Please enter your return boxes width (e.g. 10)\nWidth Requirements: Minimum 5cm - Maximum 100 cm")
        except ValueError:
            print("Please enter boxes width in digit format (e.g. 10)")

    while True:
            try:
                global customer_depth
                customer_depth = int(input("{}, What is the depth of your return box in cm? " .format(customer_name)))
                if customer_depth >= 5 and customer_depth <= 100:
                    break
                else:
                    print("Please enter your return boxes depth (e.g. 10)\nDepth Requirements: Minimum 5cm - Maximum 100 cm")
            except ValueError:
                print("Please enter boxes depth in digit format (e.g. 10)")
    print("Your return box dimensions are: \nHeight = {}cm \nWidth = {}cm \nDepth = {}cm" .format(customer_height, customer_width, customer_depth))
    
    return customer_height, customer_width, customer_depth

#calculates the volume of the customers return box and tells them
def calc_volume(height, width, depth):
    global volume
    volume = height * width * depth
    print("Your return box volume is {} cm\u00b3" .format(volume))
    return volume

#Asks customer where their returning their item from and tells them how much it will cost
def final_cost(customer_island):
    while True: 
          if customer_island in island_rates:
               global final_rate
               final_rate = island_rates[customer_island] * rate
               print("You are returning an item from {} and it will cost $ {:.2f}".format(customer_island, final_rate))
               break
          else:
                print("Please enter one of the following islands you are returning your item from: \nNorth Island / Te Ika A Maui \nSouth Island / Te Wai Pounamu \nStewart Island / Rakiura  \n(e.g. North Island)")
                customer_island = (input("What island in New Zealand are you returning your item from? ")).title().strip()
        

#Directory of Islands and rate of shipping from there
island_rates = {'North Island':1, 'Te Ika A Maui': 1, 'South Island':1.5, 'Te Wai Pounamu':1.5, 'Stewart Island':2, 'Rakiura':2}



#main program

#Asks for customers name
customer_name = input("Hello customer, what is your name? ").title()
box_dimensions()
calc_volume(customer_height, customer_width, customer_depth)

#Base rates for shipping
if volume <= 6000:
    rate = 8.00
elif volume > 6000 and volume < 100000:
    rate = 12.00
elif volume >= 100000:
    rate = 15.00
else:
    print("Please contact staff")


#Asks what Island is returning item from and total cost of shipping 
customer_island = (input("Options: \nNorth Island / Te Ika A Maui \nSouth Island / Te Wai Pounamu \nStewart Island / Rakiura \n(We are not accepting returns from other islands yet) \nWhat island in New Zealand are you returning your item from?   ")).title().strip()
final_cost(customer_island)

#Ask for customer details
print("Please enter the following details to store in our system")
customer_lastname = input("What is your last name? ").title()
customer_address = input("What is your address? ").title()
customer_telephone = input("What is your telephone number? ")
final_details = [customer_name, customer_lastname, customer_telephone, customer_address, final_rate]


#Final message with personal details and cost of returning item
print("Your first name: {} \nYour last name: {} \nYour telephone Number: {} \nYour address: {} \nYour final cost: ${:.2f}" .format(final_details[0], final_details[1], final_details[2], final_details[3], final_details[4]))


