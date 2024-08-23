import sys
import requests
import json
import webbrowser
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QWidget, QTextEdit, QScrollArea, QHBoxLayout
)
from PyQt5.QtGui import QFont, QPalette, QColor, QClipboard
from PyQt5.QtCore import Qt

# Define the expected values for the top 20 security headers
EXPECTED_VALUES = {
    'Strict-Transport-Security': 'max-age=31536000; includeSubDomains',
    'Content-Security-Policy': "default-src 'self';",
    'X-Content-Type-Options': 'nosniff',
    'X-Frame-Options': 'DENY',
    'X-XSS-Protection': '1; mode=block',
    'Referrer-Policy': 'no-referrer',
    'Feature-Policy': "geolocation 'self';",
    'Permissions-Policy': "geolocation=(self), microphone=()",
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Credentials': 'true',
    'X-Permitted-Cross-Domain-Policies': 'none',
    'X-Download-Options': 'noopen',
    'X-DNS-Prefetch-Control': 'off',
    'X-Powered-By': 'hidden',
    'Cache-Control': 'no-store',
    'Pragma': 'no-cache',
    'Expires': '0',
    'Content-Type': 'text/html; charset=utf-8'
}

class HeaderScannerApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Advanced Security Header Scanner")
        self.setGeometry(100, 100, 800, 600)

        # Set up the main layout and widgets
        self.url_input = QLineEdit(self)
        self.url_input.setPlaceholderText("Enter URL (include http:// or https://)")
        self.url_input.setFixedWidth(600)

        self.scan_button = QPushButton("Scan Headers", self)
        self.scan_button.clicked.connect(self.scan_headers)

        self.results_output = QTextEdit(self)
        self.results_output.setReadOnly(True)

        self.copy_button = QPushButton("Copy Results", self)
        self.copy_button.clicked.connect(self.copy_results)

        self.open_link_button = QPushButton("Open BugXploit", self)
        self.open_link_button.clicked.connect(self.open_bugxploit_link)

        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel("URL to scan:"))
        layout.addWidget(self.url_input)
        layout.addWidget(self.scan_button)
        layout.addWidget(QLabel("Scan Results:"))

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.results_output)
        layout.addWidget(scroll_area)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.copy_button)
        button_layout.addWidget(self.open_link_button)
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Style the application
        self.style_application()

    def style_application(self):
        palette = QPalette()
        palette.setColor(QPalette.Background, QColor(0, 0, 0))
        palette.setColor(QPalette.Foreground, QColor(0, 255, 0))
        self.setPalette(palette)

        font = QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.setFont(font)

        self.url_input.setStyleSheet("background-color: #333; color: #0f0; border: 1px solid #0f0;")
        self.scan_button.setStyleSheet("background-color: #555; color: #0f0; border: 1px solid #0f0;")
        self.results_output.setStyleSheet("background-color: #111; color: #0f0; border: 1px solid #0f0;")
        self.copy_button.setStyleSheet("background-color: #555; color: #0f0; border: 1px solid #0f0;")
        self.open_link_button.setStyleSheet("background-color: #555; color: #0f0; border: 1px solid #0f0;")

    def scan_headers(self):
        url = self.url_input.text().strip()
        if not url:
            self.results_output.setPlainText("Please enter a valid URL.")
            return

        results = self.check_security_headers(url)
        self.display_results(url, results)
        self.log_results(url, results)

    def check_security_headers(self, url):
        results = {}
        try:
            response = requests.get(url)
            headers = response.headers

            for header, expected_value in EXPECTED_VALUES.items():
                header_value = headers.get(header, 'Not present')
                if header_value == 'Not present':
                    results[header] = 'Not present'
                elif expected_value.lower() in header_value.lower():
                    results[header] = f"Present (Expected: {expected_value})"
                else:
                    results[header] = f"Present but not as expected (Actual: {header_value})"

        except requests.RequestException as e:
            results['Error'] = str(e)

        return results

    def display_results(self, url, results):
        result_text = f"Results for {url}:\n\n"
        for header, result in results.items():
            result_text += f"{header}: {result}\n"
        self.results_output.setPlainText(result_text)

    def copy_results(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.results_output.toPlainText())

    def open_bugxploit_link(self):
        webbrowser.open("https://www.blackbox.ai/agent/BugXploitB4soaHi")

    def log_results(self, url, results):
        with open('security_header_scan_results.json', 'w') as file:
            json.dump({'url': url, 'results': results}, file, indent=4)
        print("Results have been logged to 'security_header_scan_results.json'.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HeaderScannerApp()
    window.show()
    sys.exit(app.exec_())
