#DIR TE DICE QUE HACER CON UNA LISTA, O CADENA, O TUPLAS....
#DIR()

lista= list(["hola","como andas?",29,"14 de nov"])

resultado= len(lista) #cuenta los elementos de la lista
print(resultado)

resultado1= lista.append("luchibastan@gmail") #agrega elementos a la lista
print(lista)

resultado2= lista.insert(1, "!!") #agrega un elemento en una ubicacion especifica
print(lista)

resultado3= lista.extend(["False", 2023]) #agrega varios elementos a la lista, tiene que ingresarse como una lista, con []
print(lista)
print(len(lista))

resultado4= lista.pop(1) #elimina un elemento x su ubicacion.
#si escribe -1 se elimina el ultimo elemento de la lista, si escribo -2 elimina el anteultimo....
print(len(lista))

resultado5= lista.remove(29) #elimina un elemento x su valor.
print(lista)

#resultado6=lista.clear #elimina toda la lista

#ordena todos los elementos de manera ascendente pero solo los numericos.
#ordena, true, false, y numeros de menor a mayor
#resultado7=lista.sort() 
#lista.sort(reverse=True) los ordena al reves.

resultado8= lista.reverse() # te da vuelta la lista, el sort anterior te lo ordenaria 
print(lista)

resultado9= lista.index("14 de nov") #busca el elemento exacto, si buscara 14 no lo encuentra.
print(resultado9)