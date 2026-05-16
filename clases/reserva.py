from .excepciones import ErrorDatosVacios, ErrorReservaInvalida

class Reserva:
    """Clase que integra cliente, servicio y duración aplicando lógica de negocio"""
    def __init__(self, id_reserva, cliente, servicio, duracion):
        if not id_reserva:
            raise ErrorDatosVacios("El identificador de la reserva no puede estar vacío.")
        if duracion <= 0:
            raise ErrorReservaInvalida("La duración o cantidad debe ser un número mayor a cero.")
            
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Confirmada"
        
        # Aquí se ejecuta el polimorfismo puro: calcula el costo según el tipo de servicio
        self.total_pagar = servicio.calcular_costo(duracion)

    def cancelar_reserva(self):
        """Modifica el estado de la reserva controlando inconsistencias"""
        if self.estado == "Cancelada":
            raise ErrorReservaInvalida(f"La reserva {self.id_reserva} ya se encuentra cancelada.")
        self.estado = "Cancelada"

    def obtener_resumen(self):
        """Retorna la ficha técnica de la operación con el formato detallado"""
        return (f"Reserva ID: {self.id_reserva} | Estado: {self.estado}\n"
                f"  -> {self.cliente.obtener_detalles()}\n"
                f"  -> Servicio: {self.servicio.nombre} (Uso: {self.duracion})\n"
                f"  -> Total Liquidado: ${self.total_pagar:,.2f}")