lista = ["luisina","bastan garcia","29 años",2914310227,"luchibastan@gmail.com",True]
print(lista)
print(lista[3]) #comienza a contar desde la posicion 0, para acceder a elementos de la lista
tupla = ("luisina","bastan garcia","29 años",2914310227,"luchibastan@gmail.com",True) # la tubla no se puede modificar, las listas si.
#esto es valido
lista[3]="maquinola"
#esto no
#tupla[3]="maquinola"

#creando un set
conjunto ={"luisina","bastan garcia","29 años",2914310227,"luchibastan@gmail.com",True}
print(conjunto) # no puedo repetir valores en el conjunto, y no tiene indice. son datos desordenados.

diccionario = {
    "nombre": "luisina",
    "apellido": "bastan garcia",
    "edad": "29 años",
    "telefono": 2914310227,
    "mail":"luchibastan@gmail.com",
    "nose": True
}
print(diccionario["nombre"])
