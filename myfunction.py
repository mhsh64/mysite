# added my own function, this function will remove duplicate words, if we have duplicate characters in input
def my_perm(y):
    if len(y) == 1:
        return [y]
    p = []
    temp = my_perm(y[1:])
    for i in temp:
        for x in range(len(i) + 1):
            p.append(i[:x] + y[0] + i[x:])
    return list(set(p))