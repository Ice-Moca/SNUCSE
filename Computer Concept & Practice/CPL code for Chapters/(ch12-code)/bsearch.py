def bsearch(items, key, lower, upper):
    if lower + 1 == upper:
        return None
    mid = (lower + upper) // 2
    if key == items[mid]: 
        return mid
    if key < items[mid]:
        return bsearch(items, key, lower, mid)
    else:
        return bsearch(items, key, mid, upper)


items = [ 13, 25, 33, 37, 41, 48, 58, 60, 67, 72, 74, 78]
key = 37
loc_of_key = bsearch(items, key, -1, len(items))