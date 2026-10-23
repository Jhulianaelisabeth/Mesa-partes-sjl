#Archivos
import os

ARCHIVO = "reporte_vias.txt"
reportes = []

def cargar_reportes():
 if os.path.exists(ARCHIVO):
    with open(ARCHIVO, "r", encoding="utf-8") as archivo:
            for linea in archivo:
                datos = linea.rstrip("\n").split("|")
                if len(datos) == 7: 
                    reportes.append({
                        "codigo": datos[0],
                        "tipo_via": datos[1],
                        "desastre": datos[2],
                        "lugar": datos[3],
                        "gravedad": int(datos[4]),
                        "descripcion": datos[5],
                        "fecha": datos[6]
                    })

def guardar_reportes():
    with open(ARCHIVO, "w", encoding="utf-8") as archivo:
        for rep in reportes:
            linea = (
                rep["codigo"] + "|" + rep["tipo_via"] + "|" + rep["desastre"] + "|" +
                rep["lugar"] + "|" + str(rep["gravedad"]) + "|" + 
                rep["descripcion"] + "|" + rep["fecha"] + "\n"
            )
            archivo.write(linea)