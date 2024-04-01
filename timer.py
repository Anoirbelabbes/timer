from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
import sys
import time

class SecondWindow(QtWidgets.QWidget):
    def __init__(self, work_duration, rest_duration, series_rest_duration, series_number, exercise_duration):
        super().__init__()
        self.work_duration_initial = work_duration * 1000
        self.rest_duration = rest_duration * 1000
        self.series_rest_duration = series_rest_duration * 1000
        self.series_number = series_number
        self.exercise_duration = exercise_duration
        self.current_series = 1
        self.current_exercise = 1
        self.in_work = True
        self.work_duration = self.work_duration_initial
        self.timer = QtCore.QTimer()
        self.setupUi()
        self.player = QMediaPlayer()

        # Ajouter les sons ici
        self.start_sound = QMediaContent(QtCore.QUrl.fromLocalFile("beep.wav/go.wav"))
        self.stop_sound = QMediaContent(QtCore.QUrl.fromLocalFile("stop_sound.wav"))
        self.sound_1 = QMediaContent(QtCore.QUrl.fromLocalFile("beep.wav/1.wav"))
        self.sound_2 = QMediaContent(QtCore.QUrl.fromLocalFile("beep.wav/2.wav"))
        self.sound_3 = QMediaContent(QtCore.QUrl.fromLocalFile("beep.wav/3.wav"))
        self.take_a_rest_sound = QMediaContent(QtCore.QUrl.fromLocalFile("beep.wav/take_a_rest.wav"))



    def setupUi(self):
        self.setWindowTitle("Timer")
        self.resize(400, 500)
        self.setStyleSheet("background-color: #2b2b2b; color: #e0e0e0;")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)

        # Label pour afficher le temps restant
        self.timeLabel = QtWidgets.QLabel("{:.1f}".format(self.work_duration / 1000))
        self.timeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.timeLabel.setFont(QtGui.QFont("Arial", 40, QtGui.QFont.Bold))
        self.timeLabel.setStyleSheet("color: #e0e0e0;")
        self.layout.addWidget(self.timeLabel)

        # Ajouter un widget pour afficher le texte "Temps restant", "Temps de repos" ou "Série terminée"
        self.statusLabel = QtWidgets.QLabel("Temps restant")
        self.statusLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.statusLabel.setFont(QtGui.QFont("Arial", 20, QtGui.QFont.Bold))
        self.statusLabel.setStyleSheet("color: #e0e0e0;")
        self.layout.addWidget(self.statusLabel)

        # Ajouter un widget pour afficher le numéro d'exercice et de série
        self.exerciseSeriesLabel = QtWidgets.QLabel(
            "Exercice: {}/{}  Série: {}/{}".format(self.current_exercise, self.exercise_duration, self.current_series,
                                                   self.series_number))
        self.exerciseSeriesLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.exerciseSeriesLabel.setFont(QtGui.QFont("Arial", 16, QtGui.QFont.Bold))
        self.exerciseSeriesLabel.setStyleSheet("color: #e0e0e0;")
        self.layout.addWidget(self.exerciseSeriesLabel)

        # Bouton Pause/Reprendre
        self.pauseButton = QtWidgets.QPushButton("Pause")
        self.pauseButton.clicked.connect(self.pauseTimer)
        self.pauseButton.setStyleSheet(
            "background-color: #FCDC2A; color: #114232; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;")
        self.layout.addWidget(self.pauseButton)

        # Bouton Réinitialiser
        self.resetButton = QtWidgets.QPushButton("Réinitialiser")
        self.resetButton.clicked.connect(self.resetTimer)
        self.resetButton.setStyleSheet(
            "background-color: #FCDC2A; color: #114232; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;")
        self.layout.addWidget(self.resetButton)

        # Bouton Quitter
        self.quitButton = QtWidgets.QPushButton("Quitter")
        self.quitButton.clicked.connect(self.goToPreviousWindow)
        self.quitButton.setStyleSheet(
            "background-color: #FCDC2A; color: #114232; border: none; padding: 10px 20px; text-align: center; text-decoration: none; display: inline-block; font-size: 16px; margin: 4px 2px; cursor: pointer; border-radius: 8px;")
        self.layout.addWidget(self.quitButton)

        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(100)

    def play_countdown(self):
        """Joue les sons "1.wav", "2.wav" et "3.wav" avant le son "go.wav"."""
        sounds = [self.sound_3, self.sound_2, self.sound_1, self.start_sound]
        for i, sound in enumerate(sounds):
            # Jouer le son
            self.player.setMedia(sound)
            self.player.play()
            # Calculer la durée du son en secondes
            duree = self.player.duration() / 1000
            # Attendre la fin du son
            time.sleep(duree)
            # Ajouter un délai entre les sons
            if i < len(sounds) - 1:
                time.sleep(1)

    def updateTimer(self):
        if self.in_work:
            if self.work_duration > 0:
                self.work_duration -= 100
                self.timeLabel.setText("{:.1f}".format(self.work_duration / 1000))
            else:
                self.in_work = False
                self.current_exercise += 1
                if self.current_exercise > self.exercise_duration:
                    self.current_exercise = 1
                    self.current_series += 1
                    if self.current_series > self.series_number:
                        self.timer.stop()
                        self.timeLabel.setText("Entraînement terminé!")
                        self.statusLabel.setText("")
                    else:
                        self.in_work = False
                        self.work_duration = self.series_rest_duration
                        self.statusLabel.setText("Série terminée. Temps de repos:")
                        self.player.setMedia(self.take_a_rest_sound)
                        self.player.play()
                        QtCore.QTimer.singleShot(1000, self.updateTimer)  # Ajouter une seconde d'attente
                else:
                    self.in_work = False
                    self.work_duration = self.rest_duration
                    self.statusLabel.setText("Temps de repos:")
                    self.player.setMedia(self.take_a_rest_sound)
                    self.player.play()


        else:
            if self.work_duration > 0:
                self.work_duration -= 100
                self.timeLabel.setText("{:.1f}".format(self.work_duration / 1000))
            else:
                self.in_work = True
                self.work_duration = self.work_duration_initial
                self.statusLabel.setText("Temps restant")
                # Jouer le son de démarrage
                self.play_countdown()
                self.exerciseSeriesLabel.setText("Exercice: {}/{}  Série: {}/{}".format(self.current_exercise, self.exercise_duration, self.current_series, self.series_number))

    def pauseTimer(self):
        if self.timer.isActive():
            self.timer.stop()
            self.pauseButton.setText("Reprendre")
        else:
            self.timer.start(100)
            self.pauseButton.setText("Pause")

    def resetTimer(self):
        self.timer.stop()
        self.work_duration = self.work_duration_initial
        self.current_series = 1
        self.current_exercise = 1
        self.in_work = True
        self.timeLabel.setText("{:.1f}".format(self.work_duration / 1000))
        self.statusLabel.setText("Temps restant")
        self.exerciseSeriesLabel.setText("Exercice: {}/{}  Série: {}/{}".format(self.current_exercise, self.exercise_duration, self.current_series, self.series_number))
        self.pauseButton.setText("Pause")
        self.timer.start(100)

    def goToPreviousWindow(self):
        self.timer.stop()
        self.parent().show()
        self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    # Définir un style personnalisé pour l'application
    app.setStyle('Fusion')
    palette = QtGui.QPalette()
    palette.setColor(QtGui.QPalette.Window, QtGui.QColor("#f7f6bb"))
    palette.setColor(QtGui.QPalette.WindowText, QtGui.QColor("#114232"))
    app.setPalette(palette)

    try:
        window = SecondWindow(30, 10, 15, 3, 10)
        window.resize(400, 500)
        window.show()
        sys.exit(app.exec_())
    except Exception as e:
        print("An error occurred:", e)
