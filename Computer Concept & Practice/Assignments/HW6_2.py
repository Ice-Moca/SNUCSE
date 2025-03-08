def first_perfect_square(numbers):
    for i in range(len(numbers)):
        if numbers[i] > 0:
            if (numbers[i]**(0.5))==(numbers[i]**(0.5))//1:
                return i
    
    return -1

def num_perfect_square(numbers):
    result = 0
    for i in range(len(numbers)):
        if numbers[i] > 0:
            if (numbers[i]**(0.5))==(numbers[i]**(0.5))//1:
                result+=1 
    return result


def second_largest(values):
    max_index= 0
    for i in range(len(values)):
        if values[i] >= values[max_index]:
            max_index=i
            second_index=i-1
    for j in range(len(values)):
        if j != max_index:
            if values[j]>= values[second_index]:
                second_index=j
    return values[second_index]

'''
print(second_largest([3,-2,10,-1,5]))
print(second_largest([1,2,3,3]))
print(second_largest([-2,1,1,-3,5]))
print(second_largest([3.1,3.1]))
print(second_largest(['apla','beta','gamma','delta']))
print(second_largest([True,False,True,False]))
print(second_largest([True,False,False]))
'''