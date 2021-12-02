from sympy import sieve, isprime

from constraint import *
import time

def solv():
    constr =  lambda a, b, c : a*b*c - b**3 - c**2  + a*b*c**2 == 16
    constr2 = lambda a, b, c : a != b != c
    n = 300

    print(n**3)

    problem = Problem()
    problem.addVariable("a", range(0, n))
    problem.addVariable("b", range(0, n))
    problem.addVariable("c", range(0, n))

    problem.addConstraint(constr,  ("a", "b", "c"))
    problem.addConstraint(constr2, ("a", "b", "c"))

    print(problem.getSolution())

def concat_solve(n, maxt = None):
    # n = 14
    # maxt = 111317192232931437375341

    sieve.extend_to_no(n)
    p = list(map(str, list(sieve._list)))[:n][::-1]

    #print(p)

    problem = Problem()


    if maxt is None:
        maxt = int(''.join(p))

    constr = lambda *x : isprime(int(''.join(x)))
    not_that_solution = lambda *x: int(''.join(x)) < maxt


    problem.addVariables(range(0, n), p)
    problem.addConstraint(AllDifferentConstraint())

    problem.addConstraint(constr, range(0, n))
    problem.addConstraint(not_that_solution, range(0, n))

    problem.addConstraint(lambda x: x == '11', (0,))
    problem.addConstraint(lambda x: x == '13', (1,))
    problem.addConstraint(lambda x: x == '17', (2,))
    problem.addConstraint(lambda x: x == '19', (3,))
    problem.addConstraint(lambda x: x == '2',  (4,))
    problem.addConstraint(lambda x: x == '23', (5,))
    problem.addConstraint(lambda x: x == '29', (6,))
    problem.addConstraint(lambda x: x == '31', (7,))



    s = problem.getSolution()
    if s is not None:
        sol = int(''.join([ s[j] for j in range(n)]))
        return sol
    else:
        return 0

    # s = [ int(''.join([ i[j] for j in range(n)])) for i in s]

    # print(s)
    # print(min(s))


if __name__ == "__main__":
    n = 19
    sieve.extend_to_no(n)
    p = list(map(str, list(sieve._list)))[:n]

    print(p)

    t = None

    for i in range(100000):
        t = concat_solve(n , t)
        print(t)
        if t == 0:
            break


    
    
