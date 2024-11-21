import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QComboBox

class DeviceInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set window properties
        self.setWindowTitle("Device Information App")
        self.setGeometry(100, 100, 400, 300)  # x, y, width, height

        # Main layout
        self.layout = QVBoxLayout(self)

        # Add dropdown menu (QComboBox)
        self.dropdown = QComboBox(self)
        self.dropdown.addItems(self.get_serial_number())
        self.layout.addWidget(self.dropdown)

        # Add info label
        self.info_label = QLabel("Choose an option and click the button.", self)
        self.layout.addWidget(self.info_label)

        # Add button
        self.button = QPushButton("Get Info", self)
        self.button.clicked.connect(self.on_button_click)
        self.layout.addWidget(self.button)

        self.show()

    def on_button_click(self):
        """Handle button click based on dropdown selection."""
        selected_option = self.dropdown.currentText()
        if selected_option == "Device Info":
            self.info_label.setText("Fetching Device Info...")
            sn = self.get_serial_number()
            self.info_label.setText(f"Device Info: Serial Number: {sn}")
        elif selected_option == "Serial Number":
            self.info_label.setText("Fetching Serial Number...")
            sn = self.get_serial_number()
            self.info_label.setText(f"Serial Number: {sn}")
        elif selected_option in  self.get_serial_number():
            self.info_label.setText("Fetching Serial Number...")
            sn = self.get_serial_number()
            self.info_label.setText(f"Serial Number: {sn}")
        else:
            QMessageBox.information(self, "Info", "Please select a valid option.")

    def get_serial_number(self):
        """Fetch the serial number using WMIC command."""
        try:
            deviceslist = []
            device = os.popen("adb devices").readlines()
            print(len(device))
            for i in range(1, len(device) - 1):
                deviceslist.append(device[i].split()[0])
            return deviceslist
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeviceInfoApp()
    sys.exit(app.exec_())