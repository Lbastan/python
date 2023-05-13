conjunto= set(["dato2","dato1","dato3"])

#las tuplas pueden ir dentro de las listas, listas en listas no y diccionarios tampoco.

conjunto2={"dato20","dato1"}
conjunto3=frozenset(["dato1","dato2"]) #() y []

conjunto4={conjunto3,"dato3"}

print(conjunto4) #te ordena los datos de frozenset

#teoria de conjuntos

conjunto1={1,3,5,7}
conjunto2={1,3,7}

#verificando si es subconjunto
resultado=conjunto2.issubset(conjunto1)
resultado=conjunto2 <= conjunto1 #es lo mismo que issubset

#verificando si es superconjunto
resultado2=conjunto1.issuperset(conjunto2)
resultado2=conjunto1 >= conjunto2 #es lo mismo que issubset

print(resultado2)

conjunto5={2,4,6,8}

#indisjoint te dice que todos los elementos de los conjuntos son diferentes entre si
resultado3=conjunto1.isdisjoint(conjunto5) 
print(resultado3)