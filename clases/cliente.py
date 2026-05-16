from abc import ABC, abstractmethod
from .excepciones import ErrorDatosVacios, ErrorIdentificacionInvalida

class EntidadSistema(ABC):
    """Clase abstracta obligatoria para representar cualquier entidad con ID y Nombre"""
    def __init__(self, identificador, nombre):
        if not identificador or not nombre:
            raise ErrorDatosVacios("El identificador y el nombre son campos obligatorios.")
        self._identificador = identificador
        self._nombre = nombre

    @abstractmethod
    def obtener_detalles(self):
        pass

class Cliente(EntidadSistema):
    """Clase Cliente con encapsulación estricta de datos personales"""
    def __init__(self, cedula, nombre, correo):
        # Validaciones de negocio usando nuestras excepciones de ingeniería
        if not cedula.isdigit():
            raise ErrorIdentificacionInvalida("La cédula debe contener únicamente números.")
        if len(nombre.strip()) < 3:
            raise ErrorIdentificacionInvalida("El nombre debe tener al menos 3 caracteres.")
        if "@" not in correo or "." not in correo:
            raise ErrorIdentificacionInvalida("El formato del correo electrónico es inválido.")
            
        super().__init__(cedula, nombre)
        self.__correo = correo  # Atributo privado (Encapsulación)

    # Propiedades (Getters) para acceder a los datos de forma segura
    @property
    def cedula(self):
        return self._identificador

    @property
    def nombre(self):
        return self._nombre

    @property
    def correo(self):
        return self.__correo

    def obtener_detalles(self):
        return f"Cliente: {self._nombre} | CC: {self._identificador} | Email: {self.__correo}"