from sympy import factorint, primefactors, divisors, divisor_count
c = [4, 7, 10, 13, 19, 22, 25, 31, 34, 37, 43, 46, 55, 58, 61, 67, 73, 79, 82, 85, 94, 97, 103, 106, 109, 115, 118, 121, 127, 139, 142, 145, 151, 157, 163, 166, 178, 181, 187, 193, 199, 202, 205, 211, 214, 223, 226, 229, 235, 241, 253, 262, 265, 271, 274, 277, 283, 289, 295, 298]
c = c[:100]


nn = 300
s = [True]*((nn)//3 + 1)
for i in range(4, nn, 3):
    if s[(i-1)//3]:
        for t in range(4, (nn )//i, 3):
            s[(i*t-1)//3] = False
print([3*i + 1 for i in range(1, (nn + 3)//3) if s[i]])





def siev_2(nn = 300):
    s = [True]*((nn)//3 + 1)
    for i in range(4, nn, 3):
        if s[(i-1)//3]:
            for t in range(4, (nn)//i, 3):
                s[(i*t-1)//3] = False
    terms = [3*i + 1 for i in range(1, (nn + 3)//3) if s[i]]

    # print(terms[:len(c)])
    print( terms[:len(c)] == c)
    if terms[:len(c)] != c:
        print (terms[:len(c)], )
    # print(c)

    g = terms[len(terms)//2]
    print( all(d%3 != 1 or d == 1 or d == g for d in divisors(g)))


def siev(nn):
    #nn = 100
    s = [True]*nn
    for i in range(4, nn, 3):
        if s[(i-1)//3]:
            j = i
            while j < nn - i:
                j  += i
                if j % 3 == 1: s[(j-1)//3] = False
    terms = [3*i + 1 for i in range(1,1 + (nn-1)//3) if s[i]]

    #print(terms[len(c)+1])
    print(terms[len(c)+1] == c)
    #print(c)


import time

if __name__ == "__main__": 
    pass
    for i in range(300, 501):
        siev_2(i)
    

    # start = time.time()
    # siev_2(10**7)
    
    # end = time.time()
    # print(end - start)
    

    #p = [i for i in range(4, 300, 3) if all(d%3 != 1 or d == 1 or d == i for d in divisors(i))]

    #print(p)


