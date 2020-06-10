import random


def modifier(value):
    return (value - 10) // 2



class Character:
    def __init__(self):
        self.charisma = self.ability()
        self.constitution = self.ability()
        self.dexterity = self.ability()
        self.hitpoints = self.get_hitpoints()
        self.intelligence = self.ability()
        self.strength = self.ability()
        self.wisdom = self.ability()

    def ability(self):
        dices = sorted(self.throw_dices())
        scores = sum(dices[1::])
        return scores

    def get_hitpoints(self):
        score = 10 + modifier(self.constitution)
        return score

    @staticmethod
    def throw_dices():
        dices = []
        for n in range(4):
            dices.append(random.randrange(1, 6))

        return dices
