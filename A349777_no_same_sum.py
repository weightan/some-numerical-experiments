#A349777

from tqdm import tqdm

from itertools import combinations

def seq2():
    terms = [1]
    sums = set()

    for i in tqdm(range(10)):

        t = terms[-1]
        c = True
        while c:
            t+=1
            for j in terms:
                if j+t in sums:
                    break
            else:
                break

        for j in terms:
            sums.add(j+t)

        terms.append(t)

        

    print(terms)

def seq4(n):
    from itertools import combinations

    terms = [1]
    
    sums2 = set()
    sums3 = set()
    sums4 = set()

    for i in range(n):

        t = terms[-1]
        c = True
    
        while c:
            h = True
            h2 = True
            h3 = True

            p = 0
            t += 1

            for j in terms:
                if j+t in sums2 :
                    h = False
                    break
           
            if h:
                for j in sums2:
                    if j+t in sums3 :
                        h2 = False
                        break

            if h and h2:
                for j in sums3:
                    if j+t in sums4 :
                        h3 = False
                        break

            if h and h2 and h3:
                break

        
        terms.append(t)
        

        for j in combinations(terms, 2):
            sums2.add(sum(j))

        for j in combinations(terms, 3):
            sums3.add(sum(j))
            
        for j in combinations(terms, 4):
            sums4.add(sum(j))

        print(t, end = ', ')

    print(len(terms), terms)

seq4(1000)