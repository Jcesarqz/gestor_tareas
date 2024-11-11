from PyQt5 import QtWidgets, QtCore
from src.logica.gestor_tareas import GestorTareas


class GestorTareasGUI(QtWidgets.QWidget):
    def __init__(self, gestor):
        super().__init__()
        self.gestor = gestor
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestor de Tareas")

        # Layout principal
        layout = QtWidgets.QVBoxLayout()

        # Entrada de título
        self.titulo_input = QtWidgets.QLineEdit(self)
        self.titulo_input.setPlaceholderText("Título de la tarea")
        layout.addWidget(self.titulo_input)

        # Entrada de descripción
        self.descripcion_input = QtWidgets.QLineEdit(self)
        self.descripcion_input.setPlaceholderText("Descripción de la tarea")
        layout.addWidget(self.descripcion_input)

        # Botón para agregar tarea
        agregar_btn = QtWidgets.QPushButton("Agregar Tarea", self)
        agregar_btn.clicked.connect(self.agregar_tarea)
        layout.addWidget(agregar_btn)

        # Lista de tareas
        self.tareas_list = QtWidgets.QListWidget(self)
        layout.addWidget(self.tareas_list)

        # Botón para marcar como completada
        completar_btn = QtWidgets.QPushButton("Marcar como Completada", self)
        completar_btn.clicked.connect(self.marcar_completada)
        layout.addWidget(completar_btn)

        # Botón para eliminar tarea
        eliminar_btn = QtWidgets.QPushButton("Eliminar Tarea", self)
        eliminar_btn.clicked.connect(self.eliminar_tarea)
        layout.addWidget(eliminar_btn)

        self.setLayout(layout)
        self.actualizar_lista()

    def agregar_tarea(self):
        titulo = self.titulo_input.text()
        descripcion = self.descripcion_input.text()
        try:
            self.gestor.agregar_tarea(titulo, descripcion)
            self.actualizar_lista()
            self.titulo_input.clear()
            self.descripcion_input.clear()
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def actualizar_lista(self):
        self.tareas_list.clear()
        for indice, tarea in enumerate(self.gestor.obtener_tareas()):
            estado = "Completada" if tarea.completada else "Pendiente"
            self.tareas_list.addItem(f"{indice + 1}. {tarea.titulo} - {estado}")

    def marcar_completada(self):
        seleccion = self.tareas_list.currentRow()
        if seleccion != -1:
            self.gestor.marcar_completada(seleccion)
            self.actualizar_lista()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para marcar como completada")

    def eliminar_tarea(self):
        seleccion = self.tareas_list.currentRow()
        if seleccion != -1:
            self.gestor.eliminar_tarea(seleccion)
            self.actualizar_lista()
        else:
            QtWidgets.QMessageBox.warning(self, "Advertencia", "Selecciona una tarea para eliminar")


def run():
    app = QtWidgets.QApplication([])
    gestor = GestorTareas()
    gui = GestorTareasGUI(gestor)
    gui.show()
    app.exec_()


if __name__ == "__main__":
    run()
