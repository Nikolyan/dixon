# Python 3 implementation of Dixon factorization algo

from math import sqrt, gcd, ceil
import numpy as np


# Function to find the factors of a number
# using the Dixon Factorization Algorithm
def factor(n, b=7):

    # Factor base for the given number , 11, 13, 17, 19, 23, 29, 31, 37, 41
    base = []
    for num in range(2, b + 1):
        if all(num % i != 0 for i in range(2, num)):
            base.append(num)


    # Starting from the ceil of the root
    # of the given number N
    start = int(ceil(sqrt(n)))

    # Storing the related squares
    pairs = []

    # For every number from the square root
    # Till N
    for i in range(start, n+1):

        # Finding the related squares
        for j in range(len(base)):
            lhs = i ** 2 % n

            rhs = base[j] ** 2 % n
            if i == 970:
                print (i ** 2 % n, base[j] ** 2 % n)
            # If the two numbers are the
            # related squares, then append
            # them to the array
            if (lhs == rhs):
                pairs.append([i, base[j]])
    new = []
    print(pairs)
    # For every pair in the array, compute the
    # GCD such that
    for i in range(len(pairs)):
        factor = gcd(pairs[i][0] - pairs[i][1], n)
        # If we find a factor other than 1, then
        # appending it to the final factor array
        if (factor != 1):
            new.append(factor)

    x = np.array(new)
    # Returning the unique factors in the array
    a = np.unique(x)
    result = []
    for i in range(len(a)):
        result.append([a[i], n//a[i]])

    return (result)


# Driver Code
if __name__ == "__main__":
    a = factor(12389307)
    print(a)
