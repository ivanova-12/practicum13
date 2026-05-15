import itertools

set_of_nums = sorted({int(num) for num in input().split()})
all_permutations = itertools.permutations(set_of_nums)

for perm in all_permutations:
    print(perm)



