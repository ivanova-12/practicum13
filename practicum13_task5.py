def eratosthenes_sieve(n: int) -> set:
    """Find all prime numbers less than n"""
    set_of_all_nums = set(range(2, n))

    for num in range(2, int(n**0.5 + 1)):
        if num in set_of_all_nums:
            multiples_j = set(range(num * num, n + 1, num))
            set_of_all_nums -= multiples_j

    return set_of_all_nums


if __name__ == '__main__':
    print(eratosthenes_sieve(int(input())))






