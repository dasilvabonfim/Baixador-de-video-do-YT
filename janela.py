import download as Downloader
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QGridLayout, QHBoxLayout,QLabel
from PySide6.QtCore import Qt

app = QApplication()

window = QWidget()
window.setWindowTitle("Baixador de vídeo do youtube MP4 ou MP3")

link = QLineEdit()
link.setPlaceholderText("Digite o link do vídeo: ")
link.setStyleSheet("background-color: #fff; color: #000;border-radius: 5px;")
link.setFixedHeight(50)

mp4_button = QPushButton("Download MP4")
mp3_button = QPushButton("Download MP3")
mp4_button.setStyleSheet("background: #808080;color: #ffffff; border-radius: 5px;")
mp3_button.setStyleSheet("background: #808080;color: #ffffff; border-radius: 5px")
mp4_button.setFixedHeight(50)
mp3_button.setFixedHeight(50)

texto = QLabel()
texto.setText("Erro ao baixar o vídeo")
texto.setAlignment(Qt.AlignCenter)
texto.setVisible(False)
texto.setStyleSheet("background: #000;color: #ffffff;;border-radius: 5px;")
texto.setFixedHeight(40)


def mp4():
    try:
        URL = link.text()
        Downloader.downloadmp4(URL)
        texto.setVisible(False)  
    except:
        texto.setVisible(True) 

def mp3():
    try:
        URL = link.text()
        Downloader.downloadmp3(URL)
        texto.setVisible(False)
    except:
        texto.setVisible(True)


mp4_button.clicked.connect(mp4)
mp3_button.clicked.connect(mp3)

layout = QGridLayout()

button_layout = QHBoxLayout()
button_layout.addWidget(mp4_button)
button_layout.addWidget(mp3_button)

layout.addWidget(link, 1, 1)
layout.addLayout(button_layout, 2, 1)

layout.addWidget(texto, 4, 1)

window.setLayout(layout)
window.setStyleSheet("background: qlineargradient(x1:0, y1:0.3, x2:1, y2:1,stop:0 #000080, stop:1 #800080);color: #fff;")

window.setFixedSize(500, 500)
window.show()

app.exec()