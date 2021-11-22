charInventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def displayInventory(inventory):
    print('Inventory:')
    item_Total = 0
    for k,v in inventory.items():
        print('key: ' + k + ' value: ' + str(v))
        item_Total += v
    print('Total number of items: ' + str(item_Total))

displayInventory(charInventory)
