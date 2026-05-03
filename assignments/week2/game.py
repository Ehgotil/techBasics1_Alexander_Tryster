import time

print("You are falling. Wind rushes around you, strands of your hair whipping past your vision. Windows rush past you, flitting images of people staring at you as you hurtle towards the ground. You awkwardly manoeuvre your body to see how far you still have to fall. In spite of your rapid acceleration, the ground is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket.")
time.sleep(1)
print("Which will you use?")
print("Type either 'handgun'(to use the handgun) or 'knife' (to use the knife) or 'rope' (to use the rope).")

choice = input("> ").strip().lower()


if choice == "handgun":
    print("\nYou flick off the safety and aim at the window below you. Squinting through one eye, you think you can make the shot. You flip yourself as close to the windows as you can and take the shot. The glass shatters and you slide into the building, your foot catching on the sharp shards surrounding your entry point. Blood running from the gashes on your ankle, you observe the room around you. There is a door to your left, a bookshelf to your right and a patch of drywall in front of you.")
    time.sleep(1)
    print("Type either 'door' (to go through the door) or 'bookshelf' (to use the bookshelf) or drywall (to break the drywall).")

    choice = input("> ").strip().lower()

    if choice == "door":
        print("\nYou carefully open the door and find yourself in an empty atrium. Two elevator doors are in front of you. You call both of them and thankfully the first one to arrive is empty. You ride it to the top floor and get out in a room teeming with guards. You fire your last bullets at two of them and launch yourself at the third, drawing your knife as you go. The third guard goes down and you roar as you pull the knife from his lifeless corpse, kicking the fourth guards legs out from under him. The fifth drops his gun and holds up his hands, but you have no time to waste, so you throw the knife and he drops, the blade sticking out between his eyes. You grab his gun and check the clip. It’s full. You move forwards, limping and leaving a trail of red droplets behind you. You push open a heavy vault door and find yourself opposite a safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
        time.sleep(1)
        try:
            code = int(input("What code will you enter? "))

            if 3984 <= code <= 4456:
                print("\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                time.sleep(1)
                print("Then it all rushes away and you snap back to reality.")
                time.sleep(1)
                print("You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
            else:
                print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                time.sleep(1)
                print("Click-click.")
                print("Game over.")

        except ValueError:
            print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
            time.sleep(1)
            print("Click-click.")
            print("Game over.")
    if choice == "bookshelf":
        print("\nYou hobble over to the bookshelf and wedge your fingers behind the heavy wooden frame. One strong push is all you need to tip it over and it tips over with a resounding crash, smashing through the flimsy floor beneath you and dropping you into a room full of guards. “Target has escaped, we are currently tracking their position”, on of them is saying, as you bury his comrades under a pile of floor, shelf and dramatic entrance. A grin flashes across the last guy’s face and he draws a hatchet from his belt, reflexes flashing into action. You raise your gun, but he throws the hatchet, knocking the firearm from your hand and crosses the distance between you in seconds, tackling you against the glass window. You feel it crack as you smack into it, but it still holds. He draws back a fist and you dodge, letting him crack his knuckles against the glass that cracks even further. He pulls back and you lash a kick against his knees, knocking him forward. His head goes through the glass and you grab his gun from his holster, holding him over the edge by his gun. He flashes you a bloody smile and yanks you out of the window with him as you both fall. You exchange blows, but ultimately he pulls you into a head butt and your retaliatory kick connects as you slowly black out.")
    if choice == "drywall":
        print("\nA guard is leaning against the wall, lighting his cigarette and relaxing on a smoke break. Your hands shoot through the thin wall and wrap around his face, snuffing out the cigarette and his oxygen supply. When he is no longer a threat, you follow your hands and survey the room you’re in. You seem to have entered a security room of sorts. There is a uniform hanging on a coat rack on one wall and a fresh clip on a desk, alongside a whiteboard filled with security codes. One of them is circled in red. It reads 3984 - 4456.")
        time.sleep(1)
        print("What will you do?")
        print("Type either 'uniform' (to take the uniform) or 'take clip' (to take the clip) or 'all' (to do all of the above).")
        choice = input("> ").strip().lower()
        if choice == "uniform":
            print("You slip on the uniform and head to the elevators. You take the elevator down and exit the building through the lobby, with nobody paying any attention to you. You find yourself in a parking lot and crouch down behind a dark red semi truck. There is a little house with a parking attendant in it across the lot and a little gate to your left.")
            time.sleep(1)
            print("What will you do?")
            print("Type either 'steal' (to steal the truck) or 'walk out' (to approach the guard) or 'jump' (to jump the gate).")
            choice = input("> ").strip().lower()
            if choice == "steal":
                print("You break the window next to you and slide behind the wheel and step on it, accelerating madly. With smoking wheels, you take off into downtown traffic. You expect to hear blaring sirens behind you, but none come. In fact, the entire city is eerily quiet. You pull up in a side street and leave the truck there. You jog the last few side streets home and drop down on your couch. You can’t believe you made it out. You crack open a can of soda and replay the events of the day in your head. You put down your can of beer and feel the adrenaline has worn off. You curl up on the couch and paradoxically, you feel like you are waking up. You feel cold and gusts are billowing around you. It’s almost like…")
                print("Please restart the experience and try again.)")
            choice = input("> ").strip().lower()
            if choice == "walk out":
                print("You walk out, passing the guard. Your breathing stays calm. You do not expect him to notice that you do not belong in the uniform you are wearing. You exit the complex and leave your notions of a heist behind. You shrug off the uniform in a back alley and head back home. You shower, pack a bag and head to a café to start studying. You get bored pretty quickly, but you keep going, because you need to graduate at some point. Not everybody can be a heisting prodigy. Some people need to do it the old-fashioned way.")
            if choice == "jump":
                print("You sneak across the lot, throwing glances over your shoulder, but the guard seems to pay you mind. One time it looks like he picks up the phone, but nothing happens, so you feel comfortable to clamber up and over the gate. You slip up once and tear your pants, but you have bigger fish to fry. You drop down into the weeds behind the gate and start jogging. The edge of the premises is in sight. You’re almost at the edge, when you hear someone coming. You duck down into the bushes and peer out from between the branches. A guy with a flat top and an insane grin is staring out from behind his shades. “You weren’t that dumb”, he says. “Almost got away with it, too. But sadly…” His voice trails off. He sighs and suddenly pulls out a handgun. Before you can react he has pulled the trigger and your whole world is going dark. In you final moments, you feel the wind whipping up and all of a sudden…")
                print("(Please restart the experience and try again.)")
        if choice == "take clip":
            print("You take the clip and head to the elevators. You ride it to the top floor and get out in a room teeming with guards. You fire your last bullets at two of them and launch yourself at the third, drawing your knife as you go. The third guard goes down and you roar as you pull the knife from his lifeless corpse, kicking the fourth guards legs out from under him. The fifth drops his gun and holds up his hands, but you have no time to waste, so you throw the knife and he drops, the blade sticking out between his eyes. You grab his gun and check the clip. It’s full. You move forwards, limping and leaving a trail of red droplets behind you. You push open a heavy vault door and find yourself opposite a safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
            time.sleep(1)
            print("What code will you enter?")
            try:
                code = int(input("What code will you enter? "))

                if 3984 <= code <= 4456:
                    print(
                        "\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                    time.sleep(1)
                    print("Then it all rushes away and you snap back to reality.")
                    time.sleep(1)
                    print(
                        "You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
                else:
                    print(
                        "\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                    time.sleep(1)
                    print("Click-click.")
                    print("Game over.")

            except ValueError:
                print(
                    "\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                time.sleep(1)
                print("Click-click.")
                print("Game over.")
        if choice == "all":
            print("You slip on the uniform and pocket the clip. Heading to the elevators, you head up and emerge in a room teeming with guards. They pay you no mind and you pass on into the vault without issue. As the vault closes behind you, you fire your remaining bullets into the two guards stationed there and they go down. There isa safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
            time.sleep(1)
            print("What code will you enter?")
            try:
                code = int(input("What code will you enter? "))

                if 3984 <= code <= 4456:
                    print(
                        "\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                    time.sleep(1)
                    print("Then it all rushes away and you snap back to reality.")
                    time.sleep(1)
                    print(
                        "You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
                else:
                    print(
                        "\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                    time.sleep(1)
                    print("Click-click.")
                    print("Game over.")

            except ValueError:
                print(
                    "\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                time.sleep(1)
                print("Click-click.")
                print("Game over.")
if choice == "knife":
    print("You pull the knife from your belt and ram it into the side of the building. The first blow does not land, but the second and third strike pierce the metal plates that coat the side of the building. Your momentum drags you downwards, leaving a deep furrow in your wake. You jolt to a stop, hanging on by a thread. There is a vent beside you and you pry the cover off it with one hand. Just when you think you can’t hold on any longer, the vent comes off and you pull yourself inside. You crawl a few feet and suddenly hear voices under you.")
    time.sleep(1)
    print("What will you do?")
    print("Type either ‘keep going’ (to keep going) or ‘break out’ (to break out of the vent here) or ‘listen’ (to listen).")
    choice = input("> ").strip().lower()

    if choice == "keep going":
        print("You crawl on and eventually hit a grate. You bash your head against it until it falls out. You drop out into what seems to be an office. You take a good look around. There is a door to your left, a bookshelf to your right and a patch of drywall in front of you.")
        time.sleep(1)
        print("What will you do?")
        print("Type either ‘door’ (to go through the door) or ‘bookshelf’ (to use the bookshelf) or ‘drywall’ (to break the drywall).")
        choice = input("> ").strip().lower()

        if choice == "door":
            print("\nYou carefully open the door and find yourself in an empty atrium. Two elevator doors are in front of you. You call both of them and thankfully the first one to arrive is empty. You ride it to the top floor and get out in a room teeming with guards. You fire your last bullets at two of them and launch yourself at the third, drawing your knife as you go. The third guard goes down and you roar as you pull the knife from his lifeless corpse, kicking the fourth guards legs out from under him. The fifth drops his gun and holds up his hands, but you have no time to waste, so you throw the knife and he drops, the blade sticking out between his eyes. You grab his gun and check the clip. It’s full. You move forwards, limping and leaving a trail of red droplets behind you. You push open a heavy vault door and find yourself opposite a safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
            time.sleep(1)
            try:
                code = int(input("What code will you enter? "))
                if 3984 <= code <= 4456:
                    print("\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                    time.sleep(1)
                    print("Then it all rushes away and you snap back to reality.")
                    time.sleep(1)
                    print("You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
                else:
                    print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                    time.sleep(1)
                    print("Click-click.")
                    print("Game over.")
            except ValueError:
                print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                time.sleep(1)
                print("Click-click.")
                print("Game over.")

        if choice == "bookshelf":
            print("\nYou hobble over to the bookshelf and wedge your fingers behind the heavy wooden frame. One strong push is all you need to tip it over and it tips over with a resounding crash, smashing through the flimsy floor beneath you and dropping you into a room full of guards. “Target has escaped, we are currently tracking their position”, on of them is saying, as you bury his comrades under a pile of floor, shelf and dramatic entrance. A grin flashes across the last guy’s face and he draws a hatchet from his belt, reflexes flashing into action. You raise your gun, but he throws the hatchet, knocking the firearm from your hand and crosses the distance between you in seconds, tackling you against the glass window. You feel it crack as you smack into it, but it still holds. He draws back a fist and you dodge, letting him crack his knuckles against the glass that cracks even further. He pulls back and you lash a kick against his knees, knocking him forward. His head goes through the glass and you grab his gun from his holster, holding him over the edge by his gun. He flashes you a bloody smile and yanks you out of the window with him as you both fall. You exchange blows, but ultimately he pulls you into a head butt and your retaliatory kick connects as you slowly black out.")

        if choice == "drywall":
            print("\nA guard is leaning against the wall, lighting his cigarette and relaxing on a smoke break. Your hands shoot through the thin wall and wrap around his face, snuffing out the cigarette and his oxygen supply. When he is no longer a threat, you follow your hands and survey the room you’re in. You seem to have entered a security room of sorts. There is a uniform hanging on a coat rack on one wall and a fresh clip on a desk, alongside a whiteboard filled with security codes. One of them is circled in red. It reads 3984 - 4456.")
            time.sleep(1)
            print("What will you do?")
            print("Type either 'uniform' (to take the uniform) or 'take clip' (to take the clip) or 'all' (to do all of the above).")
            choice = input("> ").strip().lower()

            if choice == "uniform":
                print("You slip on the uniform and head to the elevators. You take the elevator down and exit the building through the lobby, with nobody paying any attention to you. You find yourself in a parking lot and crouch down behind a dark red semi truck. There is a little house with a parking attendant in it across the lot and a little gate to your left.")
                time.sleep(1)
                print("What will you do?")
                print("Type either 'steal' (to steal the truck) or 'walk out' (to approach the guard) or 'jump' (to jump the gate).")
                choice = input("> ").strip().lower()
                if choice == "steal":
                    print("You break the window next to you and slide behind the wheel and step on it, accelerating madly. With smoking wheels, you take off into downtown traffic. You expect to hear blaring sirens behind you, but none come. In fact, the entire city is eerily quiet. You pull up in a side street and leave the truck there. You jog the last few side streets home and drop down on your couch. You can’t believe you made it out. You crack open a can of soda and replay the events of the day in your head. You put down your can of beer and feel the adrenaline has worn off. You curl up on the couch and paradoxically, you feel like you are waking up. You feel cold and gusts are billowing around you. It’s almost like…")
                if choice == "walk out":
                    print("You walk out, passing the guard. Your breathing stays calm. You do not expect him to notice that you do not belong in the uniform you are wearing. You exit the complex and leave your notions of a heist behind. You shrug off the uniform in a back alley and head back home. You shower, pack a bag and head to a café to start studying. You get bored pretty quickly, but you keep going, because you need to graduate at some point. Not everybody can be a heisting prodigy. Some people need to do it the old-fashioned way.")
                if choice == "jump":
                    print("You sneak across the lot, throwing glances over your shoulder, but the guard seems to pay you mind. One time it looks like he picks up the phone, but nothing happens, so you feel comfortable to clamber up and over the gate. You slip up once and tear your pants, but you have bigger fish to fry. You drop down into the weeds behind the gate and start jogging. The edge of the premises is in sight. You’re almost at the edge, when you hear someone coming. You duck down into the bushes and peer out from between the branches. A guy with a flat top and an insane grin is staring out from behind his shades. “You weren’t that dumb”, he says. “Almost got away with it, too. But sadly…” His voice trails off. He sighs and suddenly pulls out a handgun. Before you can react he has pulled the trigger and your whole world is going dark. In you final moments, you feel the wind whipping up and all of a sudden…")

            if choice == "take clip":
                print("You take the clip and head to the elevators. You ride it to the top floor and get out in a room teeming with guards. You fire your last bullets at two of them and launch yourself at the third, drawing your knife as you go. The third guard goes down and you roar as you pull the knife from his lifeless corpse, kicking the fourth guards legs out from under him. The fifth drops his gun and holds up his hands, but you have no time to waste, so you throw the knife and he drops, the blade sticking out between his eyes. You grab his gun and check the clip. It’s full. You move forwards, limping and leaving a trail of red droplets behind you. You push open a heavy vault door and find yourself opposite a safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
                time.sleep(1)
                try:
                    code = int(input("What code will you enter? "))
                    if 3984 <= code <= 4456:
                        print("\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                        time.sleep(1)
                        print("Then it all rushes away and you snap back to reality.")
                        time.sleep(1)
                        print("You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
                    else:
                        print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                        time.sleep(1)
                        print("Click-click.")
                        print("Game over.")
                except ValueError:
                    print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                    time.sleep(1)
                    print("Click-click.")
                    print("Game over.")

            if choice == "all":
                print("You slip on the uniform and pocket the clip. Heading to the elevators, you head up and emerge in a room teeming with guards. They pay you no mind and you pass on into the vault without issue. As the vault closes behind you, you fire your remaining bullets into the two guards stationed there and they go down. There isa safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
                time.sleep(1)
                try:
                    code = int(input("What code will you enter? "))
                    if 3984 <= code <= 4456:
                        print("\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                        time.sleep(1)
                        print("Then it all rushes away and you snap back to reality.")
                        time.sleep(1)
                        print("You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
                    else:
                        print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                        time.sleep(1)
                        print("Click-click.")
                        print("Game over.")
                except ValueError:
                    print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                    time.sleep(1)
                    print("Click-click.")
                    print("Game over.")

    if choice == "break out":
        print("You kick the vent until the metal plates give way and drop down on to two guards. One of them goes down to your kick, the other raises his hands. “Which way to the package?”, you ask. The guard just points to the right and you follow his direction, knocking him out and locking the door behind you. You head up a set of rickety iron steps and clamber through the skyscraper’s walls like the agile climber you are. You come out in another vent, looking through the grate as three guards carry a black briefcase through a narrow corridor. You pull out your handgun and take aim. The three men fall and you hop out of the vent. You open the briefcase and pull out a piece of paper. “Digital Media B.A.”, it says. You smile and pocket the degree. “Crazy what they make you do for this”, you mutter, climbing back into the vent. As your foot retreats into the safety of the ventilation system, you feel a hand close around your ankle. A man with a flat top and an insane grin winks at you from behind his sunglasses and pulls you out of the vent and throws a punch you only narrowly dodge. He wrestles you to the ground, but you kick him away and take off running. You bust through a door, slide over the table positioned there and kicking the guy at the desk into the window behind him. The window smashes and you hurl yourself into the air, turning to see the insane flat top get smaller and smaller as he stands by the ledge and watches you go. You turn back around and pull the rope, letting the parachute expand and slowly drifting off of the premises. As the city skyline comes closer and closer, you smile. You made it out. Now, finally, you can relax. (Delay.) Unbeknownst to you, the tracker on your foot beeps little blips into the aether.")

    if choice == "listen":
        print("You pause to listen. Two guards are talking. “You hear they’re changing the code today?”, one of them asks. “Why?”, the other replies. “As soon as the package is in the safe, we’re upping the security.” One of them lowers his voice to a whisper. “So what’s the new code?” The other grunts. “Nobody’s told. Everyone gets a personalised code. Yours should be in your e-mail” The other says nothing. You assume he is checking his e-mail. “Four… Two… Five… Eight…”, he reads out loud. You hear a slapping sound and his comrade begins to chastise him, but you have what you need. Time to move on. You keep crawling through the vent, glance at a possible exit in an office, but choose to keep going. You see a security room with a guard in it and decide it is not worth the hassle. You shimmy up a vent that seems to stretch into the skies above, but eventually you can look into the vault, where two guards have their back to you. You bide your time and wait, until they eventually leave, sealing the vault door behind them. You drop down and see a safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
        time.sleep(1)
        try:
            code = int(input("What code will you enter? "))
            if 3984 <= code <= 4456:
                print("\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                time.sleep(1)
                print("Then it all rushes away and you snap back to reality.")
                time.sleep(1)
                print("You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
            else:
                print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                time.sleep(1)
                print("Click-click.")
                print("Game over.")
        except ValueError:
            print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
            time.sleep(1)
            print("Click-click.")
            print("Game over.")
if choice == "rope":
    print("You give the rope a sharp yank and the parachute sown into the back of your jacket expands. You feel a sharp jolt in your abdomen as your fall is broken and you begin to drift downwards. The fall is slow and eventually your feet touch down on rough concrete. You find yourself in a parking lot and crouch down behind a dark red semi truck. You discard your parachute and stuff it into the truck bed. There is a little house with a parking attendant in it across the lot and a little gate to your left.")
    time.sleep(1)
    print("What will you do?")
    print("Type either ‘steal’ (to steal the truck) or ‘approach’ (to approach the guard) or ‘jump’ (to jump the gate). ")
    choice = input("> ").strip().lower()

    if choice == "steal":
        print("You break the window next to you and slide behind the wheel and step on it, accelerating madly. With smoking wheels, you take off into downtown traffic. You expect to hear blaring sirens behind you, but none come. In fact, the entire city is eerily quiet. You pull up in a side street and leave the truck there. You jog the last few side streets home and drop down on your couch. You can’t believe you made it out. You crack open a can of soda and replay the events of the day in your head. You put down your can of beer and feel the adrenaline has worn off. You curl up on the couch and paradoxically, you feel like you are waking up. You feel cold and gusts are billowing around you. It’s almost like…")
        print("(Please restart the experience and try again.)")

    if choice == "approach":
        print("You crouch-walk across the lot, ducking from car to car until you’re in range of the guard in his little house. You pull out your knife and start running. You kick off the ground and go flying, landing on top of the guy and impaling his head into the desk. His blood goes all over you, but none of it gets on his uniform. You clean yourself off and take the guard’s uniform. You look back at the skyscraper and sag when you realise you have already made up your mind. Check the clip, wipe off the blade and brace yourself, then it’s back to the belly of the beast. With the cap pulled low over your eyes, nobody pays attention to you. You get in the elevator and head up, emerging in a room teeming with guards. They pay you no mind and you pass on into the vault without issue. As the vault closes behind you, stab one of guards stationed there and choke out the other. In the room there is a safe imprinted against a gigantic glass window. The dial on the front shows numbers from 1000 to 4999. It seems you should enter a code in a certain range.")
        time.sleep(1)
        try:
            code = int(input("What code will you enter? "))
            if 3984 <= code <= 4456:
                print("\nThe safe opens and you take out a briefcase. Inside is a piece of paper. You read the words written on top: “Digital Media B.A.” “Finally”, you murmur. The paper begins to glow and red light envelops you. Bolts of crimson light arc around you, sparks flying off the walls. Your feet leave the ground as you rise up, spinning like you are stuck in a centrifuge. The entire room begins to twist inwards and a series of loud cracking sounds echo around in your eardrums. You feel like you can’t breathe and begin to choke up. Tears stream down your face and you can feel your skin burning. Everything gets very hot and you can feel your heart burning in your chest. The pressure builds until it is unbearable. Your vision goes black and you collapse.")
                time.sleep(1)
                print("Then it all rushes away and you snap back to reality.")
                time.sleep(1)
                print("You are flying. Wind rushes around you, strands of your hair whipping past your vision. Planets rush past you, flitting images of civilisations rising and falling past you as you hurtle towards something beyond our comprehension. You awkwardly manoeuvre your body to see how far you still have to fly. In spite of your rapid acceleration, the incomprehensible is still far off. You pat down your pockets and bring out three items: A handgun, a military knife and three inches of black rope trailing from the inner lining of your jacket. You drop the gun and the knife and slip out of your jacket. You have no need for such toys now. You have ascended.")
            else:
                print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
                time.sleep(1)
                print("Click-click.")
                print("Game over.")
        except ValueError:
            print("\nThat’s not the code. You mutter a swear word I cannot write in an assignment. A red light on the ceiling starts to flash and a siren blares deep inside the maze of rooms you have overcome to get this far. You force yourself to slow your breathing and remain calm. Slowly, you see the vault door swing open. You do not know who or what is behind it, but they sure as hell will not be good news. You pull the gun from your waistband and flick off the safety. Check the clip.")
            time.sleep(1)
            print("Click-click.")
            print("Game over.")

    if choice == "jump":
        print("You sneak across the lot, throwing glances over your shoulder, but the guard seems to pay you mind. One time it looks like he picks up the phone, but nothing happens, so you feel comfortable to clamber up and over the gate. You slip up once and tear your pants, but you have bigger fish to fry. You drop down into the weeds behind the gate and start jogging. The edge of the premises is in sight. You’re almost at the edge, when you hear someone coming. You duck down into the bushes and peer out from between the branches. A guy with a flat top and an insane grin is staring out from behind his shades. “You weren’t that dumb”, he says. “Almost got away with it, too. But sadly…” His voice trails off. He sighs and suddenly pulls out a handgun. Before you can react he has pulled the trigger and your whole world is going dark. In you final moments, you feel the wind whipping up and all of a sudden… ")
        print("(Please restart the experience and try again.)")