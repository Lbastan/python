diccionario= {
    "nombre": "luisina",
    "apellido": "bastan garcia",
    "edad": 29
}

for datos in diccionario.items():
    key= datos[0]
    value= datos[1]
    print(f"la clave es {key} y el valor es {value}")
    
frutas = ["banana", "manzana", "granada", "naranja", "pera", "ciruela"]

for fruta in frutas:
    if fruta == "granada":
        continue #saltea el loop y sigue con el siguiente
    print(f"me voy a comer una: {fruta}")
    
for fruta in frutas:
    if fruta == "granada":
        continue #saltea el loop y sigue con el siguiente
    if fruta == "pera":
        print(f"me duele la panza por la pera")
        break #termina el loop
    print(f"me voy a comer una: {fruta}")
    
numeros2=[2,6,8,34]
numeros_duplicados=[x*2 for x in numeros2] #itero en una sola linea de codigo
print(numeros_duplicados)

