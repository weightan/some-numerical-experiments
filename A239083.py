from tqdm import tqdm

c = [1, 2, 10, 3, 11, 4, 12, 13, 14, 15, 5, 6, 16, 17, 7, 8, 18, 19, 9, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 200, 201, 121, 122, 130, 202]


digits = [1, 2]
terms = [1, 2]
appers = set(terms)

def check_n(r, n):
    r.extend(tuple(map(int, str(n)))) 
    for i in range(0, len(r)-2):
        d = r[i:i+3]
        if d[0] > d[1] > d[2]: return False
    return True

maxt = 1

for i in tqdm(range(20_000)):
    t = 1 #t in appers and not check_n(digits[-3:], t)
    while not(t not in appers and  check_n(digits[-3:], t) ) :
        t += 1
    digits.extend( tuple(map(int, str(t))) )
    appers.add(t); terms.append(t)

    if i % 1000 == 0:
        for j in range(maxt, max(appers)):
            if j not in appers:
                print(maxt, j - maxt)
                maxt = j
                break

# out = []
# for i in range(1, max(appers)):
#     if i > 100 and i in appers and not  check_n([], i):
#         out.append(i)
# print(out)


print(terms[:len(c)] == c)

import matplotlib.pyplot as plt
plt.plot(terms, ',') #, [i for i in range(len(terms))], 'r--'
plt.ylabel('some numbers')
plt.show()


