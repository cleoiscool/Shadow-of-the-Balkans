import random

# Game Variables and Character Class
class Character:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.strength = 10
        self.inventory = []
        self.morality = 0  # Neutral morality for now
        
    def display_stats(self):
        print(f"\n{self.name}'s Stats:")
        print(f"Health: {self.health} | Strength: {self.strength} | Morality: {'Good' if self.morality > 0 else 'Evil' if self.morality < 0 else 'Neutral'}")
        print(f"Inventory: {', '.join(self.inventory) if self.inventory else 'Empty'}")

    def add_item(self, item):
        self.inventory.append(item)

    def use_item(self, item):
        if item in self.inventory:
            print(f"{self.name} uses {item}.")
            self.inventory.remove(item)
            if item == "Health Potion":
                self.health += 20
                print(f"{self.name}'s health increased by 20.")
        else:
            print(f"{item} is not in your inventory.")

# Alien Enemy Class
class Alien:
    def __init__(self, name):
        self.name = name
        self.health = 50
        self.strength = 5
        
    def attack(self, target):
        damage = random.randint(5, 10) + self.strength
        target.health -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        
    def is_alive(self):
        return self.health > 0

# Exploration Scene
def explore_lab(player):
    print("\nYou are in a high-tech laboratory. The air is sterile, and strange machines hum around you.")
    choice = input("Do you wish to explore the lab? (yes/no): ").lower()
    
    if choice == "yes":
        print("\nYou search the lab and find a Health Potion!")
        player.add_item("Health Potion")
        print("You put the potion in your inventory.")
    else:
        print("\nYou choose not to explore further.")

# Combat Function
def combat(player, alien):
    print("\nA low-level alien soldier approaches!")
    
    while player.health > 0 and alien.is_alive():
        print("\nChoose your action:")
        print("1) Attack")
        print("2) Use Item")
        print("3) Run")
        action = input("Enter choice (1/2/3): ")
        
        if action == "1":
            damage = random.randint(10, 20) + player.strength
            alien.health -= damage
            print(f"{player.name} attacks {alien.name} for {damage} damage!")
        elif action == "2":
            if player.inventory:
                item = input(f"Choose an item to use: {', '.join(player.inventory)}: ").capitalize()
                player.use_item(item)
            else:
                print("You have no items in your inventory.")
        elif action == "3":
            print(f"{player.name} decides to flee from the battle!")
            break
        else:
            print("Invalid action.")

        if alien.is_alive():
            alien.attack(player)
        
        if player.health <= 0:
            print(f"{player.name} has been defeated. Game Over!")
            return False

    if alien.is_alive() == False:
        print(f"{alien.name} has been defeated!")
    return True

# Escape from Lab Scene
def escape_lab(player):
    print("\nThe alarm blares. The laboratory is under attack!")
    choice = input("Do you attempt to escape the lab? (yes/no): ").lower()
    
    if choice == "yes":
        print("\nYou find an exit and escape the lab. You can see the alien ships descending upon the city!")
        print(f"Your health is: {player.health}. You need to fight back!")
        return True
    else:
        print("\nYou stay in the lab, unsure of what to do next...")
        return False

# Ending Scene
def ending_scene():
    print("\nAs you stand outside, you look up to see the alien ships in the sky.")
    print("A massive invasion is underway. The world is in chaos.")
    print("The fight for humanity's survival begins... To be continued...")

# Main Game Loop
def main():
    print("Welcome to Shadows of the Balkans: Day Break!")
    
    player_name = input("Enter your leader's name: ")
    player = Character(player_name)
    player.display_stats()
    
    print("\nYou awaken in a high-tech lab. The air smells sterile, and your body feels weak.")
    print("You vaguely remember the events that led you here. The year... 2785? Something has gone terribly wrong.")
    
    explore_lab(player)
    combat_result = combat(player, Alien("Alien Soldier"))
    
    if combat_result:
        if escape_lab(player):
            ending_scene()

if __name__ == "__main__":
    main()
