
# * ###############
# * TUPLE METHODS #
# * ###############

def tupleMethods():
    
    # ? Count will count how many times a specified value occurs in the tuple
    
    tuple1 = ("Dog", "Donkey", "Horse", "Cat", "Horse", "Duck", "sheep");
    amount= tuple1.count("Horse")
    print('Horse appears', amount, 'times in tuple1')
    
    # ? Index will return first index where the specified element is located in the tuple
    
    idx = tuple1.index("Horse")
    print("The first Horse appears at index", idx, 'in tuple1')
    
    # ? To reverse a tuple, first create another tuple
    
    tuple2 = (12, 30, 45, 61);
    tuple3 = tuple(reversed(tuple2))
    tuple2 = tuple3
    print('tuple2 is now a reversed', tuple2)
    
    # ? To clear a tuple, first create another empty tuple
    
    tuple4 = (19, 38, 7, 13, 2, 29)
    tuple5 = ()
    tuple4 = tuple5
    print('tuple4 is now empty', tuple4)
    
tupleMethods()
