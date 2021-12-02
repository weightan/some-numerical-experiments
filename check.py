#10964160
from sympy import factorint, primefactors, divisors, divisor_count
def make_seq(n):
    s, t = [1], True
    while t:
        s.append(n*divisor_count(s[-1]) )
        for i in range(2, len(s)):
            if s[-i] == s[-1]:
                t = False
                #print(s)
                return( i - 1)

print(make_seq(14580000 ))
c = [1, 4, 15, 30, 42, 360, 196, 525, 2080, 320, 7168, 123200, 35200, 150920, 196000, 1232000, 61236, 466560]
for i in [factorint(i) for i in c]:
    print(i)

