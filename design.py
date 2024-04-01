from PyQt5 import QtCore, QtGui, QtWidgets
from timer import SecondWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 500)
        MainWindow.setStyleSheet("background-color: #2b2b2b; color: #e0e0e0;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")

        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setText("TIMER")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setFont(QtGui.QFont("Arial", 24, QtGui.QFont.Bold))
        self.titleLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.titleLabel)

        self.descriptionLabel = QtWidgets.QLabel(self.centralwidget)
        self.descriptionLabel.setText("Time Tracking App")
        self.descriptionLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionLabel.setFont(QtGui.QFont("Arial", 14))
        self.descriptionLabel.setStyleSheet("color: #cccccc;")
        self.verticalLayout.addWidget(self.descriptionLabel)

        self.trainingLabel = QtWidgets.QLabel(self.centralwidget)
        self.trainingLabel.setText("Type d'entraînement :")
        self.trainingLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.trainingLabel)

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("HIIT")
        self.comboBox.addItem("Entraînement en circuit")
        self.comboBox.addItem("Entraînement en force")
        self.comboBox.addItem("Entraînement en endurance")
        self.comboBox.addItem("Entraînement en flexibilité")
        self.comboBox.setStyleSheet(
            "background-color: #4a4a4a; color: #e0e0e0; border: 1px solid #4a4a4a; border-radius: 4px; padding: 5px;")
        self.verticalLayout.addWidget(self.comboBox)

        self.workDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.workDurationLabel.setText("Durée de travail (par série) :")
        self.workDurationLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.workDurationLabel)

        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setStyleSheet(
            "background-color: #4a4a4a; color: #e0e0e0; border: 1px solid #4a4a4a; border-radius: 4px; padding: 5px;")
        self.verticalLayout.addWidget(self.spinBox)

        self.restDurationLabel = QtWidgets.QLabel(self.centralwidget)
        self.restDurationLabel.setText("Durée de repos entre les exercices:")
        self.restDurationLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.restDurationLabel)

        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_2.setStyleSheet(
            "background-color: #4a4a4a; color: #e0e0e0; border: 1px solid #4a4a4a; border-radius: 4px; padding: 5px;")
        self.verticalLayout.addWidget(self.spinBox_2)

        self.seriesRestLabel = QtWidgets.QLabel(self.centralwidget)
        self.seriesRestLabel.setText("Durée de repos entre les séries :")
        self.seriesRestLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.seriesRestLabel)

        self.spinBox_3 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_3.setObjectName("spinBox_3")
        self.spinBox_3.setStyleSheet(
            "background-color: #4a4a4a; color: #e0e0e0; border: 1px solid #4a4a4a; border-radius: 4px; padding: 5px;")
        self.verticalLayout.addWidget(self.spinBox_3)

        self.seriesNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.seriesNumberLabel.setText("Nombre de séries :")
        self.seriesNumberLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.seriesNumberLabel)

        self.spinBox_4 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_4.setObjectName("spinBox_4")
        self.spinBox_4.setStyleSheet(
            "background-color: #4a4a4a; color: #e0e0e0; border: 1px solid #4a4a4a; border-radius: 4px; padding: 5px;")
        self.verticalLayout.addWidget(self.spinBox_4)

        self.exerciseNumberLabel = QtWidgets.QLabel(self.centralwidget)
        self.exerciseNumberLabel.setText("Nombre d'exercices par série :")
        self.exerciseNumberLabel.setStyleSheet("color: #e0e0e0;")
        self.verticalLayout.addWidget(self.exerciseNumberLabel)

        self.spinBox_5 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_5.setObjectName("spinBox_5")
        self.spinBox_5.setStyleSheet(
            "background-color: #4a4a4a; color: #e0e0e0; border: 1px solid #4a4a4a; border-radius: 4px; padding: 5px;")
        self.verticalLayout.addWidget(self.spinBox_5)

        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setText("Start")
        self.startButton.setStyleSheet(
            "background-color: #FCDC2A; color: #114232; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;")
        self.verticalLayout.addWidget(self.startButton, alignment=QtCore.Qt.AlignCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.comboBox.activated.connect(self.updateDurationValues)

        self.startButton.clicked.connect(self.startButtonClicked)

        self.startButton.setEnabled(False)

        self.default_values = {
            "HIIT": (30, 20, 10, 4, 5),
            "Entraînement en circuit": (45, 30, 15, 3, 3),
            "Entraînement en force": (60, 45, 20, 4, 4),
            "Entraînement en endurance": (90, 60, 30, 5, 5),
            "Entraînement en flexibilité": (20, 15, 10, 2, 4)
        }
        self.current_values = {
            "HIIT": (30, 20, 10, 4, 5),
            "Entraînement en circuit": (45, 30, 15, 3, 3),
            "Entraînement en force": (60, 45, 20, 4, 4),
            "Entraînement en endurance": (90, 60, 30, 5, 5),
            "Entraînement en flexibilité": (20, 15, 10, 2, 4)
        }

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "3"))

    def updateDurationValues(self, index):

        choice = self.comboBox.itemText(index)
        if choice in self.default_values:
            durations = self.default_values[choice]
            self.spinBox.setValue(durations[0])
            self.spinBox_2.setValue(durations[1])
            self.spinBox_3.setValue(durations[2])
            self.spinBox_4.setValue(durations[3])
            self.spinBox_5.setValue(durations[4])


        self.startButton.setEnabled(bool(choice))

    def startButtonClicked(self):

        work_duration = self.spinBox.value()
        rest_duration = self.spinBox_2.value()
        series_rest_duration = self.spinBox_3.value()
        series_number = self.spinBox_4.value()
        exercise_duration = self.spinBox_5.value()
        

        # Passer les valeurs à la deuxième fenêtre
        self.openSecondWindow(work_duration, rest_duration, series_rest_duration, series_number, exercise_duration)

    def openSecondWindow(self, work_duration, rest_duration, series_rest_duration, series_number, exercise_duration):
        # Créer une nouvelle instance de la fenêtre de timer
        self.secondWindow = SecondWindow(work_duration, rest_duration, series_rest_duration, series_number, exercise_duration)
        # Masquer la fenêtre principale
        MainWindow.hide()
        # Afficher la fenêtre du timer
        self.secondWindow.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)


    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#f7f6bb"))
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#114232"))
    app.setPalette(palette)

    MainWindow.show()
    sys.exit(app.exec_())
