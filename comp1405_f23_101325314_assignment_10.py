class game_start:
    def intro():
        print("""Welcome to the haunted mansion!
              You're an architect who has came here to examine the mansion for it's renovation.
              The house is old, creaky and falling apart. You walk in the front door and are in the entrance hall.
              The front door closes up and it's knob falls out so you cannot exit through front door
              While selecting your next room kindly make sure that the text is case sensitive kindly type the exact words as guided
              Here the game begins.... 
              """)
        

class map:
    def map(self):
            # Define connections between rooms
        game_map = {
            "Entrance Hall": ["Living Room", "Kitchen", "Library"],
            "Living Room": ["Entrance Hall", "Kitchen", "Master Bedroom", "Dining Room"],
            "Dining Room": ["Living Room", "Kitchen"],
            "Kitchen": ["Entrance Hall", "Living Room"],
            "Library": ["Entrance Hall", "Study"],
            "Study": ["Library", "Secret Room"],
            "Master Bedroom": ["Guest Bedroom", "Bathroom"],
            "Guest Bedroom": ["Master Bedroom", "Bathroom"],
            "Bathroom": ["Master Bedroom", "Guest Bedroom", "Secret Room"],
            "Powder Room": ["Entrance Hall", "Living Room"],
            "Conservatory": ["Living Room", "Game Room"],
            "Game Room": ["Conservatory", "Home Theater"],
            "Home Theater": ["Game Room", "Music Room"],
            "Music Room": ["Home Theater", "Art Gallery", "Exit"],
            "Art Gallery": ["Music Room", "Wine Cellar"],
            "Wine Cellar": ["Art Gallery", "Observatory"],
            "Observatory": ["Wine Cellar", "Gym"],
            "Gym": ["Observatory", "Attic"],
            "Secret Passage": ["Secret Room", "Wine Cellar"],
            "Attic": ["Gym"]
        }

        #initiate with user's initial position
        current_room = "Entrance Hall"
        while True:
            # know the next rooms the user can proceed to
            next_room = game_map[current_room]
            # take input from user of where he'd like to go
            user = input("Choose a room to proceed into(or 'quit' to exit the game): ")

            if user == 'quit':
                print("Thank you for playing!")
                break
            if 'Exit' in next_room:
                if user == "Exit":
                    print("Congratulations! You've made out of the mansion")

            if user in next_room:
                current_room = user
            else:
                print("Please select a room from given list")
            # give the user it's choices of the next possible room
            print(f"You're in the {current_room}, You can go to {next_room}")
map()        