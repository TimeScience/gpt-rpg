import time

SUPERPOWERS = {
    "fire": 30,
    "ice": 25,
    "lightning": 35
}

class Player:
    def __init__(self, name, power):
        self.name = name
        self.power = SUPERPOWERS[power]
        self.health = 100
        self.items = []
        self.gold = 50

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Power: {self.power})"

    def attack(self, enemy):
        if self.power >= enemy.power:
            damage = 20
        else:
            damage = 10
        enemy.health -= damage
        return damage


class Enemy:
    def __init__(self, name, power, health):
        self.name = name
        self.power = power
        self.health = health

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Power: {self.power})"

    def attack(self, player):
        damage = 15
        player.health -= damage
        return damage

def display(text):
    print(text)

def get_choice(num_choices):
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if 1 <= choice <= num_choices:
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def character_creation():
    display("Welcome to the RPG game!")
    display("Create your character:")
    name = input("Enter your character's name: ")
    while True:
        power = input("Choose a superpower (fire, ice, lightning): ").lower()
        if power in ['fire', 'ice', 'lightning']:
            break
        else:
            print("Invalid power. Please choose either fire, ice, or lightning.")
    return Player(name, power)

class Item:
    def __init__(self, name, description, cost=0):
        self.name = name
        self.description = description
        self.cost = cost

    def __str__(self):
        return f"{self.name}: {self.description} (Cost: {self.cost} gold)"

def intro(player):
    display(f"{player.name}, you wake up in a mysterious forest with no memory of how you got here.")
    display("You notice a glowing orb in front of you. As you touch it, you feel immense power surging through you.")
    display(f"Congratulations! {player.name}, you now possess the power of {player.power}!")

def use_item(player):
    if len(player.items) == 0:
        display("You don't have any items.")
    else:
        display("Select an item to use:")
        for idx, item in enumerate(player.items, 1):
            print(f"{idx}. {item}")
        choice = get_choice(len(player.items))
        item_to_use = player.items.pop(choice - 1)
        if item_to_use.name == "Healing Potion":
            player.health += 50
            if player.health > player.max_health:
                player.health = player.max_health
            display("You used the Healing Potion. Your health is restored.")
        elif item_to_use.name == "Enchanted Amulet":
            player.health += 20
            if player.health > player.max_health:
                player.health = player.max_health
            display("You used the Enchanted Amulet. Your health is boosted.")
        elif item_to_use.name == "Water Nymph Tears":
            player.health = player.max_health
            display("You used the Water Nymph Tears. Your health is fully restored.")
        else:
            display("You can implement the effect of other items here.")
def fight_enemy(player, enemy):
    while player.health > 0 and enemy.health > 0:
        display(f"{player.name}, your health: {player.health}")
        display(f"{enemy.name}'s health: {enemy.health}")
        display("What will you do?")
        display("1. Attack the enemy")
        display("2. Use an item (if you have any)")
        choice = get_choice(2)

        if choice == 1:
            damage_to_enemy = player.attack(enemy)
            display(f"You attacked {enemy.name} and dealt {damage_to_enemy} damage!")
            if enemy.health <= 0:
                display(f"Congratulations! You defeated {enemy.name}!")
                break

            damage_to_player = enemy.attack(player)
            display(f"{enemy.name} attacked you and dealt {damage_to_player} damage!")
            if player.health <= 0:
                display("Oh no! You were defeated. Game Over.")
                break

        elif choice == 2:
            use_item(player)

def explore(player):
    display(f"{player.name}, you continue your journey through the mysterious forest.")
    display("You discover a hidden cave entrance.")
    display("Do you want to enter the cave?")
    display("1. Yes")
    display("2. No")
    choice = get_choice(2)

    if choice == 1:
        display("Inside the cave, you find a chest filled with treasures!")
        player.items.append(Item("Golden Key", "Opens a secret door"))
        player.items.append(Item("Healing Potion", "Restores 50 health"))
    else:
        display("You decide not to enter the cave and continue exploring the forest.")
