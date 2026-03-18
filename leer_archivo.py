import sys

archivo = sys.argv[1]

try:
    with open(archivo, "r") as f:
        lineas = f.readlines()
        
        print("Contenido del archivo:")
        for linea in lineas:
            print(linea.strip())
        
        print("Cantidad de líneas:", len(lineas))

except FileNotFoundError:
    print("El archivo no existe")