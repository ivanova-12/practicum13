nums = [int(num) for num in input().split()]


if len(nums) < 3:
    print([])
else:
    list_of_right3 = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    list_of_right3.add(tuple(sorted([nums[i], nums[j], nums[k]])))

print([list(elem) for elem in sorted(list_of_right3)])

