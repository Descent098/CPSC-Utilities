def sum(n):
    """Sums a value from 1 to n recursively"""

    #End of recursive calls
    if n ==1:
        return 1

    elif n == 0:
        return 0

    #Handle Edge cases
    if n < 0:
        return 0

    #
    else:
        return (n + sum((n-1)))

print(sum(10))
