#Se crea una lista vacia que almacenara las compras realizadas por el usuario
compras_realizadas = []
#Se declara una variable inicializada en 0 para el total gastado
total_gastado = 0

#Se define la funcion para agregar una compra
def agregar_compra(monto):
    compras_realizadas.append(monto)
    print("Compra agregada correctamente.")

#Se define la función para mostrar las compras
def mostrar_compras():
    if not compras_realizadas:
        print("No hay compras registradas.")
    else:
        print("Lista de compras:")
        for i, monto in enumerate(compras_realizadas, start=1):
            print(f"Compra {i}: ${monto}")

#Se define la función para mostrar el total gastado
def mostrar_total():
    total_gastado = sum(compras_realizadas)
    total_gastado_formateado = "${:.2f}".format(total_gastado)
    print(f"Total gastado: {total_gastado_formateado}")


#Se define la funcion principal del programa (main)
def main():
    while True:
        print("Menú:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            monto = float(input("Ingresa el monto de la compra: "))
            agregar_compra(monto)
        elif opcion == "2":
            mostrar_compras()
        elif opcion == "3":
            mostrar_total()
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")

if __name__ == "__main__":
    main()