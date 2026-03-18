import sys
import os

archivo = sys.argv[1]

if os.path.exists(archivo):
    print("El archivo existe")
    
    if os.access(archivo, os.R_OK):
        print("Se puede leer")
    else:
        print("No se puede leer")
else:
    print("El archivo no existe")