#creando diccionarios
diccionario= dict(nombre="luisina",apellido="Bastan Garcia",edad=29)
print(diccionario)


diccionario2=dict.fromkeys(["nombre","apellido","edad"])
diccionario3=dict.fromkeys("nombre","apellido")
diccionario4=dict.fromkeys(["nombre","apellido"],"nose")

print(diccionario2)
print(diccionario3)
print(diccionario4)