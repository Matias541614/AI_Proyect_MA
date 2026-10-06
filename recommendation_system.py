# Importar libreria math
# Crear una clase llamada SistemaRecomendacion
# Inicializar la clase con un diccionario complejo de 5 usuarios, 5 peliculas y sus calificaciones (del 1 al 5)
# Crear un metodo para calcular la similitud de gustos entre dos usuarios
# Crear un metodo principal que reciba el nombre de un usuario y devuelva las 2 mejores recomendaciones de peliculas que aun no ha visto, ordenadas por puntaje
# Crear una instancia de la clase y realizar un print de prueba con un usuario especifico
import math

class SistemaRecomendacion:
    def __init__(self):
        self.usuarios = {
            'usuario1': {'pelicula1': 5, 'pelicula2': 3, 'pelicula3': 4, 'pelicula4': 2, 'pelicula5': 1},
            'usuario2': {'pelicula1': 4, 'pelicula2': 5, 'pelicula3': 2, 'pelicula4': 3, 'pelicula5': 1},
            'usuario3': {'pelicula1': 2, 'pelicula2': 1, 'pelicula3': 5, 'pelicula4': 4, 'pelicula5': 3},
            'usuario4': {'pelicula1': 3, 'pelicula2': 4, 'pelicula3': 1, 'pelicula4': 5, 'pelicula5': 2},
            'usuario5': {'pelicula1': 1, 'pelicula2': 2, 'pelicula3': 3, 'pelicula4': 4, 'pelicula5': 5}
        }

    def calcular_similitud(self, usuario_a, usuario_b):
        # Obtener las calificaciones de ambos usuarios
        calificaciones_a = self.usuarios[usuario_a]
        calificaciones_b = self.usuarios[usuario_b]

        # Calcular la similitud usando la fórmula de similitud del coseno
        dot_product = sum(calificaciones_a[p] * calificaciones_b[p] for p in calificaciones_a)
        magnitude_a = math.sqrt(sum(calificaciones_a[p] ** 2 for p in calificaciones_a))
        magnitude_b = math.sqrt(sum(calificaciones_b[p] ** 2 for p in calificaciones_b))

        if magnitude_a == 0 or magnitude_b == 0:
            return 0

        return dot_product / (magnitude_a * magnitude_b)

    def recomendar_peliculas(self, usuario):
        recomendaciones = {}
        for otro_usuario in self.usuarios:
            if otro_usuario != usuario:
                similitud = self.calcular_similitud(usuario, otro_usuario)
                for pelicula in self.usuarios[otro_usuario]:
                    if pelicula not in self.usuarios[usuario]:
                        if pelicula not in recomendaciones:
                            recomendaciones[pelicula] = similitud * self.usuarios[otro_usuario][pelicula]

        # Ordenar las recomendaciones por puntaje y devolver las 2 mejores
        recomendaciones_ordenadas = sorted(recomendaciones.items(), key=lambda x: x[1], reverse=True)
        return recomendaciones_ordenadas[:2]

# Crear una instancia de la clase y realizar un print de prueba con un usuario especifico
sistema = SistemaRecomendacion()
usuario_prueba = 'usuario1'
recomendaciones = sistema.recomendar_peliculas(usuario_prueba)
print(f"Recomendaciones para {usuario_prueba}: {recomendaciones}")


