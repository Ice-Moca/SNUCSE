def f_rec1(tree):
    if len(tree)==0:
        return 0
    elif any(tree[1:])==0:
        return 1
    else:
        return max(1+f_rec1(tree[1]),1+f_rec1(tree[2]))

def f_rec2(tree):
    if len(tree)==0:
        return 0
    elif any(tree[1:])==0:
        return 1
    else:
        return 1+f_rec2(tree[1])+f_rec2(tree[2])

def f_rec3(tree):
    if len(tree)==0:
        return 0
    elif any(tree[1:])==0:
        return tree[0]
    else:
        return tree[0]+f_rec3(tree[1])+f_rec3(tree[2])

def f_rec4(tree):
    if len(tree)==0:
        return
    elif any(tree[1:])==0:
        print(tree[0])
    else:
        f_rec4(tree[1])
        print(tree[0])
        f_rec4(tree[2]) #잘됨

# Binary Tree랑 Binary search Tree랑 다르다

f_rec4([2,[1,[],[]],[3,[],[4,[],[]]]])

def f_rec5(tree):
    if len(tree)==0:
        return -1
    elif any(tree[1:])==0:
        return tree[0]
    else:
        return f_rec5(tree[1])
