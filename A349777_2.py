def seq4(n):
    from itertools import combinations

    terms = [1]
    
    sums2 = set()
    sums3 = set()
    sums4 = set()

    for i in range(n):

        t = terms[-1]
    
        while True:
            h = True
            h2 = True
            h3 = True

            
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

    
        sum2_temp = set()
        sum3_temp = set()
        sum4_temp = set()
        

        for j in terms:
            sum2_temp.add(j + t)
        

        for j in sums2:
            sum3_temp.add(j + t)


        for j in sums3:
            sum4_temp.add(j + t)

        terms.append(t)
        
        sums2.update(sum2_temp)
        sums3.update(sum3_temp)
        sums4.update(sum4_temp)

        print(t, end = ', ')

    print(len(terms), terms)


#7650495, 9219214, 11365472, 13253331, 15827645
seq4(100)