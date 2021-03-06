# -*- coding: utf-8 -*-

# 44)
#Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
#Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and
#D = |Pk − Pj| is minimised; what is the value of D?

def penta(n):
    return n * (3 * n - 1) / 2

d = {penta(x): True for x in xrange(1, 10001)}
penta_keys = d.keys()

want = []

for k, i in enumerate(penta_keys):
    for j in penta_keys[k:]:
        if d.get(i+j, False) and d.get(abs(i-j), False):
            want.append((i, j))

smallest = want[0]
ans = abs(smallest[0] - smallest[1])
print ans # 5482660
