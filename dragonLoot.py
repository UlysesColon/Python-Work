inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin','dagger', 'gold coin', 'gold coin', 'ruby']



def addToInventory(inventory, addedItems):
    #code goes here
    for k in addedItems:
        if k in inventory.keys():
            inventory[k] += 1
        else:
            inventory.setdefault(k,1)
            
    return inventory


def displayInventory(inventory):
    print('Inventory:')
    item_Total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + k )
        item_Total += v
    print()
    print('Total number of items: ' + str(item_Total))


inv = addToInventory(inv, dragonLoot)

displayInventory(inv)