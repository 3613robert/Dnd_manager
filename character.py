
class Character:
    def __init__(self):
        self.hp = "12"
        self.stats = []
        self.name = "Luc"
        self.char_level = 0

    def get_hp(self):
        return self.hp

    def set_char_hp(self, new_char_hp):
        self.hp = new_char_hp

    def get_name(self):
        return self.name

    def set_char_name(self, new_char_name):
        self.name = new_char_name

    def get_stats(self):
        return self.stats

    def get_char_level(self):
        return self.char_level

    def set_char_level(self, new_char_level):
        self.char_level = new_char_level

    def set_char_stats(self, new_char_stats):
        self.stats = new_char_stats

    def new_character(self):
        self.name = input("what is your name?: \n")
        new_stats = {
            'Strength': input('what is your Strength stat?: \n'),
            "Dexterity": input("what is your Dexterity stat?: \n"),
            "Constitution": input("what is your Constitution stat?: \n"),
            "Wisdom": input("what is your Wisdom stat?: \n"),
            "Intelligence": input("what is your Intelligence stat?: \n"),
            "Charisma": input("what is your Charisma stat?: \n"),
            "Spell attack modifier": int(input("What is your spell attack modifier?: \n"))
        }
        self.stats.append(new_stats)
        self.hp = input("What is your hp? \n")
        self.char_level = int(input("What caster level are you?: \n"))

    def display_stats(self):
        for stat_dict in self.stats:
            for k, v in stat_dict.items():
                print(f"{k}:{v}", end='|')
            print()

    def add_stats(self):
        stat = input('Which stat would you like to add?: \n')
        modifier = input('What modifier does the stat have?: \n')
        added_stat = {stat: modifier}
        self.stats.append(added_stat)
        print(f"{stat} has been added to the list of stats")

    def change_stats(self):
        changed_stat = input('Which stat would you like to change?: \n')
        changed_modifier = input("new modifier: \n")
        change_all = {changed_stat: changed_modifier}
        for index, stat in enumerate(self.stats):
            if changed_stat in stat:
                self.stats[index] = change_all
                print(f"{changed_stat} has been changed to {changed_modifier}")
                break
        else:
            print(f"{changed_stat} is not found in your stats")

    def change_caster_level(self):
        new_level = input("What is your new caster level?: \n")
        self.char_level = int(new_level)

