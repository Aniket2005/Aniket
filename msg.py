from PyQt5.QtWidgets import QMessageBox

class msg:
    @staticmethod
    def messagebox(text):
        msgg = QMessageBox()
        msgg.setWindowTitle("Information")
        msgg.setIcon(QMessageBox.Information)
        msgg.setText(text)
        msgg.exec()