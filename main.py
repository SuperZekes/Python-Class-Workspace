import questionary

print("Welcome to the grocery list program")

count = questionary.text("How many items do you want to add?").ask()
count = int(count) if count.isdigit() else 0

grocery_list = []

for i in range(count):
    item = questionary.text("Enter item:").ask()
    grocery_list.append(item)

print("You've added the following items to your list:")
for item in grocery_list:
    print(f"item: {item}")

take_out = questionary.confirm("Do you want to take out an item?").ask()

while take_out and grocery_list:
    item_to_remove = questionary.select("Which item do you want to remove?", choices=grocery_list).ask()
    grocery_list.remove(item_to_remove)
    print(f"Item '{item_to_remove}' has been removed from the list.")
    
    if not grocery_list:
        print("Your grocery list is now empty.")
        break
    
    take_out = questionary.confirm("Do you want to take out another item?").ask()