def bubble_sort(items):
    """Implementation of insertion sort"""

    for i in range( len(items) ) :
         for j in range( len(items) - 1 - i ) : 
                  if items[j] > items[j+1] :                                      
                      temp = items[j]
                      items[j] = items[j+1]
                      items[j+1] = temp
         

data = [7, 5, 42, 6, 3, 15]
bubble_sort(data)
data