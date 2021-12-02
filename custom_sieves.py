from sympy import factorint, primefactors, divisors, divisor_count

def siev():
    #A257144
    nn = 200
    terms, s = [], [True]*nn
    for i in range(2, nn):
        if s[i]:
            j=i
            while j < nn - i**2:
                j  += i**2; s[j] = False
    print([i for i in range(nn) if s[i]])



def siev_2():
    D = 10**3
    s = [1]*D
    terms = []

    for i in range(2, D):
        if s[i] == 1:
            j  = i
            while j < D:
                j  = j*3 - 1
                if j < D:
                    s[j] = 0
    for i in range(D):
        if s[i] == 1: 
            terms.append(i)

    print(terms, len(terms))

if __name__ == "__main__": 
    siev()
    #siev_2()
