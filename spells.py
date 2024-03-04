import random
from level_spell_slots import spell_slots_list
class SpellList:
    def __init__(self, character_instances):
        self.char_spells = []  # Initialize the instance variable
        self.spell_slots = spell_slots_list[character_instances.char_level]
        self.character_instances = character_instances

    def get_char_spells(self):
        return self.char_spells

    def set_char_spells(self, new_char_spells):
        self.char_spells = new_char_spells

    def add_spell(self):
        new_spell = {
            'spell': input("What is the spell's name?\n"),
            'description': input("What is the description?\n")
        }
        self.char_spells.append(new_spell)
        print(f"{new_spell['spell']} has been added to spell list")

    def remove_spell(self):
        remove_spell_name = input('What spell would you like to remove?: \n')
        for spell in self.char_spells:
            if spell.get('spell') == remove_spell_name:
                self.char_spells.remove(spell)
                print(f"{remove_spell_name} has been removed from your list")
                break
        else:
            print(f"{remove_spell_name} is not in your spell list")

    def display_spell(self):
        for spell_dict in self.char_spells:
            for k, v in spell_dict.items():
                print(f"{v}", end='|')
            print()

    def cast_spell(self) :
        print(self.spell_slots)
        level = int(input('At which level?: \n'))

        if level in self.spell_slots:
            self.spell_slots[level] -= 1
            remaining_slots = self.spell_slots[level]
            print(f"{remaining_slots} slots left of {level}-level spells left")

            for stats_dict in self.character_instances.stats:
                for k, v in stats_dict.items():
                    if k == 'Spell attack modifier':
                        sam = v
            roll = random.randint(1, 20)
            total = roll + sam
            print(f"Roll:{roll}, Total:{total}")

        else:
            print(f"No slots available for level {level}")
        print(self.spell_slots)