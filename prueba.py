# Lista donde se guardan todas las notas ingresadas
notas = []  

# Función que permite agregar una nota al registro
# Solicita nombre, valida rango de nota y la almacena
def agregar_nota():
    nombre = input("Ingrese nombre del alumno: ")
    try:
        nota = float(input("Ingrese nota (1.0 a 7.0): "))
        if nota < 1.0 or nota > 7.0:
            print("ERROR: La nota debe estar entre 1.0 y 7.0")
            return
    except ValueError:
        print("ERROR: Debe ingresar un número válido")
        return
    
    notas.append({"nombre": nombre, "nota": nota})
    print("Nota agregada correctamente\n")

# Función que muestra todas las notas registradas

def listar_notas():
    if not notas:
        print("No hay notas registradas.\n")
        return
    
    print("\n--- LISTA DE NOTAS ---")
    for n in notas:
        print(f"Alumno: {n['nombre']} - Nota: {n['nota']}")
    print()

# Función que calcula el promedio general de todas las notas
def promedio_general():
    if not notas:
        print("No hay notas para calcular el promedio.\n")
        return
    
    prom = sum(n["nota"] for n in notas) / len(notas)
    print(f"Promedio general: {prom:.2f}\n")
# Función que muestra cuántas notas se han ingresado
def cantidad_notas():
    print(f"Hay {len(notas)} notas registradas.\n")

# Función que muestra la nota más alta registrada
def nota_mas_alta():
    if not notas:
        print("No hay notas registradas.\n")
        return
    
    mayor = max(notas, key=lambda x: x["nota"])
    print(f"La nota más alta es {mayor['nota']} - Alumno: {mayor['nombre']}\n")

# Menú principal del programa
# Muestra opciones y ejecuta funciones según la selección
def menu():
    while True:
        print("\n===== GESTOR DE NOTAS =====\n")
        print("1. Agregar nota")
        print("2. Listar notas")
        print("3. Promedio general")
        print("4. Mostrar cantidad de notas")
        print("5. Mostrar nota más alta")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nota()
        elif opcion == "2":
            listar_notas()
        elif opcion == "3":
            promedio_general()
        elif opcion == "4":
            cantidad_notas()
        elif opcion == "5":
            nota_mas_alta()
        elif opcion == "6":
            print("Saliendo del programa...")
            print("Programa finalizado correctamente.")
            break
        else:
            print("Opción inválida, intente nuevamente.\n")

# Inicia la ejecución del programa
menu()