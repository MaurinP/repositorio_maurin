# repositorio_maurin

Explicación de códigos; evidencias.

Explicación códigos, tarea 1.

def one():#el numero de la funcion es el numero del ejercicio
    print("hola")

Explicación: def es una forma de declarar una función. En este caso la función se llama one(). Y se llama "one" porque es el primer ejercicio. El nombre de las funciones estando en inglés fue por mero capricho perosnal, nada importante en qué pensar. En Python 3 se usa print para imprimir datos de salida. En este caso se imprime "hola", una cadena de texto. 

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
    
Explicación de estos 5 ejercicios: Es la misma lógica del primero, pero imprimiendo números en lugar de cadenas de texto. No hace falta declarar los números en variables para poder operarlos. 

def eight():
    i = 1
    while i <= 3:
        print(i)
        i+=1
Explicación ejercicio 8: i = 1 es el contador del bucle, además del número que se imprimirá por pantalla. Inicia en 1, porque el ejercicio trata acerca de imprimir números del 1 al 3. Mientras i sea menor o igual a 3, se imprimirá i en cada vuelta del bucle. Al finalizar una vuelta, i aumenta 1 (por eso aparece i+=1).

def nine():
    for i in range(1,10):
        print(i)
Explicación del ejercicio 9: Aquí usa un bucle for e lugar de un while. No hay necesidadde declrarar un contador explícitamente. El bucle imprimirá todos los números que están en el rango de 1 a 9. "range(1,10)" es todos los números iguales o mayores a 1 pero menores a 10. Si quisiéramos imprimir hasta los números de 1 a 10, deberíamos poner range(1,11).

def ten():
    i = 1
    while i <= 10000:
        print(i)
        i+=1
Explicación del ejercicio 10: Misma lógica del ejercicio 8, pero en lugar de imprimir números menores o iguales a 3, imprime números menores o iguales a 10000 empezando desde 1.

def eleven():
    for i in range(5,11):
        print(i)
Explicación del ejercicio 11: Misma lógica del ejercicio 9, pero imprime los números del 5 al 10, por eso es "range(5,11)".

def twelve():
    j = 5
    while j <= 15:
        print(j)
        j+=1
Explicación del ejercicio 12: Misma lógica del ejercicio 8, pero aquí el contador empieza en 5, y el bucle acaba cuando j es igual a 15.

def thirteen():
    for i in range(5,15001):
        print(i)
Explicación del ejercicio 13: Misma lógica del ejercicio 9, pero el range es entre 5 y 150001, para que imprima los números entre 5 y 15000.

def fourteen():
    for i in range(1,201):
        print("hola")
Explicación del ejercicio 14:El rango de números que hay entre range(1,201) es 200. En lugar de imprimir el número en cada vuelta, imprimimos "hola".

def fifteen():
    n = 1
    while n <= 30:
        print(n**2)
        n+=1
Explicación del ejercicio 15:En cada vuelta de bucle (que son 30), se imprime el cuadrado del contador (o sea, el cuadrado de cada número entre 1 y 30).

def sixteen():
    n = 1
    c = n
    while n < 5:
        c = c*(n+1)
        n = n + 1
        print(c)
Explicación del ejercicio 16: Es el factorial de 5 (5!). El resultado debe ser 120. Se requieren de dos variables, una que lleve el conteo de los números que se van multiplicando (c) y otra que almacene el nuevo número que se añadirá a la multiplicación (n).
C es igual a n, porque la multiplicación inicia en 1. Se multiplicará 1*2 primero, por eso se multiplica a c (1) por n+1 (2), y el resultado queda almacenado en c. Ahora c es 2 y n es igual a n+1, luego se hace el mismo proceso hasta que n sea igual a 5 y c haya acumulado el producto 1x2x3x4x5.

def seventeen():
    i = 1
    n = 0
    while i <= 100:
        n = n+i**2
        i+=1
    print(n)
