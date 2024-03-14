def imprimir_3veces(unacadena):
    print(unacadena)
    print(unacadena)
    print(unacadena)
    return ""
--------------------------------------------------------------------------------
def calcular_promedio(a,b):
    promedio=(a+b)/2
    return promedio
--------------------------------------------------------------------------------
def calcular_promedio3(a,b,c):
    promedio=(a+b+c)/3
    return promedio
--------------------------------------------------------------------------------
def valor_abs(a):
    modulo=0
    if a>0:
        modulo=a
    else:
        a<0
        modulo=a*(-1)
    return modulo
--------------------------------------------------------------------------------
def exclamar(unacadena):
    cad="¡"+unacadena+"!"
    return cad
--------------------------------------------------------------------------------
def gritar(unacadena):
    cad="¡¡¡"+unacadena+"!!!"
    return cad
--------------------------------------------------------------------------------
def divisores_positivos(a):
    contador=0
    for i in range(1,a+1):
        if a%i==0:
            contador=contador+1
    return contador
--------------------------------------------------------------------------------
def es_primo(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True
--------------------------------------------------------------------------------
def retorna_mayor2(a,b):
    if a>b:
        return a
    else:
        if a<b:
            return b
--------------------------------------------------------------------------------
def retorna_mayor3(a,b,c):
    if a>b and a>c:
        return a
    else:
        if a<b and b>c:
            return b
        else:
            if c>a and c>b:
                return c
--------------------------------------------------------------------------------
def potencia(a,b):
    pot=a**b
    return pot
--------------------------------------------------------------------------------
def sumadivpropios(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    return suma
--------------------------------------------------------------------------------
def numeroperfecto(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    if suma==a:
        print(a,"Es un numero perfecto")
    else:
        print(a,"No es un numero perfecto")
    return suma
--------------------------------------------------------------------------------
def numeroabundante(a):
    suma=0
    for i in range(1,a):
        if a%i==0:
            suma=suma+i
    if suma>a:
        print(a,"Es un numero abundante")
    else:
        print(a,"No es un numero abundante")
    return suma
--------------------------------------------------------------------------------
#numero poderoso
def es_primo(a):
    for i in range(2,a):
        if a%i==0:
            return False
    return True

def numeropoderoso(a):
    for i in range(2,a):
        if a%i==0 and es_primo(i):#si el i es divisor de a y a su vez es primo
            if a%(i**2)!=0:
                return False
    return True
--------------------------------------------------------------------------------