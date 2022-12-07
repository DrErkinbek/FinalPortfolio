#Header comments go here

#import main_character and section_2 here

#This start function is called by main_game.
#This will control the whole section.
#It'll need the player character as an input in order to interact with them.
def start():
    print("Your standing in the middle of small town")
    print("Where you would like to go?")
    choice = input("1. Rival's house 2.Take the route north")

    if choice == 1:
        print("You enter your arrival house. There is a young girl sitting at a table.")
        choice = input("Would you like to speak with her? Y/N")
        # If the player chooses to speak with her, the player gets a map
    elif choice == 2:
        print("You enter the lab and see people milling about")
        #Give the player the choice to talk to the people
    else:
        print("You try to take the route north")
    #Give the player some options of things to do here.
    #Be sure to put their choice in a variable!
    
    #Then use an if/elif/else statement to do something based on the player's choice.
    
    #One of the options should move the story to the next section with code like this:
    section_2.start()
    
    #Add pseudocode here to describe the rest of the functionality of this section of your game.
    #You may also draw and submit flowcharts if you prefer.
