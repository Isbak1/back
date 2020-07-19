def calc_factorielle(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    return fact



nb = 14
factorielle_nb = calc_factorielle(nb)
print("{}! = {}".format(nb, factorielle_nb))
