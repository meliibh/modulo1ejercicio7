#7. (1 punto) Sube a un repositorio de git hub un programa que encuentre un intervalo que 
#tenga 73 números no primos seguidos y compártelo a través de su link en Git Hub


def es_primo(n):
    for x in range(2,n):
        if n%x == 0:
            return False
    return True

def seriePrimos(i):
    count=0
    val=1
    while count < i:
        val+= 1
        if es_primo(val):
            count+= 1
    print("El numero primo {} es: {}".format(count,val))
    
    
seriePrimos(73)