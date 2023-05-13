diccionario = {
    "nombre" : "luisina",
    "apellido" : "bastan garcia",
    "subs" : 163004
}

claves= diccionario.keys() #devuelve las claves. 
print(claves)

nombre= diccionario.get("apellido") #devuelve el contenido de la clave que ponga, no me lanza una excepcion. 
print(nombre)

#elimina= diccionario.clear() #eliminaTODO del diccionario
elimina2= diccionario.pop("nombre") #si quiero eliminar varios, separo con coma.
print(diccionario)

#diccionarioiterable