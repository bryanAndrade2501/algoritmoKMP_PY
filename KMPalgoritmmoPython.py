#Algoritmo de KMP
#Bryan Andrade
patron = "hola"
texto = "hola mundo"

def findKMP(texto, patron):
    n = len(texto)
    m = len(patron)
    comprobar = False
    strResultados = ""
    if(m == 0):
        return strResultados
        comprobar = false
    fail = computeFailKMP(patron)
    j = 0
    k = 0
    while(j < n):
        if texto[j] == patron[k]:
            if k == m-1:
                strResultados+= (j-m+1) + ","
                k=0
            j+1
            k+1
        elif k>0:
            k = fail[k-1]
        else:
            j+1
    return strResultados




def computeFailKMP(pattern):
    m = len(pattern)
    fail = []
    j = 1
    k = 0
    while(j < m):
        if(pattern[j] == pattern[k]):
            fail[j] = k+1
            j+1
            k+1
        elif (k > 0):
            k = fail[k - 1]
        else:
            j+1
    return fail

findKMP(texto,patron)