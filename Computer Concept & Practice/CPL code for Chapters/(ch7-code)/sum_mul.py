def sum_mul(choice, *args):
    if choice == 'sum':
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result =1
        for i in args:
            result = result * i
    return result

result = sum_mul('sum', 1,2, 3, 4, 5)
print(result)

result = sum_mul('mul', 1,2,3,4,5)
print(result)
            