
# * ##############
# * LIST METHODS #
# * ##############

def listMethods():
    
    # ? Append can add only one element to the end of the list 

    list1 = [12, 33, 7, 10, 28, 37]
    list1.append(14)
    print('list1 after 1 element is added is now', list1)

    # ? Extend can add multiple elements to the end of the list 

    list2 = [21, 30, 17]; list3 = [19, 3, 40]; list4 = [35, 12, 4]
    list5 = list2 + list3 + list4
    list1.extend(list5)
    print('list1 after multiple elements are added is now', list1)


    # ? Copy returns a copy fo the list

    list6 = list1.copy()
    print('list6 is now', list6)

    # ? Clear will remove all the elements from list1

    list1.clear();
    print("list1 is now", list1)

    # ? Count will returns the number of elements of a specified value

    count = list6.count(12)
    print('12 appears', count, 'times in list6')

    # ? Index will return the first index of the element specified

    index = list6.index(37)
    print('The number 37 is found at index', index)

    # ? Insert inserts a specified elememt at a specified index

    list6.insert(5, 81)
    print('list6 is now', list6)

    # ? Pop removes an element at a specified index

    list6.pop(6)
    print('list6 is now', list6)

    # ? Remove removes the first element with the specified value

    list6.remove(81)
    print('list6 i now', list6)

    # ? Reverse reverse the order of a list

    list6.reverse()
    print('list6 is now', list6)

    # ? Sort is sorting the list

    list6.sort()
    print('list6 is now', list6)
    
# listMethods();

# * #######################################################################################
# * EXAMPLE OF USER INPUT OF NUMBERS TO CREATE LIST AND SHOW SMALLEST AND HIGHEST NUMBERS #
# * #######################################################################################

def user_amount_input():
    amount_numbers = int(input("Please enter the amount of numbers between 3 and 12: "))
    if amount_numbers < 3 or amount_numbers > 12:
        print('You are not within the specified range')
        user_amount_input()
    else:
        new_list = []
        for i in range(0, amount_numbers):
            numb = int(input("Please enter a number: "))
            new_list.append(numb)
        print("Your biggest number entered is: ", max(new_list))
        print("Your smallest number entered is: ", min(new_list))
        again = input("Enter 'y' if you want to go again or 'n' to exit")
        if again == 'y':
            user_amount_input()
        else:
            print("Thank You for playing the game")


# user_amount_input()

# * ############################################################
# * EXAMPLE OF MAPPING THROUGH A LIST WHILE CALLING A FUNCTION #
# * ############################################################

def categorise_them(num):
    if num > 89:
        return 'A+' 
    elif num > 79:
        return "A"
    elif num > 69:
        return "B"
    elif num > 59:
        return "C"
    elif num > 49:
        return "D"
    elif num > 39:
        return "E"
    else:
        return "Very Bad"

def mapList():
    listA = ['Luke', "Sona", "Bhash", "Johan", "Desiree", "Vamshi", "Sue", "Kim", "Tom", "Vinod", "Amrita"]
    listB = [81, 94, 33, 78, 66, 81, 54, 67, 46, 91, 83]
    final_list = list(map(categorise_them, listB))
    # mapping_iterator = map(categorise_them, listB)
    # final_list = list(mapping_iterator)
    for i in range(0, len(listA)):
        print(listA[i], 'scored', listB[i],'marks and achieved symbol:', final_list[i])

# mapList();

# * ######################
# * EXAMPLE OF FILTERING #
# * ######################


def return_only(numb):
    return numb > 70 


def filterList():
    numbers = [71, 28, 57, 88, 19, 68, 22, 90]
    filtered_list = list(filter(return_only, numbers))
    print('Filtered list is:', filtered_list)

# filterList();

# * #######################################
# * EXAMPLE OF REDUCE - ADDING UP NUMBERS #
# * #######################################

def reduceList():
    import functools
    numbers_list = [14, 29, 81, 33, 7, 15]
    total_sum = functools.reduce(lambda x, y: x + y, numbers_list)
    print('The total sum of the numbers is:', total_sum)

reduceList()
