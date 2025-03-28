import random

# Character Classes
class Character:
    def __init__(self, name, strength, intelligence, charisma, leadership, faction=None):
        self.name = name
        self.strength = strength
        self.intelligence = intelligence
        self.charisma = charisma
        self.leadership = leadership
        self.health = 100
        self.morale = 100  # This will affect dialogue and decisions
        self.inventory = []  # Adding inventory to hold items
        self.morality = 0  # 0 is neutral, +1 is good, -1 is evil
        self.faction = faction  # Faction alignment (e.g., 'Neutral', 'Dark', 'Light')

    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Strength: {self.strength} | Intelligence: {self.intelligence} | Charisma: {self.charisma} | Leadership: {self.leadership}")
        print(f"Health: {self.health} | Morale: {self.morale} | Morality: {'Good' if self.morality > 0 else 'Evil' if self.morality < 0 else 'Neutral'} | Faction: {self.faction}")
        print(f"Inventory: {', '.join([item.name for item in self.inventory]) if self.inventory else 'Empty'}")

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                item.use(self)
                self.inventory.remove(item)
                return True
        return False

    def update_morality(self, choice):
        if choice == "good":
            self.morality += 1
        elif choice == "evil":
            self.morality -= 1

    def update_faction(self, faction_choice):
        self.faction = faction_choice

class NPC(Character):
    def __init__(self, name, strength, intelligence, charisma, leadership, role, faction=None):
        super().__init__(name, strength, intelligence, charisma, leadership, faction)
        self.role = role  # Could be 'ally', 'enemy', etc.

    def talk(self, player):
        print(f"\n{self.name} says: 'I have a task for you, should you choose to help me.'")
        choice = input("Do you help? (yes/no): ").lower()
        if choice == "yes":
            print(f"\n{self.name}: 'You have earned my trust. I shall assist you.'")
            player.update_morality("good")
        else:
            print(f"\n{self.name}: 'You refuse me? Very well, but you make an enemy today.'")
            player.update_morality("evil")


class Enemy(Character):
    def __init__(self, name, strength, intelligence, charisma, leadership, myth_type, faction=None):
        super().__init__(name, strength, intelligence, charisma, leadership, faction)
        self.myth_type = myth_type  # Vampire, werewolf, etc.

    def attack(self, target):
        damage = random.randint(5, 15)
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")

    def special_attack(self, target):
        # Implementing magic or special ability attack
        damage = random.randint(15, 30) + self.intelligence
        target.health -= damage
        print(f"{self.name} uses a special attack on {target.name} for {damage} damage!")


class Item:
    def __init__(self, name, effect, value):
        self.name = name
        self.effect = effect
        self.value = value

    def use(self, target):
        print(f"{target.name} uses {self.name}, {self.effect}")
        if self.effect == 'heal':
            target.health += self.value
        elif self.effect == 'buff':
            target.strength += self.value
            target.intelligence += self.value


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def explore(self):
        print(f"\n{self.name}: {self.description}")


# Combat Mechanism
def battle(player, enemy):
    print(f"\nA battle has begun between {player.name} and {enemy.name}!\n")
    while player.health > 0 and enemy.health > 0:
        print("\nYour turn:")
        action = input("Choose action: 1) Attack 2) Use Item 3) Special Attack\n")
        
        if action == '1':
            player_attack(player, enemy)
        elif action == '2':
            if player.inventory:
                item_name = input(f"Enter item to use (Options: {', '.join([item.name for item in player.inventory])}): ")
                if not player.use_item(item_name):
                    print("Invalid item.")
            else:
                print("You don't have any items.")
        elif action == '3':
            special_attack(player, enemy)
        else:
            print("Invalid action.")
        
        if enemy.health > 0:
            enemy_attack(player, enemy)

    if player.health > 0:
        print(f"\n{player.name} has defeated {enemy.name}!")
    else:
        print(f"\n{player.name} has been defeated. Game over.")
        return False  # Player lost
    return True  # Player won


def player_attack(player, enemy):
    damage = random.randint(10, 20) + player.strength
    enemy.health -= damage
    print(f"\n{player.name} attacks {enemy.name} for {damage} damage!")


def special_attack(player, enemy):
    # Special attack based on player intelligence or item
    damage = random.randint(15, 30) + player.intelligence
    enemy.health -= damage
    print(f"\n{player.name} uses a special attack on {enemy.name} for {damage} damage!")


