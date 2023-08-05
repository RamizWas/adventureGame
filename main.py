import time
import turtle
import random


def print_delay(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


def draw_logo():
    screen = turtle.Screen()
    screen.bgcolor("white")

    # Set up the turtle
    logo_turtle = turtle.Turtle()
    logo_turtle.speed(0)
    logo_turtle.color("black")
    logo_turtle.penup()
    logo_turtle.hideturtle()

    # Define the ASCII art logo as a list of strings
    logo = [
        " ______   _______  __   __  _______  __   __  _______  __   __  _______ ",
        "|      | |   _   ||  | |  ||   _   ||  | |  ||       ||  | |  ||       |",
        "|  _    ||  |_|  ||  |_|  ||  |_|  ||  | |  ||   _   ||  |_|  ||_     _|",
        "| | |   ||       ||       ||       ||  |_|  ||  | |  ||       |  |   |  ",
        "| |_|   ||       ||       ||       ||       ||  |_|  ||       |  |   |  ",
        "|       ||   _   | |     | |   _   ||       ||       ||   _   |  |   |  ",
        "|______| |__| |__|  |___|  |__| |__||_______||_______||__| |__|  |___|  "
    ]

    # Set the starting position for drawing
    start_x, start_y = -220, 180
    x, y = start_x, start_y

    # Draw the logo character by character
    for line in logo:
        logo_turtle.goto(x, y)
        print_delay(line)
        y -= 25

    # Hide the turtle and display the logo
    logo_turtle.hideturtle()
    turtle.done()


def start_game():
    print_delay("You find yourself on a mysterious island. It's getting dark, and you need to find shelter.")
    print_delay("To your left, you see a dense forest. To your right, there's a cave entrance.")
    print_delay("What would you like to do?")
    print_delay("1. Go into the forest.")
    print_delay("2. Enter the cave.")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        explore_forest()
    elif choice == "2":
        explore_cave()
    else:
        print_delay("Invalid choice. Please try again.")
        start_game()


def explore_forest():
    encounter_animal = random.randint(0, 1)
    if encounter_animal:
        print_delay("As you venture deeper into the forest, you encounter a wild animal!")
        print_delay("What would you like to do?")
        print_delay("1. Try to run away.")
        print_delay("2. Climb a tree to hide.")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print_delay("You couldn't outrun the animal. Game over!")
            return
        elif choice == "2":
            print_delay("You successfully hide in the tree until the animal goes away.")

    print_delay("You find a small path leading deeper into the forest.")
    print_delay("Do you want to follow the path or head back to the beach?")
    print_delay("1. Follow the path.")
    print_delay("2. Head back to the beach.")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        find_treasure()
    elif choice == "2":
        print_delay("You head back to the beach and wait for rescue.")
    else:
        print_delay("Invalid choice. Please try again.")
        explore_forest()


def explore_cave():
    if "torch" in inventory:
        print_delay("Inside the dark cave, you can see better with your torch.")
        print_delay("You find a hidden passage!")
        print_delay("You venture further into the passage and discover a chest.")
        print_delay("With the chest in hand, you head back to the beach.")
        add_item("chest")
    else:
        print_delay("Inside the dark cave, you can barely see anything.")
        print_delay("You need a torch to light up the cave. Try finding one.")
        print_delay("You exit the cave and find yourself back at the beach.")
    beach()


def beach():
    print_delay("You are back at the beach.")
    print_delay("You can see a shipwreck in the distance.")
    print_delay("What would you like to do?")
    print_delay("1. Investigate the shipwreck.")
    print_delay("2. Explore the forest.")
    print_delay("3. Enter the cave.")
    print_delay("4. Check your inventory.")
    choice = input("Enter the number of your choice: ")
    if choice == "1":
        investigate_shipwreck()
    elif choice == "2":
        explore_forest()
    elif choice == "3":
        explore_cave()
    elif choice == "4":
        check_inventory()
    else:
        print_delay("Invalid choice. Please try again.")
        beach()


def investigate_shipwreck():
    print_delay("You swim out to the shipwreck and find some supplies.")
    print_delay("You also find a damaged diving suit.")
    add_item("diving suit")
    print_delay("You can now dive underwater.")
    beach()


def check_inventory():
    if not inventory:
        print_delay("Your inventory is empty.")
    else:
        print_delay("You have the following items in your inventory:")
        for item in inventory:
            print_delay(f"- {item}")
    beach()


def add_item(item):
    inventory.append(item)
    print_delay(f"You have obtained a {item}! It has been added to your inventory.")


def use_item(item):
    if item == "rusty key":
        print_delay("You use the rusty key to unlock an old chest.")
        if "old diary" in inventory:
            print_delay("Inside the chest, you find a map and a valuable gemstone!")
            add_item("treasure map")
            add_item("gemstone")
            print_delay("The chest is now empty.")
        else:
            print_delay("Inside the chest, you find an old diary.")
            add_item("old diary")
    elif item == "torch":
        print_delay("You light up the cave and can now see better.")
    elif item == "treasure map":
        print_delay("The map reveals the location of a hidden treasure.")
    elif item == "gemstone":
        print_delay("The gemstone sparkles beautifully.")
    elif item == "diving suit":
        print_delay("With the diving suit on, you can now explore underwater areas.")
    else:
        print_delay("You cannot use this item.")


def combine_items(item1, item2):
    if item1 == "old diary" and item2 == "treasure map":
        print_delay("You combine the old diary and the treasure map.")
        print_delay("The combined map reveals a secret path to a legendary sword.")
        add_item("legendary sword")
    else:
        print_delay("The combination does not yield any results.")


def introduce_random_elements():
    # Randomize the starting location of the rusty key
    if random.randint(0, 1) == 1:
        add_item("rusty key")
        print_delay("You find a rusty key lying on the beach.")

    # Randomize the encounter with a wild animal in the forest
    if random.randint(0, 1) == 1:
        print_delay("As you venture deeper into the forest, you encounter a wild animal!")
        print_delay("What would you like to do?")
        print_delay("1. Try to run away.")
        print_delay("2. Climb a tree to hide.")
        choice = input("Enter the number of your choice: ")
        if choice == "1":
            print_delay("You couldn't outrun the animal. Game over!")
            return False
        elif choice == "2":
            print_delay("You successfully hide in the tree until the animal goes away.")

    return True


inventory = []

if __name__ == "__main__":
    draw_logo()
    if introduce_random_elements():
        start_game()
