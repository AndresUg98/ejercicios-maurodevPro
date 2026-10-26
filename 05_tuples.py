#Son los mismo que una lista, pero las tuplas son inmutables
#Osea que no se pueden modificar una vez creadas.
#Es ideal para datos que no deberian de cambiar a lo largo de programa
#Usualmente se usan para dar mas seguriad

'''
my_tuple = tuple()
my_other_tuple = (60,30,50,60,50,10)


my_tuple = (35,1.77, "Andres", "Ugarte","zoroak")
print(my_tuple)
print(type(my_tuple))

#Si podemos juntar tuplas dentro de una NUEVA tupla
sum_tuple = my_tuple + my_other_tuple

print(sum_tuple)

print(sum_tuple[3:6])

#Convertir una tupla a una lista
my_tuple = list(my_tuple)
print(type(my_tuple))

#Editando el indice 4
my_tuple[4] = "añiñi"
print(my_tuple)

#Insertando info
my_tuple.insert(1,"Azul")
print(my_tuple)

#Convirtiendo de nuevo a tupla
my_tuple = tuple(my_tuple)
print(type(my_tuple))

#Borrando toda la tupla
del my_tuple
'''

# 1. Crea una tupla con los valores (10, 20, 30, 40, 50) e imprÃ­mela.

my_tuple2 = (10, 20, 30, 40, 50)
print(my_tuple2)

# 2. Accede al segundo elemento de la tupla (100, 200, 300, 400, 500) 
# y muÃ©stralo.

print(my_tuple2[1])

# 3. Intenta modificar el primer elemento de la tupla (1, 2, 3) a 10 y 
# observa el resultado.
my_tuple3 = (1, 2, 3)
#my_tuple3[0] = 10
print(my_tuple3)#Esto da error, por que las tuplas no se pueden modificar


# 4. Cuenta cuÃ¡ntas veces aparece el nÃºmero 3 en la tupla
#  (1, 2, 3, 3, 4, 5, 3).

my_tuple4 = (1, 2, 3, 3, 4, 5, 3)
print(my_tuple4.count(3))

# 5. Encuentra el Ã­ndice de la primera apariciÃ³n de la cadena "Python" 
# en la tupla ("Java", "Python", "JavaScript", "Python").

tuple_text = ("Java", "Python", "JavaScript", "Python")
print(tuple_text.index("Python"))

# 6. Concatena dos tuplas: (1, 2, 3) y (4, 5, 6) e imprime
#  la tupla resultante.

first_tuple = (1, 2, 3)
second_tuple =  (4, 5, 6)
mix_tuple = first_tuple + second_tuple
print(mix_tuple)

# 7. Crea una subtupla con los elementos desde la posiciÃ³n 2 
# hasta la 4 (sin incluir la 4) de la tupla (10, 20, 30, 40, 50).

print(my_tuple2[2:4])

# 8. Convierte la tupla ("rojo", "verde", "azul") en una lista, 
# cambia el segundo elemento a "amarillo" y vuelve a convertirla en 
# una tupla. Imprime la tupla resultante.

color_tuple = ("rojo", "verde", "azul")
color_tuple = list(color_tuple)
color_tuple[1] = "Amarillo"
color_tuple = tuple(color_tuple)
print(color_tuple)
# 9. Elimina una tupla llamada my_tuple usando del y luego intenta 
# imprimirla para ver el resultado.

#del my_tuple2
print(my_tuple2) #da error por que ya no existe la tupla

# 10. Crea una tupla con un solo elemento (el nÃºmero 100) e imprÃ­mela. 
# AsegÃºrate de usar la sintaxis correcta para crear una tupla con un solo 
# elemento.

one_element_tuple = (100,) #Si no ponemos la coma, lo toma como si fuera un int 
#y no una tupla
print(one_element_tuple)