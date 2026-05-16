class ErrorSistemaBase(Exception):
    """Clase raíz para controlar cualquier falla en Software FJ"""
    pass

class ErrorIdentificacionInvalida(ErrorSistemaBase):
    """Se dispara si el formato de la cédula o códigos es incorrecto"""
    pass

class ErrorDatosVacios(ErrorSistemaBase):
    """Se dispara si faltan parámetros obligatorios en los registros"""
    pass

class ErrorReservaInvalida(ErrorSistemaBase):
    """Se dispara ante inconsistencias en cálculos o estados de reserva"""
    pass