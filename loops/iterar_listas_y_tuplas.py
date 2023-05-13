#con tuplas funciona igual.

animales= ["gato","perro","loro","cocodrilo","pez"]
numeros= [41,3,6,78,9]
#for animal in animales:
    #print(f'el animal es: {animal}')

for numero,animal in zip(animales,numeros):
    print(f"recorriendo lista 1: {numero}")
    print(f"recorriendo lista 2: {animal}")
    
for num in range(9):
    print(num)
    
#recoriendo lista con su indice
for num in enumerate(numeros):
    indice= num[0]
    valor= num[1]
    print(type(num))
    print(num)
    print(f"el indice es: {indice} y el valor es: {valor}")
    
#usando el else, se muestra al final y al terminar el bucle
for numero in numeros:
    print(f"ejecutando el ultimo bucle: {numero}")
else:
    print("bucle termino")
    