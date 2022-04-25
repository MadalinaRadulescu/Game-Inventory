
# This is the file where you must work.
# Write code in the functions (and create new functions) so that they work
# according to the requirements.
arr = {"torch": 4, "sowrd":3}
arrList = ["knif", "rope"]
def display_inventory(inventory):
    for k, v in inventory.items():
        print(k + ": " + str(v))
    
def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1
    return inventory

# print(add_to_inventory(arr, arrList))

def remove_from_inventory(inventory, removed_items):
    for item in removed_items:
        if item in inventory:
            inventory[item] -= 1
            if inventory[item] < 1:
                del inventory[item]
        else:
            return inventory
    return inventory

#print(remove_from_inventory(arr, arrList))


def print_table(inventory, order=None):
    print(" -----------------")
    print (" item name | count")
    print(" -----------------")
    if order is None:
        for k, v in inventory.items():
            count = v
            print (" {:>10}| {:>5}".format(k, count))
    elif order == "desc":
        sort_inventory = sorted(inventory.items(), key = lambda x:x[1], reverse=True)
        for i in sort_inventory:
            print (" {:>10}| {:>5}".format(i[0], i[1]))
    elif order == "asc":
        sort_inventory = sorted(inventory.items(), key = lambda x:x[1])
        for i in sort_inventory:
            print (" {:>10}| {:>5}".format(i[0], i[1]))
    print(" -----------------")


def import_inventory(inventory, filename):
    import csv
    file = open(filename)
    csvreader = csv.reader(file) 

    list_itemes = []
    for l in csvreader:
        for item in l:
            list_itemes.append(row)
    add_to_inventory(inventory, list_itemes)


def export_inventory(inventory, filename):
    with open(filename, 'w') as f:
        for key, val in inventory.items():
            item = ", ".join([key]*val)
            f.write(item + ", ")
