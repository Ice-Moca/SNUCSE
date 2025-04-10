def   mysort(lst):
    import math
    result = [ ]
    for i in range( 0, len(lst)):
       index_lv = 0
       least_value = lst[0]
       for j in range( 0, len(lst)):
            if  least_value >= lst[j] :
                index_lv = j 
                least_value = lst[j]

       lst[index_lv] =  math.inf
       result = result + [ least_value ]
       print("least-value-position: ", index_lv)
       print("result: ", result)
       print("lst: ", lst)
    return result