def enemy_attack(player, enemy):
    damage = random.randint(10, 20) + enemy.strength
    player.health -= damage
    print(f"{enemy.name} attacks {player.name} for {damage} damage!")


# Side Quests with Moral Dilemmas
def side_quest(player):
    print("\nYou encounter a wounded traveler in need of help.")
    choice = input("Do you help them? (yes/no): ").lower()
    if choice == "yes":
        print("\nYou give the traveler aid. They thank you and give you a reward.")
        reward = Item("Healing Herb", "heal", 15)
        player.add_to_inventory(reward)
        player.update_morality("good")
    else:
        print("\nYou ignore the traveler, leaving them to fend for themselves.")
        player.update_morality("evil")


# Faction System
class Faction:
    def __init__(self, name, alignment):
        self.name = name  # 'Light', 'Dark', 'Neutral'
        self.alignment = alignment  # 'good', 'evil', or 'neutral'

    def offer_ally(self, player):
        print(f"\n{self.name} faction approaches you with an offer of alliance.")
        choice = input(f"Do you join the {self.name} faction? (yes/no): ").lower()
        if choice == "yes":
            player.update_faction(self.name)
            print(f"\nYou have joined the {self.name} faction! You gain special abilities but make enemies.")
            if self.alignment == 'good':
                player.update_morality("good")
            else:
                player.update_morality("evil")
        else:
            print(f"\nYou reject the offer of {self.name}. The faction grows hostile toward you.")


# Story Progression
def check_story_progression(player):
    if player.morality > 2:
        print("\nThe Light Faction welcomes you as a hero, and your fame spreads across the lands!")
    elif player.morality < -2:
        print("\nThe Dark Faction sees you as an ally, offering you power and dark secrets.")
    else:
        print("\nYou remain neutral, walking the fine line between factions, not yet fully trusted.")

# Main Game
def main():
    print("Welcome to Shadows of the Balkans!\n")

    player_name = input("Enter your leader's name: ")
    player = Character(player_name, strength=10, intelligence=8, charisma=7, leadership=9)
    player.display_stats()

    # Locations
    village = Location("War-Torn Village", "A village ravaged by conflict. You can see the smoke rising in the distance.")
    forest = Location("Haunted Forest", "A dense, eerie forest, rumored to be home to ancient spirits.")
    ruins = Location("Ancient Ruins", "Ruins of a forgotten kingdom, filled with old magic and untold secrets.")
    
    locations = [village, forest, ruins]

    # Factions
    light_faction = Faction("Light", "good")
    dark_faction = Faction("Dark", "evil")
    neutral_faction = Faction("Neutral", "neutral")

    factions = [light_faction, dark_faction, neutral_faction]

    # Enemy Encounter
    vampire = Enemy("Vampire Lord", strength=15, intelligence=12, charisma=10, leadership=11, myth_type="Vampire")
    werewolf = Enemy("Werewolf Pack", strength=20, intelligence=8, charisma=6, leadership=5, myth_type="Werewolf")
    
    enemies = [vampire, werewolf]

    # Add items to player's inventory
    health_potion = Item('Health Potion', 'heal', 20)
    player.add_to_inventory(health_potion)

    # Start Game Loop
    while player.health > 0:
        print("\nWhere do you want to go?")
        for i, location in enumerate(locations, 1):
            print(f"{i}. {location.name}")
        choice = input("Choose location (1, 2, or 3): ")

        if choice == '1':
            village.explore()
            if random.random() < 0.5:  # Random chance for battle
                print("\nAn enemy appears!")
                if not battle(player, random.choice(enemies)):
                    break  # Player lost, stop game
            side_quest(player)  # Side quest event after exploring
        elif choice == '2':
            forest.explore()
            if random.random() < 0.5:  # Random chance for battle
                print("\nAn enemy appears!")
                if not battle(player, random.choice(enemies)):
                    break  # Player lost, stop game
            light_faction.offer_ally(player)  # Faction event after exploring
        elif choice == '3':
            ruins.explore()
            if random.random() < 0.5:  # Random chance for battle
                print("\nAn enemy appears!")
                if not battle(player, random.choice(enemies)):
                    break  # Player lost, stop game
            dark_faction.offer_ally(player)  # Faction event after exploring
        else:
            print("Invalid choice.")
        
        check_story_progression(player)  # Check how the story progresses based on the player's morality and faction alignment
        
        # Check player's health after the turn
        if player.health <= 0:
            print(f"\n{player.name} has been defeated. Game over.")
            break

    print("Game over.")


if __name__ == "__main__":
    main()
