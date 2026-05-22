from datetime import datetime
from src.utilidades.cifrado import generar_hash_sha256
from src.utilidades.algoritmo_genetico import generar_llave_evolutiva

class ComprobanteVoto:
    def __init__(self):
        self.hash_voto = None
        self.llave_dinamica = None
        self.timestamp = None

    def __str__(self):
        return f"Voto Seguro: Hash[{self.hash_voto[:10]}...] | Llave[{self.llave_dinamica}]"

class VotoSeguroBuilder:
    def __init__(self):
        self.comprobante = ComprobanteVoto()

    def aplicar_cifrado(self, dni: str, candidato_id: str):
        data_cruda = f"{dni}-{candidato_id}"
        self.comprobante.hash_voto = generar_hash_sha256(data_cruda)
        return self # Permite encadenamiento

    def generar_llave_genetica(self):
        self.comprobante.llave_dinamica = generar_llave_evolutiva()
        return self

    def estampar_tiempo(self):
        self.comprobante.timestamp = datetime.now().isoformat()
        return self

    def construir(self) -> ComprobanteVoto:
        return self.comprobante