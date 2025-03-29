import random
import time

# ---- CLASS DEFINITIONS ----
class Character:
    def __init__(self, name, strength, intelligence, charisma, leadership):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma
        self.leadership = leadership
        self.health = 100 + strength * 2  # Health increases with strength
        self.morale = 100
        self.morality = 0  # Neutral starting point
        self.inventory = []
        self.occult_knowledge = 0
        self.faction = None
        self.reputation = 0  # Reputation with factions

    def level_up(self, attribute):
        if attribute == "Strength":
            self.strength += 1
        elif attribute == "Intelligence":
            self.intelligence += 1
        elif attribute == "Charisma":
            self.charisma += 1
        elif attribute == "Leadership":
            self.leadership += 1
        print(f"{self.name}'s {attribute} has increased!")

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            print(f"{self.name} uses {item}!")
            self.inventory.remove(item)
        else:
            print("Item not in inventory.")

    def change_faction(self, faction):
        self.faction = faction
        print(f"{self.name} has joined the {faction} faction!")

# ---- ENEMY CLASS ----
class Enemy:
    def __init__(self, name, health, strength, is_boss=False):
        self.name = name
        self.health = health
        self.strength = strength
        self.is_boss = is_boss

    def attack(self, player):
        damage = random.randint(self.strength - 5, self.strength + 5)
        player.health -= damage
        print(f"{self.name} attacks {player.name} for {damage} damage!")

    def is_alive(self):
        return self.health > 0

# ---- LOCATION FUNCTIONS WITH SECRETS AND EASTER EGGS ----
def explore_village(player):
    print("\nYou arrive in a war-torn village. The people look wary but desperate.")
    print("A local elder approaches and offers to help your cause.")
    choice = input("Do you want to speak to the elder? (yes/no): ").lower()

    if choice == "yes":
        print("\nThe elder shares valuable information about nearby factions.")
        player.add_item("Map of Factions")
        player.reputation += 5
    else:
        print("\nYou walk past the elder, noticing the distrust in the air.")
    
    # Easter Egg: Hidden Item
    if random.random() < 0.1:  # 10% chance to find hidden artifact
        print("\nWhile walking around, you find an old, rusted artifact buried in the dirt.")
        player.add_item("Ancient Artifact")
        print("This artifact looks strangely futuristic...")

def explore_forest(player):
    print("\nYou enter a dark forest, the trees twisted and ancient.")
    choice = input("Do you want to proceed deeper into the forest? (yes/no): ").lower()

    if choice == "yes":
        print("\nYou encounter a strange figure. It's an occultist who offers you forbidden knowledge.")
        print("You learn a dark spell that can influence people's minds.")
        player.level_up("Occult Knowledge")
    else:
        print("\nYou decide not to take any chances and head back to the village.")

    # Foreshadowing for Sequel: A strange symbol is carved into the tree.
    if random.random() < 0.15:  # 15% chance to find a hidden symbol
        print("\nYou notice a strange symbol carved into one of the trees. It seems to glow faintly, like a warning.")
        print("Perhaps you will encounter this symbol again...")

def recruit_ally(player):
    print("\nYou meet a skilled warrior in a tavern. He offers to join your faction, but only if you prove your strength.")
    choice = input("Do you accept his challenge? (yes/no): ").lower()

    if choice == "yes":
        print("\nYou fight the warrior in a one-on-one duel. You barely win, but he joins your ranks.")
        player.add_item("Skilled Warrior")
    else:
        print("\nThe warrior looks disappointed, but leaves without further conflict.")
    
    # Easter Egg: The warrior mentions something strange.
    if random.random() < 0.1:
        print("\nBefore he leaves, the warrior whispers, 'I've heard strange things... about the sky. Something is coming.'")
        
