#Un set es muy parecido a una lista, pero con la pecurialidad de que los datos
#No se deben/pueden repetir y no se pueden ordenar

my_set = set()
my_other_set = {"Andres", "Ugarte", 28}

my_other_set.add("Andres")

print(my_other_set) #un set no admite repetidos

#Verificando si un elemento existe en un set
print("Andres" in my_other_set) #true