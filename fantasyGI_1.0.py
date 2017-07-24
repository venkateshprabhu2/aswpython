def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
    		inventory.setdefault(item,0)
    		inventory[item]+=1
    return inventory

def displayInventory(inv):
	total_items=0
	for k,v in inv.items():
		print str(v) + " " + k
		total_items+=v
	print "\n" + "Total number of items:" + str(total_items)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby', 'sword', 'armor']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)