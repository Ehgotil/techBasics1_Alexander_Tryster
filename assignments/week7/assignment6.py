import csv
import datetime
import os
import time
# This imports all the necessary libraries for the additions to the code to function properly.
SCOREBOARD_FILE = "scoreboard.csv" # This defines the file that will be used to make the scoreboard work.

def init_scoreboard():
    if not os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Player Name", "Timestamp", "Time (seconds)"])
        print(f"Initialized new leaderboard file: {SCOREBOARD_FILE}")
    else:
        print("Leaderboard file detected and ready.")
# This statement was made using Gemini AI. It defines the scoreboard and opens the CSV file that the game uses to save information to the scoreboard.

def save_score(player_name, completion_time):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(SCOREBOARD_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([player_name, current_time, f"{completion_time:.2f}"])
    print(f"\nScore saved for {player_name}!")
# This statement builds upon the things established in the block above and is the function that the game calls to save the score at the end of a run.

def display_leaderboard(top_n=5):
    scores = []

    if not os.path.exists(SCOREBOARD_FILE):
        return

    with open(SCOREBOARD_FILE, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        try:
            next(reader)
        except StopIteration:
            return
        for row in reader:
            if len(row) < 3:
                continue
            player_name = row[0]
            timestamp = row[1]
            completion_time = float(row[2])
            scores.append((player_name, timestamp, completion_time))
    scores.sort(key=lambda x: x[2])
    top_scores = scores[:top_n]
    print("\nSCOREBOARD... for the losers who care")
    print(f"{'Rank':<5} {'Player':<15} {'Date/Time':<20} {'Time':<10}")
    print("-" * 52)
    for rank, score in enumerate(top_scores, start=1):
        name, item_time, p_time = score
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
                "description": "The parking garage is empty. All of the cars have been towed away, leaving blackened asphalt in their wake. Light shines down from above, giving you glimpses of passing clouds.",
                "exits": ["diner", "laser tag"],
                "items": ["knife"]
            },
            {
                "name": "laser tag",
                "description": "The laser tag joint looks like what it is: Abandoned. Plastic weapons are strewn about on the ground and creepy cardboard cutouts line the walls.",
                "exits": ["parking garage", "candy store"],
                "items": ["plasticine"]
            }
        ]

        self.current_location_idx = 0
        self.playing = True

    def get_room(self):
        return self.locations[self.current_location_idx]

    def play(self):
        print(
            "You find yourself in an abandoned shopping mall. You can only hold one item at once. You start in the candy store. Your goal is to escape. Which way will you go?\n")
        self.start_time = time.perf_counter() # This is where the timer for the game begins.
        name_input = input("What's your name, kiddo?").strip() # Here a question and function was added that lets the player name themselves. The integration was aided by Gemini AI.
        if name_input:
            self.player_name = name_input

        print(f"\nHello, {self.player_name}. I've been waiting for you. This is your first test. Meet me on the outside and maybe we'll talk. May good fortune be with you. The gods certainly aren't.")
        print(f"{self.get_room()['name'].lower()}")
        print(self.get_room()['description'])

        while self.playing:
            user_input = input("\nWhat do you want to do? ").strip().lower()
            if not user_input:
                continue
            parts = user_input.split(" ", 1)
            command = parts[0]
            argument = parts[1] if len(parts) > 1 else ""

            if command == "go":
                self.go_to(argument)
            elif command == "search":
                self.search_room(argument)
            elif command == "get":
                self.get_item(argument)
            elif command == "drop":
                self.drop_item(argument)
            elif command == "use":
                self.use_item(argument)
            else:
                print("Unknown command. Try: go [room], search [room], get [item], drop [item], or use [item].")

    def go_to(self, room_name):
        room = self.get_room()
        if room_name in room["exits"]:
            for idx, loc in enumerate(self.locations):
                if loc["name"] == room_name:
                    self.current_location_idx = idx
                    print(f"\nYou travel to the {room_name}.")
                    print(f"\n {self.get_room()['name'].lower()}")
                    print(self.get_room()['description'])
                    return
        else:
            print(f"You can't go to '{room_name}' from here. Available exits: {', '.join(room['exits'])}")

    def search_room(self, room_name):
        room = self.get_room()
        if room_name != room["name"]:
            print(f"You aren't in the '{room_name}' to search it.")
            return

        if room["items"]:
            print(f"In the {room['name']}, you see: {', '.join(room['items'])}")
        else:
            print(f"The {room['name']} has no items lying around.")

    def get_item(self, item_name):
        room = self.get_room()

        if item_name not in room["items"]:
            print(f"There is no '{item_name}' here.")
            return

        if self.inventory is not None:
            print(f"Your inventory is full! You can only hold one item. You are currently carrying a {self.inventory}.")
            return

        room["items"].remove(item_name)
        self.inventory = item_name
        print(f"You pick up the {item_name}.")

    def drop_item(self, item_name):
        if self.inventory != item_name:
            print(f"You aren't holding a '{item_name}'.")
            return

        room = self.get_room()
        room["items"].append(item_name)
        self.inventory = None
        print(f"You dropped the {item_name} in the {room['name']}.")

    def use_item(self, item_name):
        if self.inventory != item_name:
            print(f"You need to 'get' the {item_name} before you can use it.")
            return

        room = self.get_room()
        if item_name == "lollipop" and room["name"] == "candy store":
            print(
                "The roaches swarm up to the sweet treat, gnawing away at it as they go and once they are satisfied, settling on your shoulders and forearms. They seem like they're still hungry. You should get them something to eat.")
            self.inventory = None
            self.roach_effect = True
        elif item_name == "chicken leg" and room["name"] == "diner":
            if self.roach_effect:
                print(
                    "The roaches crawl down your arms and dig into the mouldy piece of chicken. Once they are done, you are left with the bone. It looks maleable. If only you had something sharp.")
                print("You receive a bone.")
                self.inventory = "bone"
            else:
                print("You don't have any reason to use the chicken leg right now.")
        elif item_name == "knife" and room["name"] == "parking garage":
            if "bone" in room["items"]:
                print(
                    "You carve the bone into a makeshift hook. The knife, rusty as it is, shatters once you are done. Now you just need something to make a handle.")
                print("You have crafted a sharpened bone.")
                room["items"].remove("bone")
                self.inventory = "sharpened bone"
            else:
                print("You have a knife, but what does the sharpness of the blade matter when it has nothing to cut?")
        elif item_name == "plasticine" and room["name"] == "laser tag":
            if "sharpened bone" in room["items"]:
                print("You have crafted a grapple. There's gotta be a place you can climb with this.")
                room["items"].remove("sharpened bone")
                self.inventory = "grapple"
            else:
                print("It's just plasticine. You're gonna need something else to make this work.")
        elif item_name == "grapple" and room["name"] == "parking garage":
            print("You climb up and out of the garage. The world awaits. Come see me, if you dare, kid.")
            end_time = time.perf_counter()
            elapsed_time = end_time - self.start_time # This and the line above end the timer once a run is completed, i.e. the player has successfully escaped.
            print(f"\n You made it. Took your time, though. {elapsed_time:.2f} seconds is quite slow.")
            self.inventory = None
            self.playing = False
        else:
            print(f"Don't use {item_name} here, dummy!")

if __name__ == "__main__":
    init_scoreboard()
    game = TextAdventure()
    game.play()

# Gemini AI was used to iterate upon ideas created by myself. Furthermore, it was specifically used to identify the best ways to implement files and the concept of a scoreboard.