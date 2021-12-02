from tqdm import tqdm



def check_n(r, n, len_s = 3):
    r.extend(map(int, str(n))) 

    #какая-то последоваетльность из трех элементов (цифр) подрад убывает

    return all(r[i:i+len_s][0] != r[i:i+len_s][1] != r[i:i+len_s][2]  for i in range(0, len(r)-len_s+1)) 

    #return any( all(r[i:i+len_s][j] > r[i:i+len_s][j+1] for j in range(len_s - 1)) for i in range(0, len(r)-len_s+1))

    # for i in range(0, len(r) - len_s + 1):
    #     d = r[i:i+len_s]
    #     if all(d[j] > d[j+1] for j in range(len_s - 1)):
    #         return False
    # return True

def seq():

    len_s = 3

    digits = [1]
    terms = [1]

    appers = set(terms)

    for i in tqdm(range(10_000)): 
        t = 1 
        #while not(t not in appers and  check_n(digits[-len_s + 1:], t, len_s) ) :
        while not(t not in appers and  check_n(list(map(int, str(terms[-1]))), t, len_s) ) :
            t += 1
        digits.extend( map(int, str(t)) ) 
        appers.add(t)
        terms.append(t)
        #print(t)


    print(terms[:50])

    import matplotlib.pyplot as plt

    plt.plot(terms, ',') #, [i for i in range(len(terms))], 'r--'
    plt.ylabel('')
    plt.show()



if __name__ == "__main__":
    seq()

    #print(check_n([1, 2], 1000, 3))
