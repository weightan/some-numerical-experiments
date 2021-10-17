import numpy as np
from numpy.linalg import LinAlgError
from scipy.linalg import circulant
import math
import random

import itertools 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import math

from tqdm import tqdm

from PIL import Image
from matplotlib import cm

from numba import jit
from numpy import linalg as LA

def make_m_fase_p(N):
    sc = 15j
    offset = sc/2
    dim = 4

    # index1 = (1, 1)
    # index2 = (3, 4)

    index1 = np.random.randint(dim, size=(2) )
    index2 = np.random.randint(dim, size=(2) )

    coef = np.zeros((N, N))

    M = np.random.choice([-1, 1], (dim, dim) ).astype(complex)

    for i in tqdm(range(N)):
        for j in range(N):
            C = M
            C[index1[0], index1[1]] = sc* (i/N) - offset
            C[index2[0], index2[1]] = sc* (j/N) - offset

            coef [i, j] = np.angle(LA.eigvals(C)[-1])

    return coef


def make_m_eigenfish(N):
    sc = random.uniform(-5, 5) + random.uniform(-5, 5 ) *1j
    cscale = 0.09
    offset = random.uniform(-5, 5) + random.uniform(-5, 5 )*1j 
    dim =6 

    # index1 = (2, 1)
    # index2 = (3, 4)

    index1 = np.random.randint(dim, size=(2) )
    index2 = np.random.randint(dim, size=(2) )

    coef = np.zeros((N, N))

    M = np.random.choice([-1, 1], (dim, dim) ).astype(complex)

    for i in tqdm(range(N)):
        for j in range(N):
            C = M
            C[index1[0], index1[1]] = sc* (i/N )*1- offset
            C[index2[0], index2[1]] = sc* (j/N)*1 - offset

            for t in LA.eigvals(C):
                x = t.real*N*cscale + N*0.5
                y = t.imag*N*cscale + N*0.5
                if 0 < x < N and 0 < y < N :

                    coef[math.floor(x) , math.floor(y)] += 1

    return coef


def run():

    #coef = make_m_fase_p(N = 500)
    coef = make_m_fase_p(N = 1000)

    size = 5
    plt.figure(num = None, figsize=(size, size), dpi=300)

    plt.axis('off')
    #cmap = 'hot'
    cmap = 'twilight'

    plot = plt.imshow(coef, cmap = cmap ) #, interpolation='bicubic'

    ####

    filenameImage = f'{random.random()}.png'

    plt.savefig(filenameImage, bbox_inches = 'tight')

    #plt.show()
    plt.close()

if __name__ == '__main__':
    for i in range(100):
        run()
