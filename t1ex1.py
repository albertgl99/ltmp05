llista = [1, 2, 3, 4, 5]

def ordenada(llista):
    for i in range(len(llista)):
        for j in range(i + 1, len(llista)):
            if llista[i] < llista[j]:
                llista[i], llista[j] = llista[j], llista[i]
    return llista
    
print(ordenada(llista))