Explicación del ejercicio 17: habría sido sencillo usar una fórmula, pero con el bucle se ejemplifica mejor el funcionamiento de los bucles. "n" es una variable inicializada en cero, porque contendrá la suma del cuadrado de todos los números entre 1 y 100 (por eso i es inicializado en 1, porque, deacuerdo a algunos textos, es el primer natural). "n" suma su propio valor al del nuevo cuadrado. De esa manera "n" está acumulando la suma del cuadrado de cada nuevo número con los anteriores. 

def eighteen():
    n = int(input("ingresa un numero: "))
    i = n
    c = n+100
    while n < c:
        n+=1
        i = i+n
    print(i)
Explicación del ejercicio 18:La lógica es la misma del anterior. "i" es la variable en donde se deposita el número escrito por el usuario, i es igual a n, porque para que el bucle funcione necesitamos una variable con el valor de n a la que se le puedan añadir todos los nuevos números, sumando también el depositado por el usuario. Si i no existe, el bucle podría volverse interminable si simplemente n = n+n, ya que n se modificaría con cada vuelta, y c sería un valor diferente en cada vuelta. No podemos almacenar suma en n, se necesita en otro lado, por eso existe i. Entonces, mientras n sea menor a c (c es n, pero más 100), i irá almacenando la suma de todos esos números entre n y c.

def nineteen():

    e = 220
    d = 1.0906
    conv_e_d = round(e*d,2)
    print(conv_e_d)
Explicación ejercicio 19: La conversión de euros a dólares es fácil. Un euro son 1.0906 dólares (al menos lo era el día que hice el ejercicio). Solo es cuestión de hacer una multiplicación. Por ejemplo,2 euros son aproximadamente 2.18 dólares, simplemente multiplicamos la cantidad de euros por lo que vale un dólar. Y la función "round" es para redondear. Multipliqué los euros por dólares, y con eso obtenemos la conversión, además lo he redondeado a 2 decimales.

def twenty():

    l = int(input("proporcione el ancho del rectangulo: "))
    h = int(input("proporcione la altura del rectangulo: "))
    a = h*l
    print("el area del rectangulo es:",a)
Explicación ejercicio 20: La fórmula para encontrar el área de un rectángulo es multiplicar el ancho por el largo, esto es simplemente multiplicar una variable "l" que represente un lado y una variale "h" que represente el otro. El resultado se almacena en una varaible diferente y luego se imprime por pantalla.

def twentyone():

    n1 = int(input("proporcione un numero: "))
    n2 = int(input("proporcione un numero: "))

    if n1 > n2:
        print(n1,"es mas grande que",n2)
    elif n2 > n1:
        print(n2,"es mas grande que",n1)
    else:
        print("debias ingresar dos numeros diferentes")
Explicación del ejercicio 21: Para encontrar cuál es el más grande entre dos números basta con compararlos, si un número no es más grande, entonces el otro debe serlo, aunque puede existir el caso de que sean iguales. Por eso hay tres casos. Si un número no es más grande al otro, hay que comparar si el otro si es más grande, y si ninguna de las anteriores es verdad, entonces son iguales.

def twentytwo():

    n = int(input("ingresa un numero: "))
    i = n-1

    while i > 0:
        if i%2 == 1:
            print(i)
        i-=1
Explicación del ejercicio 22: Para buscar los números pares menores a un determinado número hay que recorrer desde el número hasta 1 basta con crear un bucle decreciente, en donde en cada vuelta el contador se disminuya 1, y que el número que muestra el contador sea verificado a través de la operación módulo (si el módulo entre ese número es dos, entonces es par, porque por ley todo número par es divisible entre dos).

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
Explicación del ejercicio 23: ChatGPT me explicó que no era necesario que c existiera, y me di cuenta de eso, pero preferí dejarlo así, una muestra de error humano que después puede ser corregido. Mientras el residuo entre dos números sea mayor a 0, entonces ambos números se pueden seguir dividiendo. Pero el orden debe cambiar a medida de que el programa avanza. a = b, para que se pueda hallar el máximo divisor común entre los dos. Y b = r, r es igual al residuo, para poder seguir consiguiendo números cada vez más pequeños y así lograr conseguir el número maś pequeño por el que se pueda dividir a los dos números originales.

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
Explicación ejercicio 23: para conseguir las soluciones a una ecuación cuadrática basta aplicar la fórmula general de las ecuaciones cuadráticas desarrollada por Galois. Y para saber si tiene soluciones, basta con fijarse en la raíz cuadrada que hace parte de dicha fórmula. A eso se le llama discriminante (por eso la variable se llama así), si el discriminante da un número negativo, no hay soluciones, ya que daría una raíz cuadrada no real. Si el discriminante es 0, solo una solución. Si el discriminante es mayor a cero, entonces hay dos soluciones diferentes.

