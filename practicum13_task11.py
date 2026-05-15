board = []

for i in range(9):
    str_of_nums = input().split()
    board.append(str_of_nums)

    for elem in str_of_nums:
        if ((str_of_nums.count(elem) > 1 and elem != '.')
            or (elem != '.' and int(elem) >= 10)
            or (elem != '.' and int(elem) < 1)):
            print('False')
            exit()

for i in range(9):
    column = []
    for j in range(9):
        column.append(board[j][i])

    for elem in column:
        if ((column.count(elem) > 1 and elem != '.')
            or (elem != '.' and int(elem) >= 10)
            or (elem != '.' and int(elem) < 1)):
            print('False')
            exit()

for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        block = []
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                block.append(board[x][y])

        for elem in block:
            if elem != '.' and block.count(elem) > 1:
                print('False')
                exit()

print('True')










