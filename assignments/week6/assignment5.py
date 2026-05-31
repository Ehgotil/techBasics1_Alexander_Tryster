class TextAdventure:
    def __init__(self):
        self.inventory = None
        self.roach_effect = False
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
        print(f"--- {self.get_room()['name'].upper()} ---")
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
                    print(f"\n--- {self.get_room()['name'].upper()} ---")
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
                print("You try to use the knife, but you have nothing here to carve or cut.")
        elif item_name == "plasticine" and room["name"] == "laser tag":
            if "sharpened bone" in room["items"]:
                print("You have crafted a grapple. Maybe there is a place you could use it to climb out.")
                room["items"].remove("sharpened bone")
                self.inventory = "grapple"
            else:
                print("You mold the plasticine into a ball, but without a hook component, it's just a lump.")
        elif item_name == "grapple" and room["name"] == "parking garage":
            print("You climb up and out of the garage. The world awaits. Good luck out there.")
            self.inventory = None
            self.playing = False  # Ends the loop
        else:
            print(f"Using the {item_name} here doesn't seem to do anything.")
if __name__ == "__main__":
    game = TextAdventure()
    game.play()

# Gemini AI was used to help with more complex elements, such as consumable items and applying status effects to the player. Furthermore, it was used to explain parts of the code I was not able to understand on my own.