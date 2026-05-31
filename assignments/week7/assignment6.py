import csv
import datetime
import os
import time
# This imports all the necessary libraries for the additions to the code to function properly.
SCOREBOARD_FILE = "scoreboard.csv" # This defines the file that will be used to make the scoreboard work.
DEBUG = True # This sets debug to true, meaning the program checks whether the condition of debug is fulfilled (in this case it is) and if it is fulfilled, then it skips most of the game and takes you straight to the leaderboard.


def init_scoreboard():
    if not os.path.exists(SCOREBOARD_FILE):
        try:
            with open(SCOREBOARD_FILE, mode="w", newline="", encoding="utf-8") as file:
                csv.writer(file).writerow(["Player Name", "Timestamp", "Time (seconds)"])
            print(f"Initialized new leaderboard file: {SCOREBOARD_FILE}")
        except IOError as e:
            print(f"Error initializing scoreboard file: {e}")
    else:
        print("Leaderboard file detected and ready.")
# This statement was made using Gemini AI. It defines the scoreboard and opens the CSV file that the game uses to save information to the scoreboard.

def save_score(player_name, completion_time):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(SCOREBOARD_FILE, mode="a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([player_name, current_time, f"{completion_time:.2f}"])
        print(f"\nScore saved for {player_name}!")
    # This statement builds upon the things established in the block above and is the function that the game calls to save the score at the end of a run.
    except IOError as e:
        print(f"Error saving score: {e}")
def display_leaderboard(top_n=5):
    if not os.path.exists(SCOREBOARD_FILE):
        return
    scores = []
    try:
        with open(SCOREBOARD_FILE, mode="r", encoding="utf-8") as file:
            reader = csv.reader(file)
            next(reader, None)
            for row in reader:
                if len(row) >= 3:
                    scores.append((row[0], row[1], float(row[2])))
    except (IOError, ValueError) as e:
        print(f"Error reading leaderboard data: {e}")
        return
    scores.sort(key=lambda x: x[2])
    print("\nSCOREBOARD... for the losers who care.")
    print(f"{'Rank':<5} {'Player':<15} {'Date/Time':<20} {'Time':<10}")
    print("-" * 52)
    for rank, (name, item_time, p_time) in enumerate(scores[:top_n], start=1):
        print(f"{rank:<5} {name:<15} {item_time:<20} {p_time:<10.2f}s")
    print("-" * 52 + "\n")
# This function displays the scoreboard at the end of a run and adds the flavour text to give the scoreboard some personality.
class TextAdventure:
    def __init__(self):
        self.inventory = None
        self.roach_effect = False
        self.player_name = "anonymous"
        self.start_time = 0.0 # This sets the start time to 0. This ensures the timer at the end is correct.
        self.locations = [
            {
                "name": "candy store",
                "description": "The candy store is old and overrun with roaches, greedily feasting on melted globs of coagulated sugar.",
                "exits": ["diner", "parking garage"],
                "items": ["lollipop"]
            },
            {
                "name": "diner",
                "description": "The diner is old and abandoned, decaying mold creeping up the walls and permeating the air with a pungent stench.",
                "exits": ["candy store", "parking garage"],
                "items": ["chicken leg"]
            },
            {
                "name": "parking garage",
                "description": "The parking garage is empty. All of the cars have been towed away, leaving blackened asphalt in their wake...",
                "exits": ["diner", "laser tag"],
                "items": ["knife"]
            },
            {
                "name": "laser tag",
                "description": "The laser tag joint looks like what it is: Abandoned. Plastic weapons are strewn about on the ground...",
                "exits": ["parking garage", "candy store"],
                "items": ["plasticine"]
            }
        ]
        self.current_location_idx = 0
        self.playing = True

    def get_room(self):
        return self.locations[self.current_location_idx]

    def play(self):
        print("You find yourself in an abandoned shopping mall. You can only hold one item at once.\n")

        name_input = input("What's your name, kiddo? ").strip()
        if name_input:
            self.player_name = name_input
        if DEBUG:
            print(f"\n[DEBUG MODE ACTIVE] Skipping game loop for {self.player_name}...")
            save_score(self.player_name, 12.34)
            display_leaderboard()
            return
        self.start_time = time.perf_counter() # This is where the timer for the game begins.
        print(f"\nHello, {self.player_name}. I've been waiting for you. This is your first test. Meet me on the outside and maybe we'll talk. May good fortune be with you. The gods certainly aren't.") # Here a question and function was added that lets the player name themselves. The integration was aided by Gemini AI.
        print(f"\n{self.get_room()['name'].upper()}\n{self.get_room()['description']}")
        while self.playing:
            user_input = input("\nWhat do you want to do? ").strip().lower()
            if not user_input:
                continue
            parts = user_input.split(" ", 1)
            command = parts[0]
            argument = parts[1] if len(parts) > 1 else ""
            commands = {
                "go": self.go_to,
                "search": self.search_room,
                "get": self.get_item,
                "drop": self.drop_item,
                "use": self.use_item
            }
            if command in commands:
                commands[command](argument)
            else:
                print("Unknown command. Try: go [room], search [room], get [item], drop [item], or use [item].")
    def go_to(self, room_name):
        room = self.get_room()
        if room_name in room["exits"]:
            self.current_location_idx = next(i for i, loc in enumerate(self.locations) if loc["name"] == room_name)
            print(
                f"\nYou travel to the {room_name}.\n\n{self.get_room()['name'].upper()}\n{self.get_room()['description']}")
        else:
            print(f"You can't go to '{room_name}' from here. Available exits: {', '.join(room['exits'])}")

    def search_room(self, room_name):
        room = self.get_room()
        if room_name != room["name"]:
            print(f"You aren't in the '{room_name}' to search it.")
        else:
            print(f"In the {room['name']}, you see: {', '.join(room['items'])}" if room[
                "items"] else f"The {room['name']} has no items lying around.")

    def get_item(self, item_name):
        room = self.get_room()
        if item_name not in room["items"]:
            print(f"There is no '{item_name}' here.")
        elif self.inventory:
            print(f"Your inventory is full! You are currently carrying a {self.inventory}.")
        else:
            room["items"].remove(item_name)
            self.inventory = item_name
            print(f"You pick up the {item_name}.")

    def drop_item(self, item_name):
        if self.inventory != item_name:
            print(f"You aren't holding a '{item_name}'.")
        else:
            self.get_room()["items"].append(item_name)
            self.inventory = None
            print(f"You dropped the {item_name} in the {self.get_room()['name']}.")

    def use_item(self, item_name):
        if self.inventory != item_name:
            print(f"You need to 'get' the {item_name} before you can use it.")
            return

        room = self.get_room()
        r_name = room["name"]

        if item_name == "lollipop" and r_name == "candy store":
            print("The roaches swarm up to the sweet treat... You should get them something to eat.")
            self.inventory = None
            self.roach_effect = True
        elif item_name == "chicken leg" and r_name == "diner":
            if self.roach_effect:
                print("The roaches crawl down your arms and dig into the chicken... You receive a bone.")
                self.inventory = "bone"
            else:
                print("You don't have any reason to use the chicken leg right now.")
        elif item_name == "knife" and r_name == "parking garage":
            if "bone" in room["items"]:
                print("You carve the bone into a makeshift hook. You have crafted a sharpened bone.")
                room["items"].remove("bone")
                self.inventory = "sharpened bone"
            else:
                print("You have a knife, but what does the sharpness of the blade matter when it has nothing to cut?")
        elif item_name == "plasticine" and r_name == "laser tag":
            if "sharpened bone" in room["items"]:
                print("You have crafted a grapple. There's gotta be a place you can climb with this.")
                room["items"].remove("sharpened bone")
                self.inventory = "grapple"
            else:
                print("It's just plasticine. You're gonna need something else to make this work.")
        elif item_name == "grapple" and r_name == "parking garage":
            elapsed_time = time.perf_counter() - self.start_time
            print(
                f"\nYou climb up and out of the garage. The world awaits.\nTook your time, though. {elapsed_time:.2f} seconds is quite slow.")
            save_score(self.player_name, elapsed_time)
            display_leaderboard()
            self.inventory = None
            self.playing = False
        else:
            print(f"Don't use {item_name} here, dummy!")


if __name__ == "__main__":
    init_scoreboard()
    game = TextAdventure()
    game.play()
# Gemini AI was used to iterate upon ideas created by myself. Furthermore, it was specifically used to identify the best ways to implement files and the concept of a scoreboard. Furthermore, I simplified some of the code from the original game, using techniques that were aided by Gemini AI.