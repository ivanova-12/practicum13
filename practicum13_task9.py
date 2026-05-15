import itertools

set_of_nums = {int(num) for num in input().split()}
n_len_set_of_nums = len(set_of_nums)
k_num = int(input())

if k_num <= n_len_set_of_nums:
    list_of_sets = [set(combin) for combin in itertools.combinations(set_of_nums, k_num)]
    print(list_of_sets)
else:
    print('Нет таких подмножеств')

