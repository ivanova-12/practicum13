import itertools

set_of_nums = {int(num) for num in input().split()}
list_of_sets = []

for i in range(len(set_of_nums) + 1):
    list_of_sets.extend((set(combin) for combin in itertools.combinations(set_of_nums, i)))

print(list_of_sets)

