import sys

from jacobi import jacobi

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QPlainTextEdit,
    QGridLayout,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QGroupBox,
    QScrollArea
)

class Ventana(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculadora de métodos numéricos")
        self.resize(800, 700)

        self.campos_matriz = []
        self.campos_vector = []

        self.construir_interfaz()

    def construir_interfaz(self):

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout(central)

        # Titulo
        titulo = QLabel("Métodos numéricos")
        titulo.setStyleSheet(
            "font-size: 24px; font-weight: bold;"
        )

        layout.addWidget(titulo)

        # --------------------------------
        # DIMENSION DE LA MATRIZ
        # --------------------------------

        grupo_dimension = QGroupBox("Dimension del sistema")
        dimension_layout = QHBoxLayout(grupo_dimension)

        dimension_layout.addWidget(
            QLabel("Numero de incognitas:")
        )

        self.txt_dimension = QLineEdit()
        self.txt_dimension.setPlaceholderText("Ej: 3")
        self.txt_dimension.setMaximumWidth(100)

        dimension_layout.addWidget(self.txt_dimension)

        self.btn_generar = QPushButton("Generar matriz")

        self.btn_generar.clicked.connect(
            self.generar_matriz
        )

        dimension_layout.addWidget(self.btn_generar)

        dimension_layout.addStretch()

        layout.addWidget(grupo_dimension)

        # --------------------------------
        # CONTENEDOR DINAMICO
        # --------------------------------

        self.contenedor = QWidget()
        contenedor_layout = QHBoxLayout(self.contenedor)

        # Matriz A
        self.grupo_matriz = QGroupBox("Matriz de coeficientes (A)")
        self.layout_matriz = QGridLayout(self.grupo_matriz)

        # Vector b
        self.grupo_vector = QGroupBox("Vector independiente (b)")
        self.layout_vector = QVBoxLayout(self.grupo_vector)

        contenedor_layout.addWidget(self.grupo_matriz)
        contenedor_layout.addWidget(self.grupo_vector)

        # Scroll para matrices grandes
        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.contenedor)

        layout.addWidget(self.scroll, 3)

        # --------------------------------
        # PARAMETROS
        # --------------------------------

        grupo_parametros = QGroupBox("Parametros de ejecucion")
        parametros_layout = QGridLayout(grupo_parametros)

        parametros_layout.addWidget(
            QLabel("Tolerancia:"), 0, 0
        )

        self.txt_tolerancia = QLineEdit("0.0001")
        parametros_layout.addWidget(
            self.txt_tolerancia, 0, 1
        )

        parametros_layout.addWidget(
            QLabel("Maximo de iteraciones:"), 0, 2
        )

        self.txt_iteraciones = QLineEdit("100")
        parametros_layout.addWidget(
            self.txt_iteraciones, 0, 3
        )

        layout.addWidget(grupo_parametros)

        # --------------------------------
        # BOTONES
        # --------------------------------

        botones = QHBoxLayout()

        self.btn_ejecutar = QPushButton("Ejecutar metodo")
        self.btn_limpiar = QPushButton("Limpiar")

        self.btn_ejecutar.clicked.connect(self.ejecutar)
        self.btn_limpiar.clicked.connect(self.limpiar)

        botones.addWidget(self.btn_ejecutar)
        botones.addWidget(self.btn_limpiar)

        layout.addLayout(botones)

        # --------------------------------
        # RESULTADOS
        # --------------------------------

        grupo_resultados = QGroupBox("Resultados")
        resultado_layout = QVBoxLayout(grupo_resultados)

        self.txt_resultados = QPlainTextEdit()
        self.txt_resultados.setReadOnly(True)

        resultado_layout.addWidget(self.txt_resultados)

        layout.addWidget(grupo_resultados, 2)

    # --------------------------------
    # GENERAR MATRIZ DINAMICAMENTE
    # --------------------------------

    def generar_matriz(self):

        try:

            n = int(self.txt_dimension.text())

            if n <= 0:
                raise ValueError(
                    "La dimension debe ser mayor que cero"
                )

            if n > 20:
                raise ValueError(
                    "La dimension maxima permitida es 20"
                )

            # Eliminar campos anteriores
            self.limpiar_layout(self.layout_matriz)
            self.limpiar_layout(self.layout_vector)

            self.campos_matriz = []
            self.campos_vector = []

            # --------------------------------
            # CREAR MATRIZ A
            # --------------------------------

            for i in range(n):

                fila_campos = []

                for j in range(n):

                    campo = QLineEdit()
                    campo.setPlaceholderText(f"A{i+1}{j+1}")
                    campo.setFixedWidth(65)
                    campo.setAlignment(
                        self.alineacion_centrada()
                    )

                    self.layout_matriz.addWidget(
                        campo, i, j
                    )

                    fila_campos.append(campo)

                self.campos_matriz.append(fila_campos)

            # --------------------------------
            # CREAR VECTOR B
            # --------------------------------

            for i in range(n):

                campo = QLineEdit()
                campo.setPlaceholderText(f"b{i+1}")
                campo.setFixedWidth(65)
                campo.setAlignment(
                    self.alineacion_centrada()
                )

                self.layout_vector.addWidget(campo)

                self.campos_vector.append(campo)

            self.layout_vector.addStretch()

            self.txt_resultados.clear()

        except ValueError as error:

            QMessageBox.warning(
                self,
                "Dimension invalida",
                "Debe introducir un número válido."
            )

    # --------------------------------
    # FUNCIONES AUXILIARES
    # --------------------------------

    def limpiar_layout(self, layout):

        while layout.count():

            elemento = layout.takeAt(0)

            widget = elemento.widget()

            if widget is not None:
                widget.deleteLater()

    def alineacion_centrada(self):

        from PyQt6.QtCore import Qt

        return Qt.AlignmentFlag.AlignCenter

    # --------------------------------
    # LEER MATRIZ Y VECTOR
    # --------------------------------

    def leer_matriz(self):

        if not self.campos_matriz:
            raise ValueError(
                "Primero debes generar una matriz"
            )

        matriz = []

        for fila in self.campos_matriz:

            valores = []

            for campo in fila:

                texto = campo.text().strip()

                if not texto:
                    raise ValueError(
                        "Todos los campos de la matriz deben completarse"
                    )

                valores.append(float(texto))

            matriz.append(valores)

        return matriz

    def leer_vector(self):

        vector = []

        for campo in self.campos_vector:

            texto = campo.text().strip()

            if not texto:
                raise ValueError(
                    "Todos los campos del vector deben completarse"
                )

            vector.append(float(texto))

        return vector

    # --------------------------------
    # EJECUTAR METODO
    # --------------------------------

    def ejecutar(self):
        try:

            # Obtener matriz y vector
            A = self.leer_matriz()
            b = self.leer_vector()

            # Obtener parametros
            tolerancia = float(
                self.txt_tolerancia.text()
            )

            max_iter = int(
                self.txt_iteraciones.text()
            )

            # Validar parametros
            if tolerancia <= 0:
                raise ValueError(
                    "La tolerancia debe ser positiva"
                )

            if max_iter <= 0:
                raise ValueError(
                    "Las iteraciones deben ser positivas"
                )

            # Ejecutar modulo de Jacobi
            solucion, salida = jacobi(
                A,
                b,
                tolerancia,
                max_iter
            )

            # Mostrar resultados
            self.txt_resultados.clear()
            self.txt_resultados.setPlainText(salida)
            self.txt_resultados.verticalScrollBar().setValue(
                self.txt_resultados.verticalScrollBar().maximum()
            )

        except ValueError as error:
            QMessageBox.warning(
                self,
                "Error de entrada",
                str(error)
            )

        except Exception as error:

            QMessageBox.critical(
                self,
                "Error",
                f"Ocurrió un error en la ejecución del programa: {str(error)}"
            )


    # --------------------------------
    # LIMPIAR INTERFAZ
    # --------------------------------

    def limpiar(self):

        self.txt_dimension.clear()
        self.txt_resultados.clear()

        self.limpiar_layout(self.layout_matriz)
        self.limpiar_layout(self.layout_vector)

        self.campos_matriz = []
        self.campos_vector = []


# --------------------------------
# EJECUCION
# --------------------------------

if __name__ == "__main__":

    app = QApplication(sys.argv)

    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec())
