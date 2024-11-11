from PyQt5 import QtWidgets, QtCore, QtGui
from src.logica.gestor_tareas import GestorTareas

class GestorTareasGUI(QtWidgets.QWidget):
    def __init__(self, gestor):
        super().__init__()
        self.gestor = gestor
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Gestor de Tareas")

        layout = QtWidgets.QVBoxLayout()

        # Entradas de título y descripción
        self.titulo_input = QtWidgets.QLineEdit(self)
        self.titulo_input.setPlaceholderText("Título de la tarea")
        layout.addWidget(self.titulo_input)

        self.descripcion_input = QtWidgets.QLineEdit(self)
        self.descripcion_input.setPlaceholderText("Descripción de la tarea")
        layout.addWidget(self.descripcion_input)

        # Combo box para seleccionar la prioridad
        self.prioridad_combo = QtWidgets.QComboBox(self)
        self.prioridad_combo.addItems(["Baja", "Media", "Alta"])
        layout.addWidget(self.prioridad_combo)

        # Botones para agregar y actualizar tarea
        agregar_btn = QtWidgets.QPushButton("Agregar Tarea", self)
        agregar_btn.clicked.connect(self.agregar_tarea)
        layout.addWidget(agregar_btn)

        self.actualizar_btn = QtWidgets.QPushButton("Actualizar Tarea", self)
        self.actualizar_btn.clicked.connect(self.actualizar_tarea)
        self.actualizar_btn.setEnabled(False)  # Deshabilitado inicialmente
        layout.addWidget(self.actualizar_btn)

        # Lista de tareas
        self.tareas_list = QtWidgets.QListWidget(self)
        self.tareas_list.itemClicked.connect(self.cargar_tarea)
        layout.addWidget(self.tareas_list)

        # Botones para marcar como completada y eliminar
        completar_btn = QtWidgets.QPushButton("Marcar como Completada", self)
        completar_btn.clicked.connect(self.marcar_completada)
        layout.addWidget(completar_btn)

        eliminar_btn = QtWidgets.QPushButton("Eliminar Tarea", self)
        eliminar_btn.clicked.connect(self.eliminar_tarea)
        layout.addWidget(eliminar_btn)

        self.setLayout(layout)
        self.actualizar_lista()

    def agregar_tarea(self):
        titulo = self.titulo_input.text()
        descripcion = self.descripcion_input.text()
        prioridad = self.prioridad_combo.currentText()
        try:
            self.gestor.agregar_tarea(titulo, descripcion, prioridad)
            self.actualizar_lista()
            self.titulo_input.clear()
            self.descripcion_input.clear()
            self.prioridad_combo.setCurrentIndex(1)  # Resetear a "Media"
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def cargar_tarea(self, item):
        index = self.tareas_list.row(item)
        tarea = self.gestor.obtener_tareas()[index]
        self.titulo_input.setText(tarea.titulo)
        self.descripcion_input.setText(tarea.descripcion)
        self.prioridad_combo.setCurrentText(tarea.prioridad)
        self.actualizar_btn.setEnabled(True)
        self.actualizar_btn.setProperty("task_id", tarea.id)

    def actualizar_tarea(self):
        tarea_id = self.actualizar_btn.property("task_id")
        nuevo_titulo = self.titulo_input.text()
        nueva_descripcion = self.descripcion_input.text()
        nueva_prioridad = self.prioridad_combo.currentText()
        try:
            self.gestor.actualizar_tarea(tarea_id, nuevo_titulo, nueva_descripcion, nueva_prioridad)
            self.actualizar_lista()
            self.titulo_input.clear()
            self.descripcion_input.clear()
            self.prioridad_combo.setCurrentIndex(1)  # Resetear a "Media"
            self.actualizar_btn.setEnabled(False)
        except ValueError as e:
            QtWidgets.QMessageBox.critical(self, "Error", str(e))

    def actualizar_lista(self):
        self.tareas_list.clear()
        for indice, tarea in enumerate(self.gestor.obtener_tareas()):
            item = QtWidgets.QListWidgetItem(f"{tarea.titulo} - {'Completada' if tarea.completada else 'Pendiente'}")
            color = self.obtener_color_prioridad(tarea.prioridad)
            item.setBackground(color)
            self.tareas_list.addItem(item)

    def obtener_color_prioridad(self, prioridad):
        if prioridad == "Alta":
            return QtGui.QColor("red")
        elif prioridad == "Media":
            return QtGui.QColor("yellow")
        elif prioridad == "Baja":
            return QtGui.QColor("green")
        return QtGui.QColor("white")

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
