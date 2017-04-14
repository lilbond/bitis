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


# # count and print number is list
#
# def count_and_print(l):
#     dic = {}
#     length = len(l)
#     for index in range(0, length):
#         if dic[l[index]] is None:
#             dic[l[index]] = 1
#         else:
#             dic[l[index]] = dic[l[index]] + 1
#
#     for key, value in dic.items():
#         print(key, value)
#
#
# l = [1, 2, 3, 4, 5, 2, 3, 4, 5, 6]
#
# count_and_print(l)