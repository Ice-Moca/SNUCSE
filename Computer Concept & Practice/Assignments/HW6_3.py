def count_matches(some_list,value):
    if len(some_list)==0:
        return 0
    if some_list[0]==value:
        return 1+count_matches(some_list[1:],value)
    else:
        return count_matches(some_list[1:],value)

def double_each(some_list):
    if len(some_list)==0:
        return []
    return [some_list[0]]*2 + double_each(some_list[1:])

def sums_to(nums,k):
    if len(nums) == 0:
        if k == 0:
            return True
        else:
            return False
    return sums_to(nums[1:],k - nums[0])

def is_reverse(string1,string2):
    if len(string1)==0 or len(string2)==0:
        if len(string1)==0 and len(string2)==0:
            return True
        else:
            return False
    if string1[0]==string2[-1]:
        return is_reverse(string1[1:],string2[:-1])
    else:
        return False
def sort_repeated(l):
    lst = []
    for i in set(l):
        if l.count(i) > 1:
            lst.append(i)
    return sorted(lst)
def make_dict_number(lst):
    return {n:lst.count(n) for n in sorted(lst)}
def make_dict_number(lst):
    freq = {}
    for n in lst:
        if freq.get(n):
            freq[n] += 1
        else:
            freq[n] = 1
    return dict(sorted(freq.items()))
def mostFrequent(lst):
    return sorted(make_dict_number(lst).items(), key = lambda x: x[1], reverse = True)[0][0]
def histogram(dic):
    return make_dict_number(list(dic.values()))

print(make_dict_number([2, 5, 3, 4, 6, 4, 2, 4, 5]))