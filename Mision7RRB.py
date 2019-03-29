#Rafael Romero Bello A01747730
#Es un menu donde se puede realizar dos operaciones.

def encontrarMayor():
    n=0
    nm=0
    n = int(input("introduce tu valor[coloca -1 para salir]:"))
    nm = n
    while n!=(-1):
        if n<0 and n!=-1:
            print("tus numeros deben de ser positivos")
        elif n>nm:
            nm=n
        n = int(input("introduce tu valor[coloca -1 para salir]:"))
    if nm==-1:
        print('no hay numeros mayores')
    else:
        print(nm)

def dividirnumerosporrestas():
    c=0
    dividiendo = int(input('Teclea tu valor:'))
    divisor = int(input("Teclea tu divisor:"))
    residuo = dividiendo
    while residuo>=divisor:
          residuo-=divisor
          c+=1
    print(dividiendo, '/', divisor, '=', c, 'sobra', residuo)


print('1.-Calcular divisores')
print('2.-Encontrar el mayor')
print('3.-Salir')
x=int(input("Teclea tu opcion"))
while x!=3:
    if x>=1  and x<=2:
     if x==1:
         dividirnumerosporrestas()
     if x==2:
         encontrarMayor()
     if x>3:
         print('numero erroneo')


     print('1.-Calcular divisores')
     print('2.-Encontrar el mayor')
     print('3.-Salir')
     x = int(input("Teclea tu opcion"))
