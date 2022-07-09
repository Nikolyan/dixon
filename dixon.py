import time
from datetime import timedelta
import pandas as pd
from math import gcd, sqrt, ceil


def dixon(n, p):
    size = len(p)
    val = {}
    #Step1
    for z in range(ceil(sqrt(n)), n):
        w = (z**2) % n
        if w == 0:
            continue
        w_pow = [0]*size #a vector
        #Step2
        for j in range(size):
            while w % p[j] == 0:
                w_pow[j] += 1
                w /= p[j]
        #Step3
        if w == 1:
            val[z] = w_pow

    keys_ = list(val.keys())
    pairs = []
    #Step4
    for i in range(len(keys_)):
        for j in range(i, len(keys_)):
            if keys_[i] != keys_[j]:
                arr_s = [0]*size
                flag = True
                for k in range(size):
                    arr_s[k] = val[keys_[i]][k] + val[keys_[j]][k] # a 'c' vector
                    if arr_s[k] % 2 == 1:
                        flag = False
                        break
                if flag:
                    d = {'pair1': keys_[i], 'pair2': keys_[j], 'vector': arr_s}
                    pairs.append(d)
    #Step5
    for elem in pairs:
        x = (elem['pair1'] * elem['pair2']) % n
        y = 1

        for a in range(size):
            y = y * p[a] ** (elem['vector'][a]//2)

        if  x != y and x != n-y and gcd(x+y, n) != 1 and n//gcd(x+y, n) != 1:
            return((gcd(x+y, n), n//gcd(x+y, n)))


if __name__ == "__main__":
    # times = []
    # for line in [225, 113703, 118881, 184815,
    #              332667, 776223, 988027, 6571435,
    #              8640247, 9683879, 12389307, 38374681,
    #              80397827]:
    #     start_time = time.monotonic()
    #     l = dixon(line, [2, 3, 5, 7])
    #     end_time = time.monotonic()
    #     print('Число '+str(line)+' разложено на '+str(l[0])+' и '+str(l[1])+', время разложения в секундах -> '+str(timedelta(seconds=end_time - start_time).seconds))
    #     times.append({f'{line}': timedelta(seconds=end_time - start_time).seconds})
    # pd.DataFrame(times).to_excel('time1.xlsx')
    l = dixon(7121*5839, [2, 3, 5, 7])
    print(l)