def rival_faction(player):
    print("\nYou encounter a rival faction's leader. They offer an alliance, but at a price.")
    choice = input("Do you wish to form an alliance? (yes/no): ").lower()

    if choice == "yes":
        player.change_faction("Rival Faction")
        print("\nYou now have new resources but at the cost of your reputation.")
    else:
        print("\nThe rival leader scoffs at your decision. You’ve made an enemy today.")
        player.reputation -= 10
    
    # Easter Egg: The rival leader has an unusual piece of technology on their desk.
    if random.random() < 0.05:
        print("\nAs the rival leader leaves, you catch a glimpse of a strange device on their desk. It looks like a futuristic communicator.")
        print("It might be something important...")

# ---- COMBAT SYSTEM ----
def combat(player, enemy):
    print(f"\n{player.name} encounters {enemy.name}!")
    while player.health > 0 and enemy.is_alive():
        print("\nChoose your action:")
        print("1) Attack")
        print("2) Use Item")
        print("3) Flee")
        action = input("Enter choice (1/2/3): ")

        if action == "1":
            damage = random.randint(10, 20) + player.strength
            enemy.health -= damage
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")
        elif action == "2":
            if player.inventory:
                item = input(f"Choose an item to use: {', '.join(player.inventory)}: ").capitalize()
                player.use_item(item)
            else:
                print("You have no items in your inventory.")
        elif action == "3":
            print(f"{player.name} attempts to flee!")
            break
        else:
            print("Invalid action.")

        if enemy.is_alive():
            enemy.attack(player)

        if player.health <= 0:
            print(f"{player.name} has been defeated!")
            return False
    if enemy.is_alive() == False:
        print(f"{enemy.name} has been defeated!")
    return True


# ---- FINAL BOSS BATTLE ----
def final_boss_battle(player):
    print("\nThe final battle is here... face your destiny.")
    dark_lord = Enemy("Dark Lord", 300, 50, is_boss=True)
    combat(player, dark_lord)

    if player.health <= 0:
        print("\nYou have been defeated by the Dark Lord. The world falls into chaos.")
    else:
        print("\nThe Dark Lord proves unbeatable. Despite your efforts, the end is inevitable.")
        print("\nThe sky grows dark as the world braces for destruction. Your death is a sacrifice.")

# ---- GAME FLOW ----
def ending_scene(player):
    print("\nThe world is at peace for now, but at what cost?")
    print(f"{player.name} has sacrificed everything to unite the Balkans.")
    print("But a greater darkness looms on the horizon...")
    print("\nYour efforts have paved the way for something far greater. Thank you for playing!")
    print("\n* * * * *")
    print("Be ready for what comes next...")

def allocate_stats():
    print("\nAllocate 15 points to your stats:")
    stats = {"Strength": 0, "Intelligence": 0, "Charisma": 0, "Leadership": 0}
    remaining_points = 15

    while remaining_points > 0:
        print("\nCurrent stats: ", stats)
        print(f"Points remaining: {remaining_points}")
        stat_choice = input("Which stat would you like to increase? (Strength/Intelligence/Charisma/Leadership): ").capitalize()

        if stat_choice in stats and stats[stat_choice] < 10:
            points = int(input(f"How many points do you want to add to {stat_choice}? (Remaining: {remaining_points}): "))
            if points <= remaining_points and points >= 0:
                stats[stat_choice] += points
                remaining_points -= points
            else:
                print("Invalid input. Please enter a valid number of points.")
        else:
            print("Invalid stat choice or max stat reached.")

    return stats


def main():
    print("Welcome to Shadows of the Balkans!")
    player_name = input("Enter your leader's name: ")

    stats = allocate_stats()
    player = Character(player_name, stats["Strength"], stats["Intelligence"], stats["Charisma"], stats["Leadership"])

    # Start Game
    explore_village(player)
    explore_forest(player)
    recruit_ally(player)
    rival_faction(player)
    
    final_boss_battle(player)
    ending_scene(player)

if __name__ == "__main__":
    main()
