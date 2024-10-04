def adventure_game():
    # Getting User's Name
    name = input("Enter your name: ")
    
    # Welcome the User
    print(f"Welcome, {name}, to this adventure, we will see the path that you choose based on your inputs.")
    
    # Asking for Direction
    direction = input("You come to a fork, Do you want to go left or right? ").lower()
    
    if direction == "left":
        # Left Path Decision
        river_choice = input("You reached a river. Do you want to 'walk' around river or 'swim' across? ").lower()
        
        if river_choice == "swim":
            print("sad, You were eaten by an alligator. You lose")
        elif river_choice == "walk":
            print("sad, You ran out of water while walking. You lose")
        else:
            print("Invalid choice You lose, retry or choose correct option")
    
    elif direction == "right":
        # Right Path Decision
        bridge_choice = input("You come to a wobbly bridge. Do you want to 'cross' the bridge or 'back' away ").lower()
        
        if bridge_choice == "back":
            print("You backed away from the bridge. You lose")
        elif bridge_choice == "cross":
            stranger_choice = input("You cross the bridge and meet a stranger. Do you want to 'talk' to the stranger? ").lower()
            
            if stranger_choice == "talk":
                print("The stranger gives you gold and You win")
            elif stranger_choice == "not talk":
                print("The stranger is offended by your silence. You lose")
            else:
                print("Invalid choice You lose, retry or choose correct option")
        else:
            print("Invalid choice You lose, retry or choose correct option")
    
    else:
        print("Invalid choice You lose, retry or choose correct option")
    
    print(f"Thank you for playing, {name}")

# Starting game
adventure_game()
