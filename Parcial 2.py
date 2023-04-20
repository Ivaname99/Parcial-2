#Inicio del programa
print('*^*^*^*^*^*^*^*^*^*^*^*^*^')
print('*^Bienvenido al programa*^')
print('*^*^*^*^*^*^*^*^*^*^*^*^*^\n')

print("""En este programa debera ingresar un numero entero(N) y se le regresara el resultado de la suma
1 + (1/2) + (1/3)...+ (1/N)\n""")
x = 1
suma = 0

#Obtencion de datos del usuario
while x:
    try:
        num = int(input('Ingrese un numero -> '))
        break

    except ValueError:
        print("Ese no es un numero\n")
        continue

#Procesando el resultado
for i in range(num):
    suma += 1/x
    x += 1

#Imprimiendo el resultado
print(round(suma,2))

#Cierre del programa
print('\nFin del programa')