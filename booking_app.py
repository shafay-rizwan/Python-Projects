# Making a simple chat bot allowing user to book the cab ! 

import random 


# Step 1 we have created a dictionaries in list to store the the data for the available taxi 
cabs = [ 

    {"id" : 1, "name": "Uber Drive", "available": True}, # dont forget using comma in list to seperate dictionary
    {"id" : 2, "name": "Taxi", "available": False},
    {"id" : 3, "name": " InDrive", "available": True}

]

# Step 2 making an empty dictionary to store user_booking_details

booking_details = {}

# Defining a function take take input from the user

def book_cab():
    print("Welcome to 'Chatbox, the online booking agent 🕵️'")
    print(""" In order to book a ride type 'Book now'
In order to exit type 'Exit'""")
    while True:
        user_input = input("Your Text: ").lower()

        if user_input == 'to book':

            print("Enter your current location: ")
            user_pickup_location : str = input("Pickup Location: ")

            # Getting user_destination
            print("What is your Dropoff location: ")
            user_dropoff_location : str = input("Dropoff Location: ")

            # Getting user_choice_of_cab
            print("""Which car do you want to choose from the given:
1. Uber Drive
2. Taxi
3. InDrive
Note: Simple type the numeric value :""")
            
                