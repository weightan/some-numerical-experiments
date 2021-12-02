from tqdm import tqdm

def check_n(n, s):

    n = list(map(int, str(n)))
    #s = list(map(int, str(s)))
    s.extend(n)

    return not any( (s[i-2] + s[i-1] + s[i]**2) % 3 == 1 for i in range(2, len(s)))



def seq():
    len_s = 3
    digits = [1]
    terms = [1]

    appers = set(terms)

    for i in tqdm(range(5_00)): 
        t = 1 
        while not(t not in appers and check_n(t, digits[-3:]) ) :
            t += 1

        #print(t)
        digits.extend( map(int, str(t)) ) 
        appers.add(t)
        terms.append(t)



    print(terms[:50])

    import matplotlib.pyplot as plt

    plt.plot(terms, ',') #, [i for i in range(len(terms))], 'r--'
    plt.ylabel('')
    plt.show()
    plt.close()

if __name__ == "__main__":

    #print(check_n(3, '12'))
    seq()
