# Gestion
from datetime import datetime
from main_archivos import reportes, guardar_reportes

tipos_vias = ["Carretera", "Puente", "Calle", "Avenida"]
tipos_desastres = ["Huaico", "Inundación", "Terremoto", "Otro"]

def leer_texto(mensaje):
    while True:
        texto = input(mensaje).strip()
        if texto and "|" not in texto:
            return texto
        print("Error: Ingresa un texto válido (sin el caracter |).")

def registrar_reporte():
    print("\n--- REGISTRAR VÍA AFECTADA ---")
    print("\nTipo de vía:")
    for i, tv in enumerate(tipos_vias, start=1): print(i, "-", tv)
    try:
        op_via = int(input("Selecciona (1-4): "))
        tipo_via = tipos_vias[op_via - 1]
    except:
        print("Opción inválida."); return

    print("\nDesastre ocurrido:")
    for i, td in enumerate(tipos_desastres, start=1): print(i, "-", td)
    try:
        op_des = int(input("Selecciona (1-4): "))
        desastre = tipos_desastres[op_des - 1]
    except:
        print("Opción inválida."); return

    lugar = leer_texto("Ubicación exacta: ")
    descripcion = leer_texto("Descripción breve: ")

    print("\nGravedad: 1-Bajo | 2-Medio | 3-Alto | 4-Crítico")
    try:
        gravedad = int(input("Selecciona (1-4): "))
        if gravedad < 1 or gravedad > 4: raise ValueError
    except:
        print("Gravedad inválida."); return

    codigo = "REP" + str(len(reportes) + 1).zfill(4)
    reporte = {
        "codigo": codigo, "tipo_via": tipo_via, "desastre": desastre,
        "lugar": lugar, "gravedad": gravedad, "descripcion": descripcion,
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M")
    }
    reportes.append(reporte)
    guardar_reportes()
    print(f"\nReporte {codigo} registrado.")

def listar_reportes_por_urgencia():
    if not reportes:
        print("\nNo hay reportes.")
        return
    print("\n--- REPORTES ORDENADOS ---")
    
    # ORDENADO POR URGENCIA
    n = len(reportes)
    for i in range(n):
        for j in range(0, n - i - 1):
            if reportes[j]["gravedad"] < reportes[j + 1]["gravedad"]:
                reportes[j], reportes[j + 1] = reportes[j + 1], reportes[j]

    urgencia_txt = {4: "CRÍTICA", 3: "ALTA", 2: "MEDIA", 1: "BAJA"}
    for rep in reportes:
        print("------------------------------")
        print(f"Código: {rep['codigo']} | Gravedad: {rep['gravedad']} ({urgencia_txt[rep['gravedad']]})")
        print(f"Vía: {rep['tipo_via']} en {rep['lugar']}")
        print(f"Evento: {rep['desastre']}")
        print(f"Desc: {rep['descripcion']} | Fecha: {rep['fecha']}")
        
    print("------------------------------")
    input("\nPresiona ENTER para volver al menú...")