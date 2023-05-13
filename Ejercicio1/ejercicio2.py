#a

palabras=2
segundos= 1
equivalencia= palabras/segundos
frase= input("decime una frase: ")
cantidad_de_palabras=frase.count(" ")+1
print(f'la cantidad de palabras de la frase es: ',cantidad_de_palabras)
tiempo= cantidad_de_palabras/equivalencia
print(f'el tiempo que tarda en decirlo es de : ', tiempo, 'segundos')

# b
if tiempo > 60:
 print("Me parece que estas hablando mucho")

#c
persona1= 0.7
tiempo_persona1= tiempo*persona1
print(f'Esta persona tarda en decir la misma frase: ', tiempo_persona1, 'segundos')