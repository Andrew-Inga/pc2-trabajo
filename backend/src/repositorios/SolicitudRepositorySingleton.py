class SolicitudRepositorySingleton:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(SolicitudRepositorySingleton, cls).__new__(cls)
            # Inicializamos la "base de datos" en memoria por única vez
            cls._instancia.votos_almacenados = []
            cls._instancia.solicitudes_derivadas = []
            print("📦 Repositorio en memoria inicializado.")
        return cls._instancia

    def guardar_voto(self, voto_cifrado):
        self.votos_almacenados.append(voto_cifrado)
        return True

    def obtener_todos_los_votos(self):
        return self.votos_almacenados