def reverse_iter(s):
    rev_str = ""
    for ch in s:
        rev_str = ch + rev_str
    return rev_str


def reverse_iter(s):
    rev_str = ""
    for ch in s:
        rev_str = ch + rev_str
    return rev_str


def reverse(s, depth = 0):
    if (s == ""):
        return ""
    else:
        print(" " *depth, " reverse(" , s, " ): ", s[0] )
        return reverse(s[1:], depth + 1) + s[0]
    


reverse("hello")