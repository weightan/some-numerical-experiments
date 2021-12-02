from tqdm import tqdm


def NumToFib(n): # n > 0
    f0, f1, k = 1, 1, 0
    while f0 <= n:
        f0, f1, k = f0+f1, f0, k+1
    s = ""
    while k > 0:
        f0, f1, k = f1, f0-f1, k-1
        if f0 <= n:
            s+='1'
            n = n-f0
        else:
            s+='0'
    return s

def RevFibToNum(s):
    f0, f1 = 1, 1
    n, k = 0, 0
    while k < len(s):
        if s[k] == "1":
            n = n+f0
        f0, f1, k = f0+f1, f0, k+1
    return n

def seq():
    n = 0
    a = 0
    smax, expn, n2n = 0, 0, 1

    while 1:
        a += 1
        aa = a

        sa = NumToFib(aa)
        ar = RevFibToNum(sa)

        s = 0
        while aa != ar and s < smax+100:
            s += 1
            aa = aa+ar

            sa = NumToFib(aa)
            ar = RevFibToNum(sa)

        if aa == ar:
            if s > smax:
                print("######", a, s, NumToFib(a)) # ###### A348571 A348572
                smax = s
        else: # a != ar
            n += 1
            if n == n2n:
                print(expn, a) # n A348570(2^n)
                expn += 1
                n2n *= 2


def a(n, iters):
    t = NumToFib(n)
    if all(t[i] == t[-i-1] for i in range(len(t)//2)):
        return iters
    elif iters < 200:
        return a(n + RevFibToNum(NumToFib(n)), iters+1)
    else:
        return iters

def is_a_polynd(s):
    return all(s[i] == s[-i-1] for i in range(len(s)//2))

    # for i in range(len(s)//2):
    #     if s[i] != s[-i-1]:
    #         return False
    # return True
    

def a_for(n):
    nnew = 0

    for i in range(1, 10**5):
        nnew = n + RevFibToNum(NumToFib(n))

        t = NumToFib(n)

        if all(t[i] == t[-i-1] for i in range(len(t)//2)):
            return i

        if nnew == n:
            return 'cycle'

        print(len(str(nnew)))

        n = nnew

    return None



    


if __name__ == "__main__":
    #seq() 

    a_for(59)

    # for i in range(1, 100):
    #     print(i, a_for(i))
        

    #print([i + RevFibToNum(NumToFib(i)) for i in range(1, 100)])

