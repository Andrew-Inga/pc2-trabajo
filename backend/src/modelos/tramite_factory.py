from abc import ABC, abstractmethod
from datetime import datetime

# Interfaz base
class TramiteBase(ABC):
    @abstractmethod
    def procesar_derivacion(self) -> dict:
        pass

# Clases Concretas
class TramiteRegistroCivil(TramiteBase):
    def procesar_derivacion(self):
        return {"dependencia": "Registro Civil", "prioridad": "Alta", "sla_dias": 2}

class TramiteGRIAS(TramiteBase):
    def procesar_derivacion(self):
        return {"dependencia": "GRIAS", "prioridad": "Media", "sla_dias": 5}

# La Fábrica
class DerivacionFactory:
    @staticmethod
    def crear_tramite(tipo_dependencia: str) -> TramiteBase:
        tipo = tipo_dependencia.upper()
        if tipo == "REGISTRO_CIVIL":
            return TramiteRegistroCivil()
        elif tipo == "GRIAS":
            return TramiteGRIAS()
        else:
            raise ValueError(f"Dependencia {tipo} no reconocida en Mesa de Partes.")