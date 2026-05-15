lst_of_nums = [int(num) for num in input().split()]
lst_of_repeated_nums = {num for num in lst_of_nums if lst_of_nums.count(num) > 1}
possible_num = int(input())

if possible_num in lst_of_repeated_nums:
    print(f"{possible_num} принадлежит множеству повторяющихся чисел")
else:
    print(f"{possible_num} не принадлежит множеству повторяющихся чисел")

