import os
from clases.cliente import Cliente
from clases.servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from clases.reserva import Reserva
from clases.excepciones import ErrorSistemaBase

# Listas en memoria para gestionar los objetos del sistema (sin base de datos)
lista_clientes = []
lista_servicios = []
lista_reservas = []

def registrar_evento_en_log(mensaje):
    """Escribe los eventos y errores controlados en el archivo logs.txt"""
    try:
        with open("logs.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{mensaje}\n")
    except Exception as e:
        print(f"Error crítico al escribir en el archivo de bitácora: {e}")

def simular_operaciones_requeridas():
    """Simula automáticamente las 10 operaciones exigidas (éxitos y fallos controlados)"""
    registrar_evento_en_log("=== INICIO DE SIMULACIÓN DE OPERACIONES EN SOFTWARE FJ ===")
    
    # 1. Base de Servicios Ofertados
    sala_premium = ReservaSala("S01", "Sala de Juntas Ejecutiva", 60000, incluye_videobeam=True)
    servidor_dev = AlquilerEquipo("E01", "Servidor Dedicado de Desarrollo", 120000)
    consultoria_cloud = AsesoriaEspecializada("A01", "Asesoría Arquitectura Cloud", 80000, es_remota=False)
    
    lista_servicios.extend([sala_premium, servidor_dev, consultoria_cloud])

    # --- SIMULACIÓN DE CLIENTES (ÉXITOS Y ERRORES) ---
    # Operación 1: Registro válido de Cliente 1
    try:
        c1 = Cliente("11111", "Manuel Vargas", "manuel@correo.com")
        lista_clientes.append(c1)
        registrar_evento_en_log("[ÉXITO] Operación 1: Cliente 1 registrado correctamente.")
    except Exception as e:
        registrar_evento_en_log(f"[FALLO] Operación 1: {e}")

    # Operación 2: Registro válido de Cliente 2
    try:
        c2 = Cliente("22222", "Carlos Mendoza", "carlos@correo.com")
        lista_clientes.append(c2)
        registrar_evento_en_log("[ÉXITO] Operación 2: Cliente 2 registrado correctamente.")
    except Exception as e:
        registrar_evento_en_log(f"[FALLO] Operación 2: {e}")

    # Operación 3: Intento inválido (Cédula con letras) -> Debe fallar y controlarse
    try:
        registrar_evento_en_log("[INTENTO] Operación 3: Registrando cliente con cédula inválida '12345A'...")
        c_error = Cliente("12345A", "Usuario Inválido", "error@correo.com")
        lista_clientes.append(c_error)
    except Exception as e:
        registrar_evento_en_log(f"[FALLO CONTROLADO] Operación 3: {e}")

    # Operación 4: Intento inválido (Correo sin estructura) -> Debe fallar y controlarse
    try:
        registrar_evento_en_log("[INTENTO] Operación 4: Registrando cliente con correo sin @...")
        c_error2 = Cliente("33333", "Ana Gomez", "anagomez.com")
        lista_clientes.append(c_error2)
    except Exception as e:
        registrar_evento_en_log(f"[FALLO CONTROLADO] Operación 4: {e}")

    # --- SIMULACIÓN DE RESERVAS (ÉXITOS Y ERRORES) ---
    # Operación 5: Reserva válida de Sala (Polimorfismo con videobeam)
    try:
        r1 = Reserva("RES-001", lista_clientes[0], sala_premium, 3) # 3 horas
        lista_reservas.append(r1)
        registrar_evento_en_log("[ÉXITO] Operación 5: Reserva RES-001 creada satisfactoriamente.")
    except Exception as e:
        registrar_evento_en_log(f"[FALLO] Operación 5: {e}")

    # Operación 6: Reserva válida de Equipos
    try:
        r2 = Reserva("RES-002", lista_clientes[1], servidor_dev, 5) # 5 días
        lista_reservas.append(r2)
        registrar_evento_en_log("[ÉXITO] Operación 6: Reserva RES-002 creada satisfactoriamente.")
    except Exception as e:
        registrar_evento_en_log(f"[FALLO] Operación 6: {e}")

    # Operación 7: Reserva válida de Asesoría Presencial (Polimorfismo con recargo)
    try:
        r3 = Reserva("RES-003", lista_clientes[0], consultoria_cloud, 4) # 4 horas
        lista_reservas.append(r3)
        registrar_evento_en_log("[ÉXITO] Operación 7: Reserva RES-003 creada satisfactoriamente.")
    except Exception as e:
        registrar_evento_en_log(f"[FALLO] Operación 7: {e}")

    # Operación 8: Intento inválido de Reserva (Duración negativa) -> Debe fallar
    try:
        registrar_evento_en_log("[INTENTO] Operación 8: Creando reserva con duración de -2 horas...")
        r_error = Reserva("RES-004", lista_clientes[0], sala_premium, -2)
        lista_reservas.append(r_error)
    except Exception as e:
        registrar_evento_en_log(f"[FALLO CONTROLADO] Operación 8: {e}")

    # --- SIMULACIÓN DE CANCELACIONES (ÉXITOS Y ERRORES) ---
    # Operación 9: Cancelación válida
    try:
        lista_reservas[0].cancelar_reserva()
        registrar_evento_en_log("[ÉXITO] Operación 9: Reserva RES-001 cancelada con éxito.")
    except Exception as e:
        registrar_evento_en_log(f"[FALLO] Operación 9: {e}")

    # Operación 10: Intento inválido (Duplicar cancelación) -> Debe fallar
    try:
        registrar_evento_en_log("[INTENTO] Operación 10: Intentando cancelar RES-001 por segunda vez...")
        lista_reservas[0].cancelar_reserva()
    except Exception as e:
        registrar_evento_en_log(f"[FALLO CONTROLADO] Operación 10: {e}")

    registrar_evento_en_log("=== FIN DE LA SIMULACIÓN AUTOMÁTICA ===\n")


