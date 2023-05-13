cadena1= "hola, buen dia"
cadena2= "todo bien?"

#estructura --> dato.metodo
resultado= cadena1.upper() #mayurculas
resultado2= cadena1.lower() #minusculas
resultado3= cadena1.capitalize() #primera letra a mayus

# buscamos una cadena en otra cadena, te devuelve solo la prime ubicacion. Devuelve -1 cuando no encuentra.
resultado4= cadena1.find("a") 
# buscamos una cadena en otra cadena, te devuelve solo la prime ubicacion. Devuelve un excepcion cuando no encuentra.
resultado5= cadena1.index("a")

resultado6= cadena1.isnumeric() #devuelve true o false, si es un dato numerico, aunque los numero sean en tipo texto
resultado7= cadena1.isalpha() #devuelve true o false, si tiene caracteres especuales tira false, como comas o espacios
resultado8= cadena1.count("a") #devuelve cantidad de coincidencias.

#len es una funcion, por eso cadena1 entre los () , devuelve cuantos caracteres hay. con espacios incluidos.
resultado9= len(cadena1) 


resultado10= cadena1.startswith("h") #devuelve true o false, verifica con que empieza la cadena.
resultado11= cadena1.endswith("a") #devuelve true o false, verifica con que termina la cadena.

#reemplaza un pedazo de la cadena por una nueva pero no definitivamente. puedo reemplazar "," por espacios.
resultado12= cadena1.replace("la","lu")
print(resultado12)
print(cadena1)

#separar cadenas con la cadena que le pasemos
resultado13= cadena1.split(",") #devuelve una lista, los datos son los separados por comas.
print(resultado13)

