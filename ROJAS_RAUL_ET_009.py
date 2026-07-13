#Diccionarios 

planes = {
'F001': ['Plan Básico', 'mensual', 1, False, False, 'libre'],
'F002': ['Plan Full', 'mensual', 1, True, True, 'libre'],
'F003': ['Plan Estudiante', 'trimestral', 3, False, True,
'tarde'],
'F004': ['Plan Senior', 'trimestral', 3, True, False, 'mañana'],
'F005': ['Plan Anual Pro', 'anual', 12, True, True, 'libre'],
'F006': ['Plan Nocturno', 'mensual', 1, False, True, 'noche'],

}

inscripciones = {
'F001': [14990, 30],
'F002': [22990, 10],
'F003': [39990, 0],
'F004': [35990, 6],
'F005': [159990, 2],
'F006': [18990, 15],
}

#Metodos

#Metodo menu principal
def menu_principal():
    print('========== MENÚ PRINCIPAL ==========')
    print('1. Cupos por tipo de plan')
    print('2. Búsqueda de planes por rango de precio')
    print('3. Actualizar precio de plan')
    print('4. Agregar plan')
    print('5. Eliminar plan')
    print('6. Salir')
    print('=====================================')

#Metodo 1 para validar opciones
def leer_opcion():
    while True:
        opcion = input('Ingrese una opcion (1-6):')
        if opcion.strip() == "":
            print('Error: la opcion ingresada no puede quedar vacía o solo contener solo espacios en blanco.')
        else:
            try:
                opcion = int(opcion)
                if opcion not in (1,2,3,4,5,6):
                    print('Error: Opcion no esta en el rango indicado.')
                else: 
                    return True
            except ValueError as e:
                print('Error: la Opcion no es valida')
                print('Detalle en:', e)
#Metodo 2
 
def cupos_tipo(tipo):
    tipo = input('Ingrese tipo de plan a consultar:')
    if tipo == "":
        print('Error: el plan no puede ser quedar vacío.')
    elif tipo.strip() == "":
        print('Error: el plan no puede ser solo espacios en blanco,')
    elif tipo in ('mensual','MENSUAL'):
        print(f'El total de cupos disponibles es: {inscripciones}[1]')
    elif tipo in ('anual','ANUAL'):
        print(print(f'El total de cupos disponibles es: {inscripciones}[1]'))
    elif tipo in ('trimestral','TRIMESTRAL'):
         print(print(f'El total de cupos disponibles es: {inscripciones}[1]'))

#Metodo 3
def busqueda_precio(p_min, p_max):
    while True:
        p_min = input('Ingrese el precio minimo')
        p_max = input('Ingrese el precio maximo')

        if p_min == "" or p_max == "":
            print('El precio no puede quedar vacío.')
        elif p_min.strip() == "" or p_max.strip() == "":
            print('El precio no puede ser solo espacios en blanco.')
        else:
            try:
                p_min = float(p_min)
                p_max = float(p_max)
                
                if p_min < 0 or p_max < 0:
                    print('El precio no puede ser 0')
                if p_min > p_max:
                    print('El precio minimo no puede ser mayor que el precio maximo.')
                    return True
            except ValueError as e:
                print('Error: Debe ingresar valores enteros')
                print('Detalle en:', e)
#Metodo 4
def buscar_codigo(codigo):
    codigo = ""
    while True:
        codigo = input('Ingrese el codigo del plan:')
        if codigo == "":
            print('El codigo no puede quedar vacío.')
        if codigo.strip() == "":
            print('El codigo no puede ser solo espacios en blanco')
        elif codigo not in inscripciones:
            print(f'El codigo {codigo} no existe.')
        else: 
            print(f'Los planes encontrados son: {planes}')
            return True,planes
#Metodo 5
def actualizar_precio(codigo, nuevo_precio):
    buscar_codigo = False
    buscar_codigo,codigo = buscar_codigo()
    if buscar_codigo == False:
        return False, codigo
    else:
        while True:
            print(f'Desea Actualizar el precio del plan: {planes}?(s/n)')
            if input().lower() == 's':
                nuevo_precio = input(f'Ingrese el precio nuevo del plan{planes}')
            if nuevo_precio == "":
                print ('El precio no puede quedar vacío.')
            if nuevo_precio.strip == "":
                print('El precio no puede ser solo espacios en blanco.')
            else:
                try:
                    nuevo_precio = int(nuevo_precio)
                    if nuevo_precio <= 0:
                        print('El nuevo precio no puede ser negativo o igual a cero.')
                        inscripciones[codigo][0] = int(nuevo_precio)
                        print(f'El precio de {planes} se ha actualizado a {inscripciones[codigo][0]}\n')
                        return True
                except ValueError as e:
                                print('Error: Debe ingresar valores enteros')
                                print('Detalle en:', e)
#Metodo 6
def eliminar_plan(codigo):
    bool_codigo = buscar_codigo()
    if bool_codigo:
        if bool_codigo in {planes[inscripciones]}:
            print(f'El plan:{codigo} ha sido eliminado.')
            return True
        else:
            print(f'El plan: {codigo} no existe.')
            return False


#Metodo 7
def validar_codigo(codigo_nuevo):
    if codigo_nuevo == "":
        print('El codigo no puede quedar vacío.')
    if codigo_nuevo.strip() == "":
        print('El codigo no puede ser solo espacios en blanco.')
    elif codigo_nuevo in planes:
        print('El codigo ya ha sido registrado.')
    else:
        return True
#Metodo 8
def validar_nombre(nombre_nuevo):
    if nombre_nuevo == "":
        print('El nombre del plan no puede quedar vacío')
    if nombre_nuevo.strip() == "":
        print('El nombre del plan no puede ser solo espacios en blanco.')
    else:
        return True
#Metodo 9
def validar_tipo(tipo_nuevo):
    if tipo_nuevo not in ('mensual','trimestral', 'anual'):
        print('El tipo ingresado no corresponde a ninguno disponible.')
    else:
        return True
#Metodo 10
def validar_duracion(nueva_duracion):
    if nueva_duracion < 0:
        print('La duración debe ser mayor a cero.')
    else:
        return True
#Metodo 11
def validar_nuevo_acceso_piscina(nuevo_acceso_piscina):
    if nuevo_acceso_piscina == 's':
        return True
    if nuevo_acceso_piscina == 'n':
        return False
#Metodo 12
def validar_nueva_incluye_clases(nueva_incluye_clases):
    if nueva_incluye_clases == 's':
        return True
    if nueva_incluye_clases == 'n':
        return False
#Metodo 13
def validar_nuevo_horario(nuevo_horario):
    if nuevo_horario == "":
        print('El horario no puede quedar vacío')    
    if nuevo_horario.strip():
        print('El horario no puede ser solo espacios en blanco.')
    else:
        return True
#Metodo 14
def validar_nuevo_precio(nuevo_precio):
    if nuevo_precio < 0:
        print('El nuevo precio debe ser mayor a cero.')
    else: 
        return True
#Metodo 15
def validar_nuevos_cupos(nuevos_cupos):
    if nuevos_cupos < 0:
        print('El cupo debe ser mayor o igual a cero.')
    else:
        return True



#Metodo 16
def agregar_plan(codigo, nombre, tipo, duracion, acceso_piscina, incluye_clases,horario, precio, cupos):
    codigo = input('Ingrese el codigo del nuevo plan:')
    nombre = input('Ingrese el nombre del plan:')
    tipo = input('Ingrese el tipo de plan:')
    duracion = input('Ingrese la duracion del plan (meses)')
    acceso_piscina = input('¿Incluye acceso a piscina? (s/n):')
    incluye_clases = input('¿Incluye clases grupales? (s/n):')
    horario = input('Ingrese horario:')
    precio = input('Ingrese precio:')
    cupos = input ('Ingrese cupos:')

    bool_codigo = validar_codigo(codigo)
    bool_nombre = validar_nombre(nombre)
    bool_tipo = validar_tipo(tipo)
    bool_duracion = validar_duracion(duracion)
    bool_acceso_piscina = validar_nuevo_acceso_piscina(acceso_piscina)
    bool_incluye_clases = validar_nueva_incluye_clases(incluye_clases)
    bool_horario = validar_nuevo_horario(horario)
    bool_precio = validar_nuevo_precio(precio)
    bool_cupos = validar_nuevos_cupos(cupos)

    if bool_codigo and bool_nombre and bool_tipo and bool_duracion and bool_acceso_piscina and bool_incluye_clases and bool_horario and bool_precio and bool_cupos:
        if codigo in planes:
            print('El codigo ya eta registrado.')
    else: 
        print('Se ha registrdo con exito el plan.')

#Metodo 17 
def main():
    while True:
        menu_principal()
        opcion = leer_opcion()
        if opcion == 1:
            cupos_tipo()
        elif opcion == 2:
            buscar_codigo()
        elif opcion == 3:
            actualizar_precio()
        elif opcion == 4:
            actualizar_precio()
        elif opcion == 5:
            eliminar_plan()
        elif opcion == 6:
            print('Programa finalizado, Muchas graias por usar el sistema FitPass.')  
            exit(0)
        else:
            print('Seleccione una opcion válida.')
#Llamado a Main
main()








