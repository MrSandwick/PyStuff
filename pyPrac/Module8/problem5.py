# Problem5_GameCharacter.py
# Baatyrbek Turatov
# June 18, 2024
# Checks if character can complete tasks based on items and debuffs

class Character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses
    
    def check_task(self, task_items, forbidden_debuffs):
        # Check for required items
        for item in task_items:
            if item not in self.weapons:
                print(f"Cannot perform task - missing {item}")
                return False
        
        # Check for forbidden debuffs
        for debuff in forbidden_debuffs:
            if debuff in self.weaknesses:
                print(f"Cannot perform task - has {debuff} debuff")
                return False
        
        print("Can perform task")
        return True

# Create character
player1 = Character('Dragon Slayer', ['pan', 'paper', 'idea', 'rope', 'groceries'], ['slow'])

# Task checks
print("\nTask 1: Climb a mountain")
player1.check_task(['rope', 'coat', 'first aid kit'], ['slow'])

print("\nTask 2: Cook a meal")
player1.check_task(['pan', 'groceries'], ['small'])

print("\nTask 3: Write a book")
player1.check_task(['pen', 'paper', 'idea'], ['confusion'])