class Tarea:
    def __init__(self, titulo, descripcion):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False


class GestorTareas:
    def __init__(self):
        self.tareas = []

        def agregar_tarea(self, titulo, descripcion):
            if not titulo:
                raise ValueError("El título no puede estar vacío")
                tarea = Tarea(titulo, descripcion)
                self.tareas.append(tarea)

        def obtener_tareas(self):
            return self.tareas

        def marcar_completada(self, indice):
            if 0 <= indice < len(self.tareas):
                self.tareas[indice].completada = True
            else:
                raise IndexError("Índice fuera de rango")

        def eliminar_tarea(self, indice):
            if 0 <= indice < len(self.tareas):
                del self.tareas[indice]
            else:
                raise IndexError("Índice fuera de rango")
