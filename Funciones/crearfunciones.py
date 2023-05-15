#creando una funciòn simple
#crear una funcion que tenga parametros
def Universidad(nombre,sitacion):
    sitacion = sitacion.lower()
    if (sitacion == "egresado"):
        adjetivo = "felicitaciones por terminar tu carrera"
    elif (sitacion == "estudiante"):
        adjetivo = "ya queda poco!"
    elif (sitacion == "ingresante"):
        adjetivo = "bienvenido"    
    else:
        adjetivo = '¿ya viste los cursos que ofrecemos?'
    print(f"Hola {nombre}, ¿Como andas? {adjetivo} ")
    
    
Universidad("Camila","egresado")
Universidad("Lucas","estudiante")
Universidad("Fran","ingresante")
Universidad("Luisina","sin saber que hacer")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
    return contraseña,num
    
#desempaquetando la funciòn
password,primer_numero = crear_contraseña_random(981)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_numero}")