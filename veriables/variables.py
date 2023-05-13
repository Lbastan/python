numero = 10
numero += 2
print(numero)
nombre = 35
bienvenida = f"hola {nombre} como estas?" # la f concatena y pasa a texto cualquier dato.
print(bienvenida)
# del: operador que elimina datos de la memoria.
del nombre #aparece igual porque se elimino despues de que definiera bienvenida.

print("Hola" in bienvenida) #false porque esta H.
print("hola" in bienvenida) #true. 
# lo mismo para "not in"