import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
import random


class Roll(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def createInputLabel(self, text):
        label = QLabel(text)
        self.layout.addWidget(label)

    def createLineEdit(self):
        line_edit = QLineEdit()
        self.layout.addWidget(line_edit)
        return line_edit
    def setupUI(self):
        self.setWindowTitle('программа для бросания кубиков')
        self.setGeometry(200, 200, 300, 300)

        self.layout = QVBoxLayout()

        self.createInputLabel('Кол-во кубиков:')
        self.num_dice_input = self.createLineEdit()
        self.createInputLabel('Кол-во бросков:')
        self.num_rolls_input = self.createLineEdit()

        self.simulate_button = QPushButton('Начать')
        self.simulate_button.clicked.connect(self.performDiceRoll)
        self.layout.addWidget(self.simulate_button)

        self.result_label = QLabel('')
        self.layout.addWidget(self.result_label)

        self.setLayout(self.layout)

        self.num_dice_input.textChanged.connect(self.validateInput)
        self.num_rolls_input.textChanged.connect(self.validateInput)
    def validateInput(self):
        sender = self.sender()
        if sender.text() and not sender.text().isdigit():
            sender.clear()
            self.showWarningMessage("Нужно вводить только цифры.")

    def showWarningMessage(self, text):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setText(text)
        msg.setWindowTitle("Ошибка , неправильный ввод")
        msg.exec()

    def performDiceRoll(self):
        num_dice = int(self.num_dice_input.text())
        num_rolls = int(self.num_rolls_input.text())

        results = {}
        for _ in range(num_rolls):
            total = sum(random.randint(1, 6) for _ in range(num_dice))
            results[total] = results.get(total, 0) + 1

        output = ''
        for key in sorted(results.keys()):
            percentage = (results[key] / num_rolls) * 100
            output += f"Сумма {key}: {percentage:.2f}%\n"

        self.result_label.setText(output)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    simulator = Roll()
    simulator.show()
    sys.exit(app.exec())