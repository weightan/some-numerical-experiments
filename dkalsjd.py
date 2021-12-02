
suc = lambda x: [x]
pred = lambda x : x[0]

summ = lambda x, y: summ(suc(x), pred(y)) if y !=[] else [x]

prod = lambda x, y: prod(summ(x, x), pred(y)) if y !=[] else x

print(prod([], [[[]]]))