import time
import random  # Importing the random module to generate random events

# Function to print messages with a pause for dramatic effect
def print_pause(message, pause_time=1):
    print(message)
    time.sleep(pause_time)

# Function to display the game intro
def intro():
    print_pause("You find yourself with your friend in a Jungle.")
    print_pause("The Jungle is filled with strange noises.")
    print_pause("You and your friend possess strong courage. What do you do?")

# Function to get the player's main path choice
def get_path_choice():
    paths = ["near the village", "near the volcano"]
    print_pause(f"1. Go left {paths[0]}.")
    print_pause(f"2. Go right {paths[1]}.")

    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return "village"
        elif choice == "2":
            return "volcano"
        else:
            print_pause("Invalid input. Please enter 1 or 2.")

# Function to explore forest (village) area
def explore_forest_area():
    print_pause("You venture near the village...")
    print_pause("You see three paths ahead. What do you do?")
    print_pause("1. Go to the lake (potential treasure).")
    print_pause("2. Investigate the three statues (mystery).")
    print_pause("3. Follow the noises to an enigma (puzzle challenge).")

    while True:
        forest_choice = input("Enter 1, 2, or 3: ")
        if forest_choice == "1":
            explore_location("forest_lake", loot_range=(5, 15))
            break
        elif forest_choice == "2":
            explore_location("forest_statues", penalty_range=(2, 7))
            break
        elif forest_choice == "3":
            explore_location("forest_enigma", loot_range=(10, 20))
            break
        else:
            print_pause("Invalid input. Please enter 1, 2, or 3.")

# Function to explore volcano area
def explore_volcano_area():
    print_pause("You walk near the volcano...")
    print_pause("You spot three points of interest ahead. What do you do?")
    print_pause("1. Follow the heat to the volcano (dangerous exploration).")
    print_pause("2. Visit the witch (possible magic encounter).")
    print_pause("3. Approach the creepy place (mystical artifacts).")

    while True:
        meadow_choice = input("Enter 1, 2, or 3: ")
        if meadow_choice == "1":
            explore_location("forest_volcano", penalty_range=(5, 12))
            break
        elif meadow_choice == "2":
            explore_location("forest_witch", penalty_range=(6, 10))
            break
        elif meadow_choice == "3":
            explore_location("creepy_place", loot_range=(15, 25))
            break
        else:
            print_pause("Invalid input. Please enter 1, 2, or 3.")

# Function to show or update the score and evaluate end game
def check_score():
    print_pause(f"Your current score is: {score}")
    while True:
        print_pause("Do you want to return to the Jungle?")
        print_pause("1. Yes, keep exploring.")
        print_pause("2. No, end the adventure.")
        return_choice = input("Enter 1 or 2: ")
        if return_choice == "1":
            return True  # Continue game
        elif return_choice == "2":
            if score >= 20:
                print_pause("Congratulations! You won the game with a great score!")
            elif score <= 0:
                print_pause("You lost the game. Better luck next time!")
            else:
                print_pause("Game over! You neither won nor lost—try again to improve!")
            print_pause(f"Your final score is: {score}")
            print_pause("Thank you for playing! Goodbye!")
            return False  # Exit game
        else:
            print_pause("Invalid input. Please enter 1 or 2.")

# Function to handle location exploration dynamically with random descriptions
def explore_location(location_name, loot_range=None, penalty_range=None):
    global score  # Ensure score is updated globally
    if location_name in visited_places:
        print_pause(f"You've already explored {location_name}. No new discoveries.")
    else:
        # Randomized event descriptions
        event_descriptions = {
            "forest_lake": [
                "You find a peaceful lake reflecting the sky like a mirror.",
                "A hidden cave behind the waterfall contains ancient treasure!",
                "A mysterious ripple disturbs the water… something is lurking beneath."
            ],
            "forest_statues": [
                "The statues seem to whisper when the wind blows.",
                "You discover strange inscriptions on one of them—what could they mean?",
                "A buried chest lies near the statues, but opening it triggers a trap!"
            ],
            "forest_enigma": [
                "A cryptic puzzle appears on a stone tablet—can you solve it?",
                "A faint glow surrounds you as you step closer to the enigma.",
                "The markings change mysteriously—perhaps they reveal a hidden path?"
            ],
            "forest_volcano": [
                "The ground trembles as the volcano grumbles in the distance.",
                "You find an abandoned camp—who lived here before?",
                "A sudden gush of steam rises from the cracks beneath you!"
            ],
            "forest_witch": [
                "The witch hums an eerie tune—she seems to be expecting you.",
                "A glowing potion sits on a table—do you dare drink it?",
                "She offers you a choice: knowledge or magic—what will you take?"
            ],
            "creepy_place": [
                "A cursed amulet lies half-buried in the dirt.",
                "Ghostly whispers surround you… are you truly alone?",
                "A collection of mystical artifacts gleams under the dim moonlight."
            ]
        }

        # Select a random description for the visited location
        if location_name in event_descriptions:
            print_pause(random.choice(event_descriptions[location_name]))

        # Apply loot or penalty effects
        if loot_range:
            score_change = random.randint(loot_range[0], loot_range[1])
        elif penalty_range:
            score_change = -random.randint(penalty_range[0], penalty_range[1])
        else:
            score_change = 0
        
        score += score_change
        visited_places.add(location_name)

# Main function for the adventure game
def adventure_game():
    global score  # Define score globally for easy modification
    score = 0  # Initialize the player's score
    global visited_places
    visited_places = set()  # Track visited locations to prevent repeating events

    while True:
        intro()
        path = get_path_choice()

        if path == "village":
            explore_forest_area()
        elif path == "volcano":
            explore_volcano_area()

        if not check_score():
            break

# Run the game
adventure_game()