def ejecutar_menu():
    # Ejecutamos las 10 operaciones simuladas por debajo al arrancar
    simular_operaciones_requeridas()
    
    while True:
        print("\n" + "="*50)
        print("     SISTEMA INTEGRAL DE GESTIÓN - SOFTWARE FJ")
        print("="*50)
        print("1. Registrar Nuevo Cliente (Manual)")
        print("2. Crear Nueva Reserva (Manual)")
        print("3. Ver Reporte Global de Reservas")
        print("4. Cancelar una Reserva")
        print("5. Salir del Sistema")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n--- REGISTRO DE CLIENTE ---")
            try:
                cedula = input("Cédula (Solo números): ").strip()
                nombre = input("Nombre completo: ").strip()
                correo = input("Correo electrónico: ").strip()
                
                nuevo_cliente = Cliente(cedula, nombre, correo)
                lista_clientes.append(nuevo_cliente)
                print(f"¡Éxito! Cliente {nombre} guardado correctamente.")
                registrar_evento_en_log(f"[USER] Cliente registrado manualmente: CC {cedula}")
                
            except ErrorSistemaBase as e:
                print(f"\n[Error Controlado]: {e}")
                registrar_evento_en_log(f"[USER ERROR] Registro manual fallido: {e}")
            except Exception as e:
                print(f"\n[Error Inesperado]: {e}")
                registrar_evento_en_log(f"[CRÍTICO] Error inesperado en Clientes: {e}")

        elif opcion == "2":
            print("\n--- CREAR RESERVA ---")
            if not lista_clientes:
                print("No hay clientes registrados en el sistema.")
                continue
                
            try:
                id_reserva = input("Código único de reserva: ").strip()
                cc_cliente = input("Cédula del cliente: ").strip()
                
                cliente_enc = next((c for c in lista_clientes if c.cedula == cc_cliente), None)
                if not cliente_enc:
                    print("El cliente no está registrado.")
                    continue
                
                print("\nServicios en Portafolio:")
                for i, serv in enumerate(lista_servicios, 1):
                    print(f"  {i}. {serv.nombre} (Código: {serv.codigo})")
                    
                sel = int(input("Seleccione el número del servicio: ")) - 1
                if sel < 0 or sel >= len(lista_servicios):
                    print("Selección inválida.")
                    continue
                    
                duracion = int(input("Ingrese la duración (Horas / Días): "))
                
                nueva_reserva = Reserva(id_reserva, cliente_enc, lista_servicios[sel], duracion)
                lista_reservas.append(nueva_reserva)
                print("\n¡Reserva generada exitosamente!")
                registrar_evento_en_log(f"[USER] Reserva manual creada: ID {id_reserva}")
                
            except (ValueError, TypeError):
                print("\n[Error de Formato]: Se ingresaron caracteres no numéricos.")
                registrar_evento_en_log("[USER ERROR] Entrada de datos no numérica en reserva manual.")
            except ErrorSistemaBase as e:
                print(f"\n[Error Controlado]: {e}")
                registrar_evento_en_log(f"[USER ERROR] Reserva manual fallida: {e}")

        elif opcion == "3":
            print("\n--- REPORTE GLOBAL DE RESERVAS ---")
            if not lista_reservas:
                print("No se registran transacciones en el sistema.")
            else:
                for res in lista_reservas:
                    print("-" * 45)
                    print(res.obtener_resumen())
                print("-" * 45)

        elif opcion == "4":
            print("\n--- CANCELAR RESERVA ---")
            id_canc = input("Ingrese el código de la reserva a cancelar: ").strip()
            reserva_enc = next((r for r in lista_reservas if r.id_reserva == id_canc), None)
            
            try:
                if not reserva_enc:
                    print(f"No existe ninguna reserva bajo el código '{id_canc}'")
                    continue
                reserva_enc.cancelar_reserva()
                print(f"La reserva {id_canc} ha sido cancelada.")
                registrar_evento_en_log(f"[USER] Reserva {id_canc} cancelada manualmente.")
            except ErrorSistemaBase as e:
                print(f"\n[Error al Cancelar]: {e}")
                registrar_evento_en_log(f"[USER ERROR] Falla al cancelar {id_canc}: {e}")

        elif opcion == "5":
            print("\nCerrando el ecosistema de Software FJ. ¡Proceso completado con éxito!")
            break
        else:
            print("\nOpción no válida. Ingrese un dígito del 1 al 5.")

if __name__ == "__main__":
    ejecutar_menu()