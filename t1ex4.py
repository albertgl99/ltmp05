paraula1 = 'orden'
paraula2 = 'nerdoasd'

def es_anagrama(p1,p2):
    flag = True
    for x in p1:
        if x not in p2 or paraula1.count(x) != paraula2.count(x):
            flag = False
    return flag
            
if es_anagrama(paraula1,paraula2):
    print('Son anagramas')
else:
    print('No son anagramas')
