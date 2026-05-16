from abc import ABC, abstractmethod
from .excepciones import ErrorDatosVacios, ErrorReservaInvalida

class Servicio(ABC):
    """Clase abstracta que define la estructura base de un servicio en la empresa"""
    def __init__(self, codigo, nombre, precio_base):
        if not codigo or not nombre:
            raise ErrorDatosVacios("El código y el nombre del servicio son obligatorios.")
        if precio_base <= 0:
            raise ErrorReservaInvalida("El precio base del servicio debe ser mayor a cero.")
            
        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = precio_base

    @property
    def codigo(self):
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @abstractmethod
    def calcular_costo(self, cantidad_o_horas):
        """Método abstracto para que cada servicio liquide su tarifa de forma independiente"""
        pass


# 1. Servicio: Reserva de Salas
class ReservaSala(Servicio):
    def __init__(self, codigo, nombre, precio_base, incluye_videobeam=False):
        super().__init__(codigo, nombre, precio_base)
        self.incluye_videobeam = incluye_videobeam

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorReservaInvalida("La cantidad de horas debe ser mayor a cero.")
        
        total = self._precio_base * horas
        if self.incluye_videobeam:
            total += 50000  # Costo adicional fijo por el uso de ayudas audiovisuales
        return total


# 2. Servicio: Alquiler de Equipos
class AlquilerEquipo(Servicio):
    def __init__(self, codigo, nombre, precio_base, seguro_daños=0.05):
        super().__init__(codigo, nombre, precio_base)
        self.seguro_daños = seguro_daños

    def calcular_costo(self, dias):
        if dias <= 0:
            raise ErrorReservaInvalida("La cantidad de días debe ser mayor a cero.")
            
        costo_base = self._precio_base * dias
        total = costo_base + (costo_base * self.seguro_daños)  # Suma el porcentaje del seguro
        return total


# 3. Servicio: Asesoría Especializada
class AsesoriaEspecializada(Servicio):
    def __init__(self, codigo, nombre, precio_base, es_remota=True):
        super().__init__(codigo, nombre, precio_base)
        self.es_remota = es_remota

    def calcular_costo(self, horas):
        if horas <= 0:
            raise ErrorReservaInvalida("La cantidad de horas de asesoría debe ser mayor a cero.")
            
        total = self._precio_base * horas
        if not self.es_remota:
            total += 30000  # Costo de viáticos si la consultoría requiere presencialidad
        return total