def visit_shop(player):
    display(f"{player.name}, you come across a mysterious shop hidden in the forest.")
    display("The shopkeeper welcomes you and offers to sell various items.")
    display("Here are the items available for purchase:")
    
    shop_items = [
        Item("Fire Sword", "Deals extra damage with fire element", 30),
        Item("Ice Staff", "Freezes enemies temporarily", 25),
        Item("Lightning Ring", "Shocks enemies in battle", 20)
    ]
    
    for idx, item in enumerate(shop_items, 1):
        display(f"{idx}. {item.name} - {item.description} (Cost: {item.cost} gold)")

    display(f"You currently have {player.gold} gold.")
    display("Select an item to purchase or enter '0' to exit the shop.")
    
    choice = get_choice(len(shop_items) + 1)
    
    if choice == 0:
        display("You thank the shopkeeper and leave the shop.")
    else:
        item_to_buy = shop_items[choice - 1]
        if item_to_buy.name in [item.name for item in player.items]:
            display(f"You already have the {item_to_buy.name}, no need to buy another one!")
        elif player.gold >= item_to_buy.cost:
            player.gold -= item_to_buy.cost
            player.items.append(item_to_buy)
            display(f"Congratulations! You purchased the {item_to_buy.name}.")
        else:
            display(f"You don't have enough gold to buy the {item_to_buy.name}.")
def explore_enchanted_lake(player):
    display("At the Enchanted Lake, you encounter a group of water nymphs.")
    display("They offer you a choice:")
    display("1. Receive a magical blessing that enhances your power.")
    display("2. Gain valuable items that aid you in battle.")
    choice = get_choice(2)
    if choice == 1:
        player.power += 5
        display("The water nymphs bestow their magical blessing upon you.")
        display(f"Your power increases to {player.power}.")
    elif choice == 2:
        player.items.append(Item("Enchanted Amulet", "Boosts your health during battles"))
        player.items.append(Item("Water Nymph Tears", "Revives you once if your health reaches 0"))
        display("The water nymphs gift you with valuable items.")

def explore_cursed_swamp(player):
    display("As you venture through the Cursed Swamp, you encounter a group of cursed creatures.")
    display("They challenge you to a game of riddles. If you succeed, they will share a secret with you.")
    display("Are you ready for the riddle challenge?")
    display("1. Yes")
    display("2. No")
    choice = get_choice(2)
    if choice == 1:
        display("The cursed creatures present you with a riddle:")
        display("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?")
        riddle_answer = "echo"
        answer = input("Enter your answer: ").lower()
        if answer == riddle_answer:
            player.items.append(Item("Cursed Scroll", "Unlocks a hidden passage in the forest"))
            display("Congratulations! You solved the riddle.")
            display("The cursed creatures reward you with a Cursed Scroll.")
        else:
            display("Incorrect answer. The cursed creatures decide not to share their secret.")
    else:
        display("You decide not to participate in the riddle challenge and continue your journey.")
def explore_mystic_mountains(player):
    display("As you climb the Mystic Mountains, you discover an ancient shrine.")
    display("The shrine presents you with a mystical test of courage.")
    display("Do you accept the challenge?")
    display("1. Yes")
    display("2. No")
    choice = get_choice(2)
    if choice == 1:
        if player.power >= 30:
            display("Your power is sufficient to face the mystical test.")
            display("You enter the shrine and confront the guardian spirit.")
            display("Prepare yourself for a challenging battle!")
            guardian_spirit = Enemy("Guardian Spirit", 30, 150)
            fight_enemy(player, guardian_spirit)
            if player.health > 0:
                player.items.append(Item("Mystic Crystal", "Grants temporary invincibility in battles"))
                display("Congratulations! You successfully conquered the mystical test.")
                display("The guardian spirit rewards you with a Mystic Crystal.")
            else:
                display("You were unable to defeat the guardian spirit. Better luck next time!")
        else:
            display("You do not feel prepared for the mystical test and decide not to enter the shrine.")
    else:
        display("You decide not to accept the challenge and continue your journey.")

def final_boss_encounter(player):
    display("As you continue your journey, you reach the heart of the mysterious forest.")
    display("A powerful enemy, the Dark Sorcerer, stands before you.")
    display("Prepare for the final battle!")

    dark_sorcerer = Enemy("Dark Sorcerer", 50, 200)

    fight_enemy(player, dark_sorcerer)

    if player.health <= 0:
        display("You were defeated by the Dark Sorcerer. The forest falls into darkness.")
        display("Game Over.")
    else:
        display("Congratulations! You defeated the Dark Sorcerer and restored balance to the forest.")
        display("You are hailed as the hero of the land!")
def main():
    player = character_creation()
    intro(player)

    enemy1 = Enemy("Evil Goblin", 10, 50)
    display(f"A wild {enemy1.name} appears!")
    fight_enemy(player, enemy1)

    explore(player)
    visit_shop(player)
    explore_enchanted_lake(player)
    explore_cursed_swamp(player)
    explore_mystic_mountains(player)
    final_boss_encounter(player)

if __name__ == "__main__":
    main()
