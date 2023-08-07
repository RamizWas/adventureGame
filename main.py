import time
import random

# List of ANSI escape codes for different colors
colors = [
    '\033[91m',  # Red
    '\033[92m',  # Green
    '\033[93m',  # Yellow
    '\033[94m',  # Blue
    '\033[95m',  # Magenta
    '\033[96m',  # Cyan
]


def print_delay(text, delay=0.05, color=random.choice(colors)):
    for char in text:
        if color:
            print(color + char + '\033[0m', end='', flush=True)
        else:
            print(char, end='', flush=True)
        time.sleep(delay)
    print()


def get_valid_input(message, options):
    while True:
        choice = input(message)
        if choice.isdigit() and int(choice) in options:
            return int(choice)
        else:
            print_delay("Invalid input. Please enter"
                        " a valid option.", color=random.choice(colors))


def start_game():
    print_delay("You find yourself on a mysterious island. It's getting"
                " dark, and you need to find shelter.")
    print_delay("To your left, you see a dense forest. "
                "To your right, there's a cave entrance.")
    print_delay("What would you like to do?")
    print_delay("1. Go into the forest.")
    print_delay("2. Enter the cave.")
    choice = get_valid_input("Enter the number of your choice: ", [1, 2])
    if choice == 1:
        explore_forest()
    elif choice == 2:
        explore_cave()


def explore_forest():
    encounter_animal = random.randint(0, 1)
    if encounter_animal:
        print_delay("As you venture deeper into the forest,"
                    " you encounter a wild animal!")
        print_delay("What would you like to do?")
        print_delay("1. Try to run away.")
        print_delay("2. Climb a tree to hide.")
        choice = get_valid_input("Enter the number of your choice: ", [1, 2])
        if choice == 1:
            print_delay("You couldn't outrun the animal."
                        " Game over!", color=colors[0])
            play_again()
            return
        elif choice == 2:
            print_delay("You successfully hide in the "
                        "tree until the animal goes away.")

    print_delay("You find a small path leading "
                "deeper into the forest.")
    print_delay("Do you want to follow the path "
                "or head back to the beach?")
    print_delay("1. Follow the path.")
    print_delay("2. Head back to the beach.")
    choice = get_valid_input("Enter the number of your choice: ", [1, 2])
    if choice == 1:
        find_treasure()
    elif choice == 2:
        print_delay("You head back to the beach"
                    " and wait for rescue.")
        play_again()
    else:
        print_delay("Invalid choice. Please try again.")
        explore_forest()


def explore_cave():
    print_delay("You enter a dark cave with "
                "mysterious echoes.")
    print_delay("As you walk deeper, you notice a "
                "glimmering light ahead.")
    print_delay("Do you want to investigate the "
                "light or turn back?")
    print_delay("1. Investigate the light.")
    print_delay("2. Turn back.")
    choice = get_valid_input("Enter the number of your choice: ", [1, 2])
    if choice == 1:
        investigate_shipwreck()
    elif choice == 2:
        print_delay("You decide it's too risky"
                    " and return to the beach.")
        beach()
    else:
        print_delay("Invalid choice. Please try again.")
        explore_cave()


def beach():
    print_delay("You are back on the sandy beach,"
                " where the waves gently crash against the shore.")
    print_delay("You see a shipwreck in the distance "
                "and a path leading into the forest.")
    print_delay("What would you like to do?")
    print_delay("1. Investigate the shipwreck.")
    print_delay("2. Follow the forest path.")
    choice = get_valid_input("Enter the number of your choice: ", [1, 2])
    if choice == 1:
        investigate_shipwreck()
    elif choice == 2:
        explore_forest()
    else:
        print_delay("Invalid choice. Please try again.")
        beach()


def investigate_shipwreck():
    print_delay("You carefully approach the shipwreck,"
                " navigating through debris and wreckage.")
    print_delay("You find a rusty key among the remains.")
    add_item("rusty key")
    print_delay("You decide to head back to the beach.")
    beach()


def find_treasure():
    print_delay("As you follow the path, you discover "
                "a hidden treasure chest!")
    chest_locked = random.choice([True, False])

    if chest_locked:
        print_delay("The chest is locked. You need to "
                    "find a key to unlock it.")
        if "rusty key" in inventory:
            print_delay("You use the rusty key to unlock the chest.")
            print_delay("Inside the chest, you find a valuable gemstone!")
            add_item("gemstone")
        else:
            print_delay("You don't have the key to unlock "
                        "the chest. Continue exploring.")
    else:
        print_delay("The chest is already unlocked. Inside,"
                    " you find a valuable gemstone!")
        add_item("gemstone")

    play_again()


def check_inventory():
    print_delay("You check your inventory:")
    if not inventory:
        print_delay("Your inventory is empty.")
    else:
        for item in inventory:
            print_delay("- " + item)


def add_item(item):
    inventory.append(item)
    print_delay(f"You've added {item} to your inventory.")


def use_item(item):
    if item == "rusty key":
        print_delay("You can't find a use for the rusty key right now.")
    elif item == "gemstone":
        print_delay("You admire the sparkling gemstone in your hand.")
    else:
        print_delay("You can't use that item.")


def combine_items(item1, item2):
    if item1 == "rusty key" and item2 == "gemstone":
        print_delay("You combine the rusty key and"
                    " the gemstone, but nothing happens.")
    else:
        print_delay("You can't combine these items.")


def play_again():
    print_delay("Would you like to play again?")
    print_delay("1. Yes")
    print_delay("2. No")
    choice = get_valid_input("Enter the number of your choice: ", [1, 2])
    if choice == 1:
        inventory.clear()
        if introduce_random_elements():
            start_game()
    elif choice == 2:
        print_delay("Thanks for playing. Goodbye!")
    else:
        print_delay("Invalid choice. Please try again.")
        play_again()


def introduce_random_elements():
    random.seed()  # Initialize random number generator
    # Add your random element introduction code here
    return True  # Replace with appropriate condition


inventory = []

if __name__ == "__main__":

    if introduce_random_elements():
        start_game()
