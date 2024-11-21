import os
import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox


class DeviceInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    '''整个窗口的大小个title信息'''
    def initUI(self):
        # Set window properties
        self.setWindowTitle("Device Information App")
        self.setGeometry(200, 200, 600, 400)  # x, y, width, height

        # Create label
        self.info_label = QLabel("Click the button to get device information.", self)
        self.info_label.move(10, 10)  # Adjust the label's position

        # Create button with specific size and position
        self.button = QPushButton("Get Device Info", self)
        self.button.setGeometry(20, 40, 200, 40)  # x, y, width, height
        self.button.clicked.connect(self.get_device_info)
        self.show()

    def xialatnakuang(self):
        self.ui.comboBox.addItem("pingguo")
        self.ui.comboBox.addItems(["葡萄", "香蕉", "西瓜"])


    def get_device_info(self):
        """Fetch device serial number and display it."""
        try:
            sn = self.get_serial_number()
            if sn:
                self.info_label.setText(f"Device Serial Number: {sn}")
            else:
                QMessageBox.warning(self, "Warning", "Unable to retrieve device serial number.")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    def get_serial_number(self):
        """Use WMIC command to fetch the serial number for Windows devices."""
        try:
            result = os.popen("adb shell getprop ro.serialno")
            lines = result.readlines()
            # print(lines)
            # print(lines[0])
            # print(lines)
            # lines=[0,"demo"]
            # Extract serial number if available
            if len(lines) >= 1:
                return lines[0]
            else:
                return "Not available"
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DeviceInfoApp()
    sys.exit(app.exec_())