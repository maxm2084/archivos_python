# CODE:39
# Archivos [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 3.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con archivos

import csv

# Objetivo:
# Leer y trabajar con un archivo CSV complejo y el
# manejo de excepciones

def desafio(ambientes):
    print('Ejercicios con archivos CSV complejos')
    archivo = open('propiedades.csv')

    # Realice un programa que abra el archivo CSV "propiedades.csv"
    # en modo lectura. Recorrer dicho archivo y contar
    # la cantidad de departamentos de 2 ambientes y la cantidad
    # de departamentos de 3 ambientes disponibles.
    # Al finalizar el proceso, imprima en pantalla los resultados.
    
    # Según el valor ingresado en "ambientes" está función deberá
    # retornar (return):
    # 1) si ambientes == "2_ambientes"
    #  ---> retornar la cantidad encontrada de departamentos de 2 ambientes
    # 2) si ambientes == "3_ambientes"
    #  ---> retornar la cantidad encontrada de departamentos de 3 ambientes

    # Tener cuidado que hay departamentos que no tienen definidos
    # la cantidad de ambientes, verifique el texto no esté vacio
    # antes de convertirlo a entero con "int( .. )"
    # Puede evitar que el programa explote utilizando "try except".

    # Comenzar aquí, recuerde el identado dentro de esta funcion
    
    listado = list(csv.DictReader(archivo))
    
    
    ambientes_2 = 0
    ambientes_3 = 0

    for i, k in listado:
        if ambientes == "2_ambientes":
            row = listado[k]
        try:
            ambientes = int(row['ambiente'])
            print('Fila', k, 'dato ambientes:', ambientes)
        except:
            print('Error Fila', k, 'dato cantidad ambientes faltante')
            ambientes_2 += k
            return ambientes_2
        else:
            ambientes_3 += k
        return ambientes_3
    archivo.close()

if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    desafio("2_ambientes")