def twentyfive():

    def factorial(n):
        if n == 1:
            return 1
        else:
            return n*factorial(n-1)
    factorial(5)

Explicación del ejercicio 25: La función factorial se llama a sí misma hasta que el valor que se pasa a sí misma cada vez que se llama sea 1, de ese modo la recursión termina y debe devolver el valor de la multiplicación entre todos los valores de todas las recursiones hechas. Además, en este caso la función TIENE un valor (valor que solo existe por el return 1 del primer if que aparece una vez n es igual a 1), por eso se puede multiplicar.

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

Explicación del ejercicio 25: el int(input()) es para recibir únicamente números, o que todo lo que reciba sea convertido a número, puede verse de ambas maneras. El while del principio dicta que si los números no son diferentes entre sí, es decir que si al menos dos de ellos son iguales, el usuario deberá digitarlos de nuevo hasta que todos sean diferentes. Luego sigue determinar cuál es mayor. Dado que debe haber uno solo que sea más grande aplico la siguiente regla: uno de todos debe ser mayor DEBE ser más grande a los otros dos, por eso existen "if a > b and a > c", porque necesariamente algo así debe pasar. Luego comparo a los dos que quedan, si un número x no es más grande que y, pero tenemos certeza de que alguno de los dos es más grande, entonces y es más grande que x. Eso mismo aplico luego de encontrar cuál es el maś grande de todos.

def twentyseven():

    f = 0
    while f != 999:
        f = int(input("ingresa una temperatura en grados fahrenheit: "))
        c = round((5/9)*(f-32),2)
        print(f,"grados fahrenheit equivalen a",c,"grados celsius")
Explicación del ejercicio 27: Aplico la fórmula de conversión de fahrenheit a celsius, y el programa continúa mientras los grados fahrenheit dados por teclado sean diferentes a 999.


def twentyeight():
    return "no existe la estructura switch en Python"
Explicación del ejercicio 28: La explicación del programa es bastante explícita, creo yo.

def twentynine():
    try:
        while True:
            datos_de_entrada = input("ingresa informacion (Ctr+D para finalizar los datos de entrada): ")
            print("ingresaste como datos de entrada:",datos_de_entrada)
    except EOFError:
        print("Final de archivo alcanzado, no hay datos de entrada")
Explicación del ejercicio 29: try-except es un forma de manejar errores. Normalente presionar Ctl+D y salirse del programa sin llenar los datos que se piden por teclado son una forma de error en Python, pero se puede manejar. La lógica de try-except es: en caso de que se intente un programa, pero haya cierto tipo de fallo, entonces se pueden manejar unas opciones. En este caso la opción al Ctrl+D es notificar que se alcanzado el final de los datos de entrada (sé que escribí archivo, me confundí cuando escribía el programa, pero lo voy a dejar así).

def thirty():

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
Explicación del ejercicio 30: Hay un algoritmo que consiste en conseguir dividir a todos los números menores o iguales a la raíz cuadrada de un número, si alguno de esos números logra dividir al número, entonces no es primo. n representa el número introducido, el que queremos saber si es primo, i es para que el bucle while se ejecute hasta que algún número logre dividir a n, si es el caso, entonces el bucle se detiene. El bucle for lo que es hace es recorrer los números entre 2 y la raíz cuadrada de n, y dividiendo sistemáticamente a n por cada uno de esos números, si el bucle termina sin problemas y sin cambiar a i de True a False, es porque el número es primo. 
