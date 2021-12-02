
from tqdm import tqdm
import  random

def findcycle(c):
    for i in range(2, len(c)//2):
        if c[len(c)-i : ] == c[len(c)-i*2 : len(c)-i]:
            return c[len(c) - i:]
    return []

def find_cycle2(c):
    for i in range(2, len(c)):
        if c[-i] == c[-1]:
            return i - 1 
    return 0

# terms, appears = [2], {2:True}
# for n in tqdm(range(1, 50_000)):
#     for m in range(n-1, 0, -1):
#         if terms[m-1] == terms[n-1]:
#             terms.append(n-m); appears[n-m]=True; break 
#     else:
#         t = 1
#         while appears.get(t) is not None:
#             t += 1
#         terms.append(t-1);appears[t-1]=True

# print(terms, terms[:len(c)] == c)


def make_seq(st = 2):

    #[3, 2, 4, 2]
    #[8, 1, 9]

    #st = [random.randint(1, 10) for i in range(random.randint(1, 4))]

    terms = st.copy()
    appears =  set(terms)

    for n in range(1, 3*10**4):
        for m in range(n-1, 0, -1):
            if terms[m-1] == terms[-1]:
                terms.append(n-m);appears.add(n-m);break 
        else:
            t = 1
            while t in appears:
                t+=1
            terms.append(t-1); appears.add(t-1)

        if n in [50, 100, 200, 600, 1000, 2000, 5000, 10000, 30000]:
            s = findcycle(terms)
            if s != []:
                print(st, len(s), n, s)
                return 0 

    print(st, None)


def make_orig():
    terms = [2]
    appears =  set(terms)

    for n in tqdm(range(1, 5 00_000)):
        for m in range(n-1, 0, -1):
            if terms[m-1] == terms[-1]:
                terms.append(n-m);appears.add(n-m);break 
        else:
            t = 1
            while t in appears:
                t+=1
            terms.append(t-1); appears.add(t-1)

    s = findcycle(terms)
    print(s)

    for i in range(max(appears)):
        if i not in appears:
            print(i)
            break


# import matplotlib.pyplot as plt
# plt.plot(terms, ',', [i for i in range(len(terms))], 'r--')
# plt.ylabel('some numbers')
# plt.show()


if __name__ == "__main__":
    make_orig()
    # for i in range(3, 10**3):
    #     make_seq(i)