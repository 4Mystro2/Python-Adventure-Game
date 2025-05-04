import time
import random  # Importing the random module to generate random events

# Function to print messages with a pause for dramatic effect
def print_pause(message, pause_time=1):
    print(message)
    time.sleep(pause_time)

# Main function for the adventure game
def adventure_game():
    score = 0  # Initialize the player's score
    visited_places = set()  # Track visited locations to prevent repeating events

    while True:
        print_pause("You find yourself with your friend in a Jungle.")
        print_pause("The Jungle is filled with strange noises.")
        print_pause("You and your friend possess strong courage. What do you do?")
        
        # Creating dynamic starting paths to make each playthrough unique
        paths = ["near the village", "near the volcano"]
        chosen_path = random.choice(paths)  # Randomly selecting a path
        print_pause(f"1. Go left {paths[0]}.")
        print_pause(f"2. Go right {paths[1]}.")

        while True:
            choice = input("Enter 1 or 2: ")
            if choice == "1":
                print_pause("You venture near the village...")
                print_pause("Strange noises surround you.")
                print_pause("You see three paths ahead. What do you do?")
                print_pause("1. Go to the lake (potential treasure).")
                print_pause("2. Investigate the three statues (mystery).")
                print_pause("3. Follow the noises to an enigma (puzzle challenge).")

                while True:
                    forest_choice = input("Enter 1, 2, or 3: ")
                    if forest_choice == "1":
                        if "forest_lake" in visited_places:
                            print_pause("You've already visited the lake. There's nothing new here.")
                        else:
                            print_pause("You find a beautiful lake with a hidden cave behind it. Inside, you discover a great deal of loot!")
                            score += random.randint(5, 15)  # Randomizing the loot value
                            visited_places.add("forest_lake")  # Mark the place as visited
                        break
                    elif forest_choice == "2":
                        if "forest_statues" in visited_places:
                            print_pause("You've already approached the statues. Nothing new remains.")
                        else:
                            print_pause("You examine the three statues and discover a treasure chest. However, it's trapped!")
                            score -= random.randint(2, 7)  # Randomizing the trap damage
                            visited_places.add("forest_statues")  
                        break
                    elif forest_choice == "3":
                        if "forest_enigma" in visited_places:
                            print_pause("You've already solved the enigma. No treasure left.")
                        else:
                            print_pause("You solve the enigma and find a big treasure chest full of gold.")
                            score += random.randint(10, 20)  # Randomizing the treasure value
                            visited_places.add("forest_enigma")  
                        break
                    else:
                        print_pause("Invalid input. Please enter 1, 2, or 3.")
                break

            elif choice == "2":
                print_pause("You walk near the volcano...")
                print_pause("The temperature is scorching hot.")
                print_pause("You spot three points of interest ahead. What do you do?")
                print_pause("1. Follow the heat to the volcano (dangerous exploration).")
                print_pause("2. Visit the witch (possible magic encounter).")
                print_pause("3. Approach the creepy place (mystical artifacts).")

                while True:
                    meadow_choice = input("Enter 1, 2, or 3: ")
                    if meadow_choice == "1":
                        if "forest_volcano" in visited_places:
                            print_pause("You've already explored the volcano. No new discoveries.")
                        else:
                            print_pause("You reach a burned village near the volcano. The sight fills you with sorrow.")
                            score -= random.randint(5, 12)  # Randomizing emotional impact
                            visited_places.add("forest_volcano")  
                        break
                    elif meadow_choice == "2":
                        if "forest_witch" in visited_places:
                            print_pause("You've already met the witch. No new events.")
                        else:
                            print_pause("The witch casts a spell on you!")
                            score -= random.randint(6, 10)  # Randomizing magic damage
                            visited_places.add("forest_witch")  
                        break
                    elif meadow_choice == "3":
                        if "Creepy_place" in visited_places:
                            print_pause("You've already explored the creepy place. Nothing new remains.")
                        else:
                            print_pause("In the eerie place, you uncover a magic ward, increasing your energy!")
                            score += random.randint(15, 25)  # Randomizing magical boost
                            visited_places.add("Creepy_place")  
                        break
                    else:
                        print_pause("Invalid input. Please enter 1, 2, or 3.")
                break

            else:
                print_pause("Invalid input. Please enter 1 or 2.")

        # Display the player's current score after each adventure
        print_pause(f"Your current score is: {score}")

        # Ask if the player wants to continue exploring
        print_pause("Do you want to return to the Jungle?")
        print_pause("1. Yes, keep exploring.")
        print_pause("2. No, end the adventure.")

        while True:
            return_choice = input("Enter 1 or 2: ")
            if return_choice == "1":
                break  # Restart the game loop
            elif return_choice == "2":
                # Determine the player's outcome based on their final score
                if score >= 20:
                    print_pause("Congratulations! You won the game with a great score!")
                elif score <= 0:
                    print_pause("You lost the game. Better luck next time!")
                else:
                    print_pause("Game over! You neither won nor lost—try again to improve!")
                print_pause(f"Your final score is: {score}")
                print_pause("Thank you for playing! Goodbye!")
                return  # End the game
            else:
                print_pause("Invalid input. Please enter 1 or 2.")

# Run the game
adventure_game()
