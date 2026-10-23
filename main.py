# Main
import main_archivos
import main_gestion

def menu():
    main_archivos.cargar_reportes()
    while True:
        print("\n================================")
        print("   MESA DE PARTES DIGITAL SJL")
        print("================================")
        print("1. Registrar reporte")
        print("2. Listar reportes (Por urgencia)")
        print("3. Guardar y Salir")
        print("================================")
        
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == "1": 
            main_gestion.registrar_reporte()
        elif opcion == "2": 
            main_gestion.listar_reportes_por_urgencia()
        elif opcion == "3":
            main_archivos.guardar_reportes()
            print("Saliendo del sistema...")
            break
        else: 
            print("Opción incorrecta.")

if __name__== "__main__":
    menu()