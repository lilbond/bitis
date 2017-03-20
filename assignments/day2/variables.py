# finding last index of element in list
def find_last_index(l, e):
    length = len(l)
    for index in range(0, length):
        if l[index] == e:
            x = index
    return x


# finding last index of element in list using negative index with lower complexity
def find_last_index_reverse(l, e):
    length = len(l)
    for index in range(-1, -(length+1), -1):
        if l[index] == e:
            return -(index+1)


l = [1, 2, 3, 4, 5]

print(find_last_index(l, 3))

print(find_last_index_reverse(l, 3))


# finding if an element is present inside list, if present return true
def is_present(l, e):
    length = len(l)
    for index in range(0, length):
        if l[index] == e:
            return True

print(is_present(l, 3))