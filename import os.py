import os
import time

# Lista donde guardaremos las tareas (cada tarea será un diccionario)
tareas = []

def limpiar_pantalla():
    """Limpia la terminal dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra un encabezado estético para el programa."""
    print("=" * 45)
    print("       ORGANIZADOR DE TAREAS ESCOLARES       ")
    print("=" * 45)

def agregar_tarea():
    """Solicita los datos de la tarea y la añade a la lista."""
    limpiar_pantalla()
    print("--- AGREGAR NUEVA TAREA ---\n")
    
    materia = input("Ingresa la materia (ej. Matemáticas, Historia): ").strip()
    descripcion = input("Describe brevemente la tarea: ").strip()
    fecha_limite = input("Fecha de entrega (ej. 25 de Octubre): ").strip()
    
    if materia and descripcion and fecha_limite:
        nueva_tarea = {
            "materia": materia,
            "descripcion": descripcion,
            "fecha": fecha_limite,
            "completada": False
        }
        tareas.append(nueva_tarea)
        print("\n[✔] ¡Tarea agregada con éxito!")
    else:
        print("\n[✖] Error: Todos los campos son obligatorios.")
    
    input("\nPresiona Enter para volver al menú...")

def mostrar_tareas():
    """Muestra todas las tareas registradas hasta el momento."""
    limpiar_pantalla()
    print("--- LISTA DE TAREAS PENDIENTES ---\n")
    
    if not tareas:
        print("No hay tareas registradas todavía. ¡Vas al día!")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "✔ Completada" if tarea["completada"] else "⏳ Pendiente"
            print(f"[{i}] Materia: {tarea['materia']}")
            print(f"    Descripción: {tarea['descripcion']}")
            print(f"    Entrega: {tarea['fecha']}")
            print(f"    Estado: {estado}")
            print("-" * 40)
            
    input("\nPresiona Enter para volver al menú...")

def principal():
    """Bucle principal del programa que maneja el menú."""
    while True:
        limpiar_pantalla()
        mostrar_banner()
        print("\n1. Agregar tarea")
        print("2. Mostrar todas las tareas")
        print("3. Salir del programa")
        
        opcion = input("\nElige una opción (1-3): ").strip()
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            mostrar_tareas()
        elif opcion == "3":
            limpiar_pantalla()
            print("Saliendo del organizador. ¡Mucho éxito con tus estudios!")
            time.sleep(1.5)
            break
        else:
            print("\n[✖] Opción no válida. Ingresa un número entre 1 y 3.")
            time.sleep(1.2)

# Punto de entrada del script
if __name__ == "__main__":
    principal()