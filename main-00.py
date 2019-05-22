# Imprimir un texto
print("Hello world")

# Variable de texto
text = "Hello world"
print(text)

# Variable numérica
num = 3
print(num)

# Concatenación
name = "John"
print("Hello " + name)

# String + Integer
#print("Hello " + num)
print("Hello " + str(num))

# Variable múltiple (arreglo/vector)
list = [1,1,2,3,5,8,13]
print("list[3]: " + str(list[3]))

# Si <condición>: <sentencias> else: <sentencias>
if num == 3:
    print("Es un 3")
else:
    print("No es un 3")

num = 4

# Si <condición>: <sentencias> else: <sentencias>
if num != 3:
    print("No es un 3")
else:
    print("Es un 3")

# Or
if (num == 3 or num == 5):
    print("El número es tres o cinco")

# And
if (num >= 1 and num <= 3):
    print("El número está entre 1 y 3")

# for <variable> in <arreglo>: <sentencias>
for value in list:
    print(value)

# while <condición>: <sentencias>
suma = 0
i = 0
while suma < 10:
    suma += list[i]
    print("+", list[i], "=", suma)
    i += 1