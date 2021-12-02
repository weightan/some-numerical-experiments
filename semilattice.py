
import itertools
from tqdm import tqdm
from collections import Counter
# from arrs import *
import math
import numpy as np
from sympy import primefactors, sieve
import matplotlib.pyplot as plt
import plotly.graph_objects as go

import networkx as nx


from itertools import chain, combinations, combinations_with_replacement

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def bin_operation(a, b, mod):
    return (a*b)%mod


def check_idemp(a, mod):
    return bin_operation(a, a, mod) == a


def absorption_laws(a, b, mod1, mod2):
    return bin_operation(a, bin_operation(a, b, mod1), mod2 ) == a and bin_operation(a, bin_operation(a, b, mod2), mod1 ) == a



def distributivity(a, b, c, mod1, mod2):
    return bin_operation(a, bin_operation(b, c, mod2), mod1) == bin_operation( bin_operation(a, b, mod1), bin_operation(a, c, mod1), mod2)


def is_distributiv(setp, mod1, mod2):
    for i in combinations_with_replacement(setp, 3):
        if distributivity(*i, mod1, mod2) == 0:
            return 0
    return 1

def check_ordered(setp, mod):
    for i in combinations(setp, 2):
        if bin_operation(i[0], i[1], mod) not in i:
            return 0
    return 1

def check_ordered_double(setp, mod1, mod2):
    for i in combinations(setp, 2):

        if bin_operation(i[0], i[1], mod1) not in i:
            return 0

        if bin_operation(i[0], i[1], mod2) not in i:
            return 0

        if bin_operation(i[0], i[1], mod1) ==  bin_operation(i[0], i[1], mod2) :
            return 0

    return 1


def inters(a, b):
    return list(set(a) & set(b))


def is_a_semigroup(setp, mod):
    for i in combinations_with_replacement(setp, 2):
        if bin_operation(i[0], i[1], mod) not in setp:
            return 0
    return 1


def is_a_lattice(setp, mod1, mod2):
    for c in combinations_with_replacement(setp, 2):
        if absorption_laws(c[0], c[1], mod1, mod2) == 0:
            return 0
    return 1

def make_a_table(setp, mod):
    d = {setp[i]: i for i in range(len(setp))}

    l = len(setp)

    M = np.zeros((l, l))

    for i in range(l):
        for j in range(l):
            M[i, j] = d[bin_operation(setp[i], setp[j], mod)]

    return M

def isomorphism_two_table(M1, M2):

    if M1.shape != M2.shape:
        return 0

    if  (np.array_equal(M1, M2) or
         np.array_equal(np.transpose(M1), M2) or
         np.array_equal(M1, np.transpose(M2)) or
         np.array_equal(np.transpose(M1), np.transpose(M2)) ):

        return 1

def check_isomorphism(setp, mod1, mod2, p = 0):
    M1 = make_a_table(setp, mod1)
    M2 = make_a_table(setp, mod2)
    if p == 1:
        print(M1)
        print(M2)

    return isomorphism_two_table(M1, M2)


def characterise(setp, mod1, mod2):
    d1 = is_distributiv(setp, mod1, mod2)
    d2 = is_distributiv(setp, mod2, mod1)

    d4 = check_ordered(setp, mod1)
    d5 = check_ordered(setp, mod2)

    d7 = check_ordered_double(setp, mod1, mod2)

    d6 = check_isomorphism(setp, mod1, mod2)

    print("ordered 2: ", d7 ,'is distributiv ', d1, d2,' is  ordered ', d4, d5, ' is isom ', d6,  setp, mod1, mod2)



def make_a_matrix(setp, mod):
    l = len(setp)
    M = np.zeros((l, l))

    for i in range(l):
        for j in range(l):
            M[i, j] = ((setp[i]*setp[j])%mod == setp[i])

    return M



def find_one_nums_like_h():
    arr = []
    for i in tqdm(range(2, 4_000)):
        out = []
        for j in range(0, i):
            if check_idemp(j, i):
                out.append(j)
        t = 0

        r = (out, i)

        if len(out) > 2:
            arr.append(r)

    out = []

    for k in tqdm(combinations(arr, 2)):
        t = inters(k[0][0], k[1][0])
        if len(t) > 3:
            g = (sorted(t),  k[0][1], k[1][1] ) 
            out.append(g)
            #print(g)

    for p in out:

        for i in powerset(p[0]):
            if is_a_semigroup(i, p[1]) and is_a_semigroup(i, p[2]):
                if len(i) > 3 and is_a_lattice(i,  p[1],  p[2]):

                    characterise(i,  p[1],  p[2])



def find_sets_like_hilbert():
     for i in range(1, 31):
        t = 0

        #print(i)
        for s in powerset(range(0, i)):
            c = 1
            

            for k in combinations_with_replacement(s, 2):
                if k[0] == k[1]:
                    if (k[0] * k[0])%i != k[0]:
                        c = 0 
                        break

                if (k[0] * k[1])%i not in s:
                    c = 0 
                    break

            if c == 1 and s != () :
                #print([s, i], ',')
                t +=1

        print(i, t)


import matplotlib.pyplot as plt
import networkx as nx

def show_graph_with_labels(adjacency_matrix, mylabels):
    rows, cols = np.where(adjacency_matrix == 1)
    edges = zip(rows.tolist(), cols.tolist())
    gr = nx.Graph()
    gr.add_edges_from(edges)
    nx.draw(gr, node_size=500, labels=mylabels, with_labels=True)
    plt.show()

def visualize(arr, mod):
    M = make_a_matrix(arr, mod)
    print(M)
    mylabels = {i:str(arr[i]) for i in range(len(arr))}
    G = nx.from_numpy_matrix(M, create_using=nx.DiGraph)
    options = {
    'node_color': 'white',
    'node_size': 400,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 22,
    }
    nx.draw_circular(G, labels=mylabels, arrows=True, **options)
    plt.draw()
    plt.show()

if __name__ == "__main__":
    #find_sets_like_hilbert()
    find_one_nums_like_h()
    #(0, 190, 855, 1065), 1330, 1995

    # visualize((0, 385, 595, 925), 1155)
    # visualize((0, 385, 595, 925), 2310)

    #check_isomorphism((0, 190, 855, 1065) ,1330, 1995, 1)

    
    

    


