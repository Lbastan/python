#a
#diferencia en %

max = 7
prom = 4
Min = 2.5
curso= 1.5

porcentaje1 = 100-curso/max*100
print(f'el curso es mas rapido que el maximo de los cursos', porcentaje1)

porcentaje2 = 100-curso/Min*100
print(f' el curso es mas rapido que el minimo  de los cursos ', porcentaje2)

porcentaje3 = 100-curso/prom*100
print(f'el curso es mas rapido que el promedio de los cursos', porcentaje3)

#b
mat_crudo_prom = 5
Mat_crudo_curso = 3.5

porc_inservible_prom= ((mat_crudo_prom-prom)/mat_crudo_prom)*100
porc_inservible_curso= ((Mat_crudo_curso-curso)/Mat_crudo_curso)*100
print(f'el material inservible del curso es de: ', porc_inservible_curso)
print(f'el material inservible del promedio de los cursos es de: ', porc_inservible_prom)

#C 
# ver 10 hs de este curso a cuanto equivale del resto.

horas= 10
equivalencia= prom/curso
total_de_horas= equivalencia*horas

print(f' si miro 10 hr de este curso, equivale a: ', total_de_horas, 'de los otros cusos')

total_de_horas2= (1/equivalencia)*horas
print(f' si miro 10 hr de otros cursos, equivale a: ', total_de_horas2, 'de este cuso')