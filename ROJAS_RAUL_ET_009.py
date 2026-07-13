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
        opcion = input('Ingrese una opcion (1-6)')
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
def 








