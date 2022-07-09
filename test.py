from math import sqrt, gcd
from sympy import Matrix

def Dixon(n, B):
    prime_base = []
    for num in range(2, B + 1):
        if all(num % i != 0 for i in range(2, num)):
            prime_base.append(num)
    prime_base_size = len(prime_base)
    x_i = int(sqrt(n)) + 1
    while x_i <= n:
        X = []
        Q_x_exponents = []
        V = []
        #print(x_i)
        while True:
            vect = [0] * prime_base_size
            Q_x_i = (x_i ** 2) % n
            Q_x_i_exponents = [0] * prime_base_size
            for j in range(0, prime_base_size):

                p_j = prime_base[j]
                while Q_x_i % p_j == 0:
                    Q_x_i = Q_x_i // p_j
                    vect[j] = (vect[j] + 1) % 2
                    Q_x_i_exponents[j] = Q_x_i_exponents[j] + 1
                if Q_x_i == 1:
                    X.append(x_i)
                    V.append(vect)
                    Q_x_exponents.append(Q_x_i_exponents)
                    break

            if len(X) >= prime_base_size:
                break
            x_i = x_i + 1


        A = Matrix(V)

        K = A.nullspace()

        K_size = len(K)
        for j in range(1, K_size):
            x = 1
            y = 1
            K_vect = K[j]
            y_exponent_vect = [0] * prime_base_size
            for k in range(0, len(X)):
                if K_vect[k] == 1:
                    x_factor = X[k]
                    for l in range(0, prime_base_size):

                        y_exponent_vect[l] = y_exponent_vect[l] + Q_x_exponents[k][l]
                    x = (x * x_factor) % n
            for l in range(0, prime_base_size):
                y = y * pow(prime_base[l], y_exponent_vect[l]//2) % n

        if x != y and x != n-y:
            d_1 = gcd(x+y, n)
            d_2 = n // d_1
            if d_1 != 1:
                return d_1,d_2
        x_i+=1

    return None


print(Dixon(97520247, 7))