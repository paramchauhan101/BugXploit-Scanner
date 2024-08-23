import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QTextEdit
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont

class ScanThread(QThread):
    output_signal = pyqtSignal(str)

    def __init__(self, command):
        super().__init__()
        self.command = command

    def run(self):
        process = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
        for line in iter(process.stdout.readline, b''):
            self.output_signal.emit(line.decode('utf-8'))
        process.stdout.close()
        process.wait()

class RealTimeScanner(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Website Scanner")
        self.setGeometry(100, 100, 900, 600)
        self.setStyleSheet("background-color: #000000; color: #00FF00;")

        layout = QVBoxLayout()

        # Title Label
        title_label = QLabel("Website Scanner")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #00FF00; border: 1px solid #00FF00; padding: 10px;")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Target Entry
        input_layout = QHBoxLayout()
        target_label = QLabel("Enter target IP or hostname:")
        target_label.setStyleSheet("font-size: 16px; color: #00FF00;")
        input_layout.addWidget(target_label)

        self.target_entry = QLineEdit()
        self.target_entry.setStyleSheet("""
            background-color: #1e1e1e;
            padding: 8px;
            border-radius: 5px;
            font-size: 14px;
            color: #00FF00;
            border: 1px solid #00FF00;
        """)
        input_layout.addWidget(self.target_entry)

        layout.addLayout(input_layout)

        # Buttons Layout
        buttons_layout = QHBoxLayout()

        nmap_button = QPushButton("Port Scan")
        nmap_button.setStyleSheet(self.get_button_style())
        nmap_button.clicked.connect(self.start_nmap_scan)
        buttons_layout.addWidget(nmap_button)

        nikto_button = QPushButton("Vulnerability Scan")
        nikto_button.setStyleSheet(self.get_button_style())
        nikto_button.clicked.connect(self.start_nikto_scan)
        buttons_layout.addWidget(nikto_button)

        secheader_button = QPushButton("Security Header Scan")
        secheader_button.setStyleSheet(self.get_button_style())
        secheader_button.clicked.connect(self.start_secheader_scan)
        buttons_layout.addWidget(secheader_button)

        layout.addLayout(buttons_layout)

        # Output Area
        self.output_text = QTextEdit()
        self.output_text.setStyleSheet("""
            background-color: #1e1e1e;
            font-family: Courier;
            font-size: 14px;
            color: #00FF00;
            border: 1px solid #00FF00;
        """)
        self.output_text.setReadOnly(True)
        layout.addWidget(self.output_text)

        # Copy Results Button
        copy_button = QPushButton("Copy Results")
        copy_button.setStyleSheet(self.get_button_style())
        copy_button.clicked.connect(self.copy_results)
        layout.addWidget(copy_button)

        # Open BugXploit Button
        open_button = QPushButton("Open BugXploit")
        open_button.setStyleSheet(self.get_button_style())
        open_button.clicked.connect(self.open_bugxploit)
        layout.addWidget(open_button)

        self.setLayout(layout)

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #000000;
                color: #00FF00;
                font-weight: bold;
                padding: 10px;
                border-radius: 8px;
                font-size: 16px;
                border: 2px solid #00FF00;
            }
            QPushButton:hover {
                background-color: #00FF00;
                color: #000000;
            }
        """

    def start_nmap_scan(self):
        command = f"nmap {self.target_entry.text()}"
        self.run_scan(command)

    def start_nikto_scan(self):
        command = f"nikto -h {self.target_entry.text()}"
        self.run_scan(command)

    def start_secheader_scan(self):
        command = f"python3 secheader.py {self.target_entry.text()}"
        self.run_scan(command)

    def run_scan(self, command):
        self.output_text.clear()
        self.thread = ScanThread(command)
        self.thread.output_signal.connect(self.update_output)
        self.thread.start()

    def update_output(self, output):
        self.output_text.append(output)

    def copy_results(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output_text.toPlainText())

    def open_bugxploit(self):
        subprocess.Popen(['xdg-open', 'https://www.blackbox.ai/agent/BugXploitB4soaHi'])

def main():
    app = QApplication(sys.argv)
    scanner = RealTimeScanner()
    scanner.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
