def msort(list):
    if len(list) == 0 or len(list) == 1: # base case
        return list[:len(list)] # copy the input
    # recursive case
    halfway = len(list) // 2
    list1 = list[0:halfway]
    list2 = list[halfway:len(list)]
    newlist1 = msort(list1)  # recursively sort left half
    newlist2 = msort(list2)  # recursively sort right half
    newlist  = merge(newlist1, newlist2)
    return newlist

def merge(a, b):
    index_a = 0 # the current index in list a
    index_b = 0 # the current index in list b
    c = []
    while index_a < len(a) and index_b < len(b):
        if a[index_a] <= b[index_b]:
            c.append( a[index_a] )
            index_a = index_a + 1
        else:
            c.append( b[index_b] )
            index_b = index_b + 1
    # when we exit the loop
    # we are at the end of at least one of the lists
    c.extend(a[index_a:])
    c.extend(b[index_b:])
    return c

data = [84, 27, 49, 91, 32, 53, 63, 17]
msort(data)
