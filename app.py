import pandas as pd
import os
#Importar todas las funciones necesarias de los otros modulos
from analisis import analizar_ventas
from datos import guardar_csv, ingresar_ventas, cargar_ventas

#lista que funcionara como base de datos en memoria
VENTAS_DATA = []

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    global VENTAS_DATA
    while True:
        #cada vez que se muestre el menu, limpiar la pantalla
        limpiar_pantalla()
        print('\n--Menú de Gestión de Ventas--')
        print('1. Ingresar nueva venta')
        print('2. Analisis de ventas')
        print('3. Cargar ventas desde archivo')
        print('4. Salir')
        opcion = input('Seleccione una opción: ')   
        if opcion == '1':
            ingresar_ventas(VENTAS_DATA)    
        elif opcion == '2':
            analizar_ventas(VENTAS_DATA)    
        elif opcion == '3':
            VENTAS_DATA = cargar_ventas()
        elif opcion == '4':
            print('Saliendo del sistema...')
            break
        else:
            print('Opción no válida. Por favor, intente de nuevo.')
        
        input("Presione Enter para continuar...")
        
        


guardar_csv(VENTAS_DATA)


if __name__ == "__main__":

    print("Bienvenido al Sistema de Gestión de Ventas!")
    VENTAS_DATA = cargar_ventas()
    #ingresar_ventas(VENTAS_DATA)
    menu()
    