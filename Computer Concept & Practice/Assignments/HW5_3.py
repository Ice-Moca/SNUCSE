def BS_App():
    data = list(map(lambda s: eval(s), input("Type the ordered input data: ").split(" ")))
    index = list(map(lambda s: eval(s), input("Type the search_keys: ").split(" ")))
    for i in index:
        print("The location of search_key",i ,": position " + str(binary_search(data, i, 0, len(data) - 1)))
      
def binary_search(datalist, val, lower, upper):
    if lower <= upper:
        mid = (lower + upper) // 2
        if datalist[mid] == val:
            return mid
        elif datalist[mid] > val:
            return binary_search(datalist, val, lower, mid - 1)
        else:
            return binary_search(datalist, val, mid + 1, upper)
    else:
        return -1
      
if __name__== '__main__':
  BS_App()

def permute_App():
  N = int(input("Type the number of persons: "))
  flag =[False]*N
  progress = []
  permute(N, flag, progress)

def permute(N, flag, progress):
    arr=[i for i in range(1,N+1)]
    
    if len(progress) == N:
        print(progress)
        
    for i in range(len(arr)):
        if flag[i]==False:
            progress.append(arr[i])
            flag[i] = True
            permute(N, flag, progress)
            flag[i] = False
            progress.pop()

if __name__ == "__main__":
    permute_App()

'''
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()

    generate([], used)
  
permutation([1,2,3,4,5],3)
'''

