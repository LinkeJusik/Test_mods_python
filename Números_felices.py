def felices(n):
    n = str(n)
    cont = 0
    for i in range(0,len(n),1):
        cont += pow(int(n[i]),2)
    cont=int(cont)
    if cont == 1:
        print(cont,"es un número felíz")
        return True
    elif cont == 4:
        print(cont,"NO es un número felíz")
        return False
    else:
        print(cont)
        return felices(cont)

def holiwi(n):
    if n>0:
        print("xd")
    else:
        print("no xd")