def one():#el numero de la funcion es el numero del ejercicio
    print("hola")
def two():
    print(273)
def three():
    print(5.3)
def four():
    print(1234+532)
def five():
    print(1234-532)
def six():
    print(1234*532)
def seven():
    print(124/532)
def eight():
    i = 1
    while i <= 3:
        print(i)
        i+=1
def nine():
    for i in range(1,10):
        print(i)
def ten():
    i = 1
    while i <= 10000:
        print(i)
        i+=1
def eleven():
    for i in range(5,11):
        print(i)
def twelve():
    j = 5
    while j <= 15:
        print(j)
        j+=1
def thirteen():
    for i in range(5,15001):
        print(i)
def fourteen():
    for i in range(1,201):
        print("hola")
def fifteen():
    n = 1
    while n <= 30:
        print(n**2)
        n+=1
def sixteen():
    n = 1
    c = n
    while n < 5:
        c = c*(n+1)
        n = n + 1
        print(c)

def seventeen():
    i = 1
    n = 0
    while i <= 100:
        n = n+i**2
        print(n)
        i+=1

def eighteen():
    n = int(input("ingresa un numero: "))
    i = n
    c = n+100
    while n < c:
        n+=1
        i = i+n
    print(i)

def nineteen():

    e = 220
    d = 1.0906
    conv_e_d = round(e*d,2)
    print(conv_e_d)

def twenty():

    l = int(input("proporcione el ancho del rectangulo: "))
    h = int(input("proporcione la altura del rectangulo: "))
    a = h*l
    print("el area del rectangulo es:",a)

def twentyone():

    n1 = int(input("proporcione un numero: "))
    n2 = int(input("proporcione un numero: "))

    if n1 > n2:
        print(n1,"es mas grande que",n2)
    elif n2 > n1:
        print(n2,"es mas grande que",n1)
    else:
        print("debias ingresar dos numeros diferentes")

def twentytwo():

    n = int(input("ingresa un numero: "))
    i = n-1

    while i > 0:
        if i%2 == 1:
            print(i)
        i-=1
def twentythree():
    a = int(input("ingresa un numero: "))
    b = int(input("ingresa otro numero: "))
    r = a%b
    c = 0
    while r > 0:
        c = r
        r = a%b
        a = b
        b = r
    print(c)

def twentyfour():

    a = int(input())
    b = int(input())
    c = int(input())
    
    discr = b**2-(4*a*c)

    if discr > 0:
        print("hay dos soluciones diferentes")
        discr = discr**0.5
        sol_sum = (-b+discr)/(2*a)
        sol_res = (-b-discr)/(2*a)
        print("las dos soluciones son:",sol_sum,"y",sol_res)
    if discr == 0:
        print("hay una sola solucion")
    if discr < 0:
        print("no hay soluciones reales")

def twentyfive():

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n*factorial(n-1)
    factorial(5)

def twentysix():
    print("todo los numeros que vas a escribir deben ser positivos y diferentes entre si")
    a = int(input("escribe el primer numero: "))
    b = int(input("escribe el segundo numero: "))
    c = int(input("escribe el tercer numero: "))

    while a < 0 or b < 0 or c < 0 or a == b or c == b or a == c:
        print("recuerda que todos los numeros deben ser positivos y diferentes entre si")
        a = int(input("escribe el primer numero: "))
        b = int(input("escribe el segundo numero: "))
        c = int(input("escribe el tercer numero: "))

    if a > b and a > c:
        print(a,"es el mayor de todos")
        if b > c:
            print(c,"es el menor de todos")
        else:
            print(b,"es el menor de todos")
    if b > a and b > c:
        print(b,"es mayor de todos")
        if a > c:
            print(c,"es el menor de todos")
        else:
            print(a,"es el menor de todos")
    if c > a and c > b:
        print(c,"es el mayor de todos")
        if a > b:
            print(b,"es el menor de todos")
        else:
            print(a,"es el menor de todos")

def twentyseven():

    f = 0
    while f != 999:
        f = int(input("ingresa una temperatura en grados fahrenheit: "))
        c = round((5/9)*(f-32),2)
        print(f,"grados fahrenheit equivalen a",c,"grados celsius")

def twentyeight():
    return "no existe la estructura switch en Python"
def twentynine():
    #en sistemas Linux Ctrl+D finaliza los datos de entrada.
    try:
        while True:
            datos_de_entrada = input("ingresa informacion (Ctr+D para finalizar los datos de entrada): ")
            print("ingresaste como datos de entrada:",datos_de_entrada)
    except EOFError:
        print("Final de archivo alcanzado, no hay datos de entrada")
def thirty():
    #el codigo no puede aceptar números demasiado grandes
    n = 489990965341
    i = True
    while i == True:
        for i in range(2,int(n**0.5)+1):
            if n%i == 0:
                print(n,"no es primo")
                i = False
                break
        else:
            print(n,"es primo")
