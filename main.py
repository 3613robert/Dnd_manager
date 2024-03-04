from spells import SpellList
from save import Save
from character import Character
from dice_roller import DiceRoller
from inventory import Inventory

character = Character()
spell_list = SpellList(character_instances=character)
inventory = Inventory()
save = Save(spell_list_instance=spell_list, character_instance=character, inventory_instance=inventory)

def display_main():
    print(f"Character: {character.name}, hp{character.hp}, Spells:{len(spell_list.get_char_spells())}")

new_load = input('Do you want to (l)oad a character or start a (n)ew one?: \n')
if new_load == 'n':
    character.new_character()
elif new_load == 'l':
    save.load_char(char_name=input("What character to load? "))

main = True
while main:
    display_main()
    option = input("What would you like to do? "
                   "Type (s) for spell list, "
                   "(c) for character info,"
                   "(d) for diceroller,"
                   "(n) for new character,"
                   "(i) for inventory, "
                   "(sa) for save,"
                   "(l) for load: ")
    if option == 's':
        char_spells = spell_list.get_char_spells()
        spell_list.display_spell()
        option_spells = input("Would you like to add, remove or cast a spell? Type 'a', 'r' or 'c': \n")
        if option_spells == 'a':
            spell_list.add_spell()
            spell_list.char_spells = spell_list.get_char_spells()
            print("Updated Spell List:", char_spells)
        elif option_spells == 'r':
            spell_list.remove_spell()
            print("")
        elif option_spells == 'c':
            spell_list.cast_spell()
    elif option == 'c':
        character.display_stats()
        option_character = input("Would you like to (a)dd, (c)hange stats or change (l)evel?")
        if option_character == 'a':
            character.add_stats()
        elif option_character == 'c':
            character.change_stats()
        elif option_character == 'l':
            character.change_caster_level()
            character.set_char_level(new_char_level=character.char_level)
            spell_list = SpellList(character_instances=character)
    elif option == 'd':
        dice_roller = DiceRoller()
        dice_roller.roll_dice()
    elif option == 'n':
        character.new_character()
    elif option == 'i':
        add = True
        while add:
            inventory.display_inventory()
            inventory_choice = input("Type (a) to add items, (r) to remove items and (b) to go back")
            if inventory_choice == 'b':
                add = False
            elif inventory_choice == 'a':
                inventory.add_item()
            elif inventory_choice == 'r':
                inventory.remove_item()
    elif option == "sa":
        save.save_char()
    elif option == 'l':
        save.load_char(char_name=input("What character to load? "))
