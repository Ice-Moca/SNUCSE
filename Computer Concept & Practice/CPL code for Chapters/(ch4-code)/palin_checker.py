def palindrome_checker( ):
    P_candidate = input("Type your pallindrome candiate: ")
    print ("Here is your pallindrome candiate:", P_candidate)
    P_candidate = P_candidate.lower( )
    print ("After lowering characters ==> ", P_candidate)
    #
    isPallindrome_candidate = True
    p1 = 0
    p2 = len(P_candidate) - 1
    #
    while isPallindrome_candidate and p1 < p2:
        if P_candidate[p1].isalpha( ):
            if P_candidate[p2].isalpha( ):
                if P_candidate[p1]==P_candidate[p2]:
                    p1 = p1 + 1
                    p2 = p2 - 1
                else:   isPallindrome_candidate = False
            else:  p2 = p2 -  1   # if not alphabet ==> move p2 to left
        else: p1 = p1 + 1         # if not alphabet ==> move p1 to right
#
    if  isPallindrome_candidate: 
           print ("Yes, your pallindrome candiate", P_candidate,  "is a real pallindrome!")
    else:  print ("No, your pallindrome candiate", P_candidate,  "is not a real pallindrome!")
