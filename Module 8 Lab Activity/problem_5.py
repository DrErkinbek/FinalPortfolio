"""
Erkinbek
11/29/2022
Task1. Climb a mountain - needs rope,
coat and first aid kit cannot have slow
Task2. Cook a meal - needs pan, groceries,
cannot have a small
Task3. Write a book - needs pen, paper,
idea, cannot have confusion
"""

class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname
    def get_year(self):
        return self.weapons

    def get_color(self):
        return self.weaknesses

    def profile(self):
        return self.nickname, self.weapons, self.weaknesses

player1 = character("", "", "")
player1.nickname = "Dragon Slayer"
player1.weapons = ["pan", "paper", "idea", "rope", "groceries"]
player1.weaknesses = ["slow"]

for item in player1.weapons:
    print("Item:", item)
for debuff in player1.weaknesses:
    print("Debuff", debuff)

def climb_mountain():
    item = "rope"
    if item in player1.weapons:
        print("Character has picked up!")