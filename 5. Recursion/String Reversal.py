def str_rev(a_str):
    rev_str = ""
    if len(a_str) == 1:
        return a_str
    else:
        rev_str = str_rev(a_str[1:]) + a_str[0]
    return rev_str

print(str_rev("me thinks its a weasel"))