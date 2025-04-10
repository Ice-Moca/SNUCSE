def molecular_wight():
    print("Please enter the number of each atom!!! ")
    C = input("carbon: ")
    H = input("hydrogen: ")
    O = input("oxygen: ")
    W = C*12.011 + H*1.0079 + O*15.9994
    print()
    print ("The molecular weight of C_%d H_%d O_%d is: %d" % (C, H, O, round(W, 2)) ) 

def molecular_wight_correct():
    print("Please enter the number of each atom!!! ")
    C = eval(input("carbon: "))
    H = eval(input("hydrogen: "))
    O = eval(input("oxygen: "))
    W = C*12.011 + H*1.0079 + O*15.9994
    print()
    print ("The molecular weight of C_%d H_%d O_%d is: %d" % (C, H, O, round(W, 2)) ) 