
# * ###############
# * SET METHODS   #
# * ###############

def setMethods():
    
    # ? Add will add only 1 element to the set
    
    set1 = {"Man", "Woman", "Child", "Car", "House", "Furniture", "Man"}
    set1.add("Computer")
    print('set1 is now', set1)
    
    # ? Clear will remove all the elements from the set
    
    set1.clear()
    print('set1 is now empty', set1)
    
    # ? Copy returns a copy of the set
    
    set2 = {18, 39, 17, 10}
    set3 = set2.copy()
    print('set3 is now', set3)
    
    # ? Difference will return a set with the differences between 2 or more sets
    
    set4 = {"Paper", "Steel", "Wool", "Fabrics"}
    set5 = {"Gold", "Paper", "Water", "Wool"}
    
    set6 = set4.difference(set5)
    print('The following values appear in set4 but not in set5', set6)
    set7 = set5.difference(set4)
    print('The following values appear in set5 but not in set4', set7)
    
    # ? Difference_update removes the elements that appear in both sets
    
    set8 = {"Apple", "Banana", "Pear", "Apricot"}
    set9 = {"Tomato", "Apple", "Pear", "Pineapple"}
    set8.difference_update(set9)
    print('set8 is now', set8)
    
    # ? Discard removes the specified element from the set - The same effect with remove()
    
    set10 = {19, 17, 8, 10, 31, 33, 24, 20, 13, 19}
    set10.discard(19);
    print('set10 is now', set10)
    
    # ? Intersection will return the elements that exist in both sets
    
    set11 = {"Blue", "Yellow", "Green", "Red"}
    set12 = {"Orange", "Purple", "Blue", "Green", "Pink"}
    
    set13 = set11.intersection(set12)
    print('set13 is now', set13)
    
    # ? Intersection_update removes the elements that do not appear in both sets
    
    set14 = {"Hallo", "Hi", "Hey", "Hello", "Goodbye"}
    set15 = {"Hi", "Bye", "Hello", "Cheers"}
    set14.intersection_update(set15);
    print('set14 is now', set14)

    # ? Isdisjoint will return true if no items in 1 set is present in another set, else false
    
    set16 = {12, 28, 15, 33, 22, 7}
    set17 = {17, 10, 27, 20, 13, 8}
    boola = set16.isdisjoint(set17)
    print('No items in set16 is equal to an item in set17 -', boola)
    
    # ? Issubset Return True if all items in set x are present in set y
    
    set18 = {19, 14, 10, 12, 22, 30}
    set19 = {10, 19, 12, 22, 30, 14, 10, 14}
    boolb = set18.issubset(set19)
    print('All items in set18 is present in set19 -', boolb)
    
    # ? Issuperset Return True if all items in set y are present in set x
    
    set20 = {"B", "A", "Z", "P", "K", "L", "E", "X", "W", "R"}
    set21 = {"K", "A", "L", "Z", "E", "P"}
    boolc = set20.issuperset(set21)
    print('All the items in set21 are present in set20 -', boolc)
    
    # ? Pop removes a random item from the set
    
    set22 = {44, 18, 20, 71, 99, 57, 81, 40, 33}
    set22.pop()
    print('set22 is now', set22)
    
    # ? Return a set that contains all items from both sets, except items that are present 
    # ? in both sets:
    
    set23 = {'Donkey', "Horse", "Duck", "Dog", "Sheep"}
    set24 = {"Cat", "Chicken", "Donkey", "Duck", "Dog"}
    set25 = set23.symmetric_difference(set24);
    print('set25 is now', set25)
    
    # ? Symmetric_difference_update Remove the items that are present in both sets,  
    # ? AND insert the items that is not present in both sets:
    
    set26 = {'Donkey', "Horse", "Duck", "Dog", "Sheep"}
    set27 = {"Cat", "Chicken", "Donkey", "Duck", "Dog"}
    set26.symmetric_difference_update(set27)
    print('set26 is now', set26)
    
    # ? Union Return a set that contains all items from both sets - duplicates are excluded
    
    set29 = {26, 28, 44, 57, 80, 21, 27, 44}
    set30 = {57, 33, 41, 7, 10, 26, 44, 43}
    set31= set29.union(set30)
    print('set31 is now', set31)
    
setMethods();
