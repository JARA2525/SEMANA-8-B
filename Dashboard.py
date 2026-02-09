# ============================================
# DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS
# Autor: Jhon Jara
# Descripción: Sistema para navegar carpetas y ejecutar scripts Python
# ============================================

# Importación de librerías necesarias
import os  # Manejo de archivos y directorios
import subprocess  # Ejecución de procesos externos

# ============================================
# FUNCIÓN: MOSTRAR CÓDIGO DE UN SCRIPT
# ============================================
def mostrar_codigo(ruta_script):
    # Convertir la ruta a absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        # Abrir archivo en modo lectura
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()  # Leer contenido completo
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)  # Mostrar código
            return codigo  # Retornar código
    except FileNotFoundError:
        # Error si no existe el archivo
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        # Capturar otros errores
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None

# ============================================
# FUNCIÓN: EJECUTAR SCRIPT EXTERNO
# ============================================
def ejecutar_codigo(ruta_script):
    try:
        # Detectar sistema operativo
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux / Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        # Mostrar error si falla ejecución
        print(f"Ocurrió un error al ejecutar el código: {e}")

# ============================================
# FUNCIÓN: MENÚ PRINCIPAL
# ============================================
def mostrar_menu():
    # Ruta base del archivo actual
    ruta_base = os.path.dirname(__file__)

    # Diccionario de unidades disponibles
    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    # Bucle infinito del menú
    while True:

        # Limpiar pantalla (mejora visual)
        os.system('cls' if os.name == 'nt' else 'clear')

        # ============================================
        # CUADRO ASCII DECORATIVO DEL SISTEMA
        # ============================================
        print("╔══════════════════════════════════════════════════════╗")
        print("║              SISTEMA DASHBOARD POO                   ║")
        print("║        Autor: Jhon Jara - Segundo Semestre            ║")
        print("║        Universidad Estatal Amazónica                 ║")
        print("╚══════════════════════════════════════════════════════╝")

        # Mostrar menú principal
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        # Leer opción del usuario
        eleccion_unidad = input("Elige una unidad o '0' para salir: ")

        # Confirmación antes de salir (mejora funcional)
        if eleccion_unidad == '0':
            confirmar = input("¿Seguro que desea salir? (s/n): ")
            if confirmar.lower() == 's':
                print("Saliendo del programa.")
                break
            else:
                continue

        # Si la opción es válida
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# ============================================
# FUNCIÓN: SUBMENÚ DE CARPETAS
# ============================================
def mostrar_sub_menu(ruta_unidad):
    # Obtener subcarpetas
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")

        # Mostrar subcarpetas
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        # Leer opción
        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")

        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# ============================================
# FUNCIÓN: MOSTRAR SCRIPTS PYTHON
# ============================================
def mostrar_scripts(ruta_sub_carpeta):
    # Listar scripts Python
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]

    # Mostrar cantidad de scripts encontrados
    print(f"\nTotal de scripts encontrados: {len(scripts)}")

    # Validación si no hay scripts
    if not scripts:
        print("No hay scripts disponibles en esta carpeta.")
        return

    while True:
        print("\nScripts - Selecciona un script para ver y ejecutar")

        # Mostrar scripts
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú anterior")
        print("9 - Regresar al menú principal")

        # Leer opción
        eleccion_script = input("Elige un script, '0' para regresar o '9' para ir al menú principal: ")

        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])
                    codigo = mostrar_codigo(ruta_script)

                    # Preguntar si desea ejecutar
                    if codigo:
                        ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                        if ejecutar == '1':
                            ejecutar_codigo(ruta_script)
                        elif ejecutar == '0':
                            print("No se ejecutó el script.")
                        else:
                            print("Opción no válida.")

                        # Pausa
                        input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida. Por favor, intenta de nuevo.")
            except ValueError:
                print("Opción no válida. Por favor, intenta de nuevo.")

# ============================================
# BLOQUE PRINCIPAL DEL PROGRAMA
# ============================================
if __name__ == "__main__":
    # Ejecutar menú principal
    mostrar_menu()
