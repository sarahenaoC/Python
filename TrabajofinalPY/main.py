import sys
import numpy as np
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QFrame
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPalette, QColor

# Cargar tus datos
df = pd.read_csv("heart_disease.csv")

# Selecciona las variables predictoras y la variable objetivo
features = df[["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"]]
target = df["target"]

# Divide los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=42)

# Crea el modelo de Bosques Aleatorios
model = RandomForestClassifier()

# Entrena el modelo
model.fit(X_train, y_train)

class InfartoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Predicción de Infarto')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        frame = QFrame(self)
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setStyleSheet("background-color: #f0f0f0;")
        layout.addWidget(frame)

        title_label = QLabel('Predicción de Infarto', frame)
        title_label.setFont(QFont('Arial', 16))
        title_label.setAlignment(Qt.AlignCenter)

        layout.addWidget(title_label)

        self.input_fields = {}
        for feature in features.columns:
            label = QLabel(f'Ingrese {feature}:', frame)
            input_field = QLineEdit(frame)
            layout.addWidget(label)
            layout.addWidget(input_field)
            self.input_fields[feature] = input_field

        result_label = QLabel('Resultado:', frame)
        result_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(result_label)

        self.result_text = QTextEdit(frame)
        self.result_text.setReadOnly(True)
        self.result_text.setStyleSheet("background-color: #f9f9f9;")
        layout.addWidget(self.result_text)

        predict_button = QPushButton('Predecir', frame)
        predict_button.setStyleSheet("background-color: #add8e6;")  # Azul claro
        predict_button.clicked.connect(self.predict)
        layout.addWidget(predict_button)

        clear_button = QPushButton('Borrar', frame)
        clear_button.setStyleSheet("background-color: #ffb6c1;")  # Rojo claro
        clear_button.clicked.connect(self.clear_fields)
        layout.addWidget(clear_button)

        self.setLayout(layout)

    def predict(self):
        # Obtener valores de entrada del usuario
        input_data = [float(self.input_fields[feature].text()) for feature in features.columns]
        input_data = np.array(input_data).reshape(1, -1)

        # Realizar la predicción
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            result_text = "Eres propenso a tener un infarto."
        else:
            result_text = "No eres propenso a tener un infarto."

        self.result_text.setPlainText(result_text)

    def clear_fields(self):
        for input_field in self.input_fields.values():
            input_field.clear()
        self.result_text.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')  # Establecer el estilo de la aplicación a Fusion
    window = InfartoApp()
    window.show()
    sys.exit(app.exec_())

