import json

class Save:
    def __init__(self, spell_list_instance, character_instance, inventory_instance):
        self.spell_list_instance = spell_list_instance
        self.character_instance = character_instance
        self.inventory_instance = inventory_instance
        self.loaded_char = ""

    def save_char(self):
        name = input("What is your character's name? ")
        char_data = {
            "char_name": name,
            "char_spells": self.spell_list_instance.get_char_spells(),
            "char_hp": self.character_instance.get_hp(),
            "char_stats": self.character_instance.get_stats(),
            "char_level": self.character_instance.get_char_level(),
            "char_inventory": self.inventory_instance.get_inventory(),
        }
        with open(f"{name}.json", "w") as save_file:
            json.dump(char_data, save_file)
        print(f'Data saved under {name}')

    def load_char(self, char_name):
        try:
            with open(f"{char_name}.json", "r") as file:
                character_data = json.load(file)
                loaded_char_spells = character_data.get("char_spells", [])
                loaded_char_stats = character_data.get("char_stats", [])
                loaded_char_level = character_data.get("char_level", )
                loaded_char_name = character_data.get("char_name", "")
                loaded_char_hp = character_data.get("char_hp", "")
                loaded_char_inventory = character_data.get("char_inventory", [])
                self.spell_list_instance.set_char_spells(loaded_char_spells)
                self.character_instance.set_char_stats(loaded_char_stats)
                self.character_instance.set_char_level(loaded_char_level)
                self.character_instance.set_char_name(loaded_char_name)
                self.character_instance.set_char_hp(loaded_char_hp)
                self.inventory_instance.set_inventory(loaded_char_inventory)
            self.loaded_char = character_data.get("char_name", "")
            print(f"Character: {self.loaded_char} loaded")
        except FileNotFoundError:
            print(f"Character file for {char_name} not found.")

