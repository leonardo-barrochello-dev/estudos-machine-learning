import random

class Player:
    name: str
    level : int
    hp : int

    def __init__(self, name: str, level: int , hp: int):
        self.name = name
        self.level = level
        self.hp = hp

    def attack(self, enemy : 'Player'):
        damage = random.randint(50, 99)
        enemy.hp -= damage
        if enemy.hp <= 0:
            enemy.hp = 0
            print(f"💀 O herói {self.name} derrotou o herói {enemy.name}")
        else:
            print(f"⚔️ {self.name} atacou {enemy.name} (Dano: {damage} | HP Restante: {enemy.hp})")
        
    def __str__(self):
        return f"Heroi {self.name} (Lv {self.level}) - HP: {self.hp}"

players = [Player("Aragorn", 1, 100), Player("Legolas", 1, 100), Player("Gimli", 1, 100)]

players_new = [ p for p in players if p.name.lower().find("a") != -1 ]

for i in range(len(players_new) - 1 ):
    players_new[i].attack(players_new[i+1])

final_data = { "mortos" : [ p.name for p in players_new if p.hp <= 0 ], "vivos" : [ p.name for p in players_new if p.hp > 0]}

print(final_data)