class Tarea:
    id_counter = 1  # Para generar un ID único para cada tarea

    def __init__(self, titulo, descripcion, prioridad="Media"):
        self.id = Tarea.id_counter
        Tarea.id_counter += 1
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = False
        self.prioridad = prioridad  # Prioridad puede ser "Baja", "Media" o "Alta"


class GestorTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, titulo, descripcion, prioridad="Media"):
        if not titulo:
            raise ValueError("El título no puede estar vacío")
        tarea = Tarea(titulo, descripcion, prioridad)
        self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas

    # Los demás métodos no necesitan cambios para manejar prioridades
