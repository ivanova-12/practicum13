for num in range(100, 1000):
    if ((len(set(str(num)))) == 3
        and len(set(str(num * 3)) & set(str(num))) == 0
        and len(set(str(num * 3))) == 3 and num * 3 < 1000):

        print(f"{num}+{num}+{num}={num * 3}")

