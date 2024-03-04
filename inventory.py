class Inventory:
    def __init__(self):
        self.inventory = []

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, new_inventory):
        self.inventory = new_inventory

    def add_item(self):
        new_item = {'name': input("What item would you like to add?: \n").lower(),
                    'amount': int(input("How many?: \n"))
                    }
        self.inventory.append(new_item)

    def display_inventory(self):
        for item_dict in self.inventory:
            for k, v in item_dict.items():
                print(f"{k}:{v}", end='|')
            print()

    def remove_item(self) :
        remove_item = input("Which item would you like to remove?: \n")
        remove_amount = int(input("How many would you like to remove?: \n"))

        for index, item in enumerate(self.inventory):
            if remove_item == item['name']:
                self.inventory[index]['amount'] -= remove_amount
                print(f"{remove_amount} removed from {item['name']} in inventory")

                if self.inventory[index]['amount'] <= 0:
                    del self.inventory[index]
                    print(f"No {item['name']}'s left, {item['name']} is removed from Inventory")
                    break
                else:
                    break
        else:
            print('Item not in inventory')


