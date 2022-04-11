from pytube import Playlist
import pytube
from PySide2.QtWidgets import *
from ui import Ui_MainWindow
import sys


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('YouTube Video Downloader')
        self.oneVideoButton.clicked.connect(self.downloader)

    def downloader(self):
        url = self.lineEdit_2.text()
        save_path = self.lineEdit.text()

        if self.radioButton.isChecked():
            yt = pytube.YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(save_path)

            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText('Video downloaded!')
            message.exec_()

        elif self.radioButton_2.isChecked():
            # YouTube(url).streams.first().download()
            p = Playlist(url)
            # print(f'Downloading: {p.title}')
            for video in p.videos:
                video.streams.first().download()

                video.streams. \
                    filter(type='video', progressive=True, file_extension='mp4'). \
                    order_by('resolution'). \
                    desc(). \
                    first(). \
                    download(save_path)  # save path here

            message = QMessageBox()
            message.setIcon(QMessageBox.Information)
            message.setText('Playlist downloaded!')
            message.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

# def one_video(link):
#     # link=input('Insert the link: ')
#     yt = pytube.YouTube(link)
#
#     stream = yt.streams.get_highest_resolution()
#     stream.download()


#
# link = input('Insert the Playlist link: ')
# p = Playlist(link)
# print(f'Downloading: {p.title}')
# for video in p.videos:
#     video.streams.first().download()
