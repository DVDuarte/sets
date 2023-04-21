meu_set = {1, 2, 3, 4, 1}
meu_set_2 = set([1, 2, 8, 9, 10])

setUniao = meu_set.union(meu_set_2)
print(setUniao)

setIntersecao = meu_set.intersection(meu_set_2)
print(setIntersecao)

setDiferenca = meu_set.difference(meu_set_2)
print(setDiferenca)

setDiferencaSimetrica = meu_set.symmetric_difference(meu_set_2)
print(setDiferencaSimetrica)