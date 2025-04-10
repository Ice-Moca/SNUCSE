def selSort(nums):   
    # sort nums into ascending order
    n = len(nums) 
    for bottom in range(n-1):   
    # nums[bottom] ~ nums[n-1]에서 가장 작은값 찿기   
      mp = bottom 
      for i in range(bottom+1, n): 
         if nums[i] < nums[mp]: 
            mp = i      # nums[mp]가 가장 작은값
      # swap the smallest item to the bottom
      temp         = nums[bottom]
      nums[bottom] = nums[mp]
      nums[mp]     = temp

data = [29, 64, 73, 34, 20]
selSort(data)
