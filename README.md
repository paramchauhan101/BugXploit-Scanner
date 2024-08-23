# BugXploit

BugXploit is a powerful tool designed for various security assessments, including network scanning, web vulnerability scanning, and security header analysis. It integrates multiple functionalities into a single, user-friendly application, allowing for efficient and real-time security checks.

## Features

- **Basic Nmap Scan**: Quickly scan a network to identify open ports and services.
- **Nikto Scan**: Conduct a thorough web vulnerability scan to uncover potential issues on web servers.
- **Security Header Scan**: Analyze the security headers of a website to ensure proper configurations.
- **Copy Results**: Easily copy scan results to the clipboard.
- **Open BugXploit**: Access BugXploit directly from the application.

## Installation

### Prerequisites

- Python 3.10 or higher
- Administrative privileges (for installing system-wide tools)
- PyQt5 library (for the GUI)
- Nmap (for network scanning)
- Nikto (for web vulnerability scanning)

### Installation on Linux

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/paramchauhan101/BugXploit.git
    cd BugXploit
    ```

2. **Install Dependencies:**

    Ensure you have `PyQt5`, `nmap`, and `nikto` installed. You can install `PyQt5` using `pip`:

    ```bash
    pip install PyQt5
    ```

    Install `nmap` and `nikto` using your package manager, such as `apt` on Debian-based systems:

    ```bash
    sudo apt-get update
    sudo apt-get install nmap nikto
    ```

3. **Run the Application:**

    Execute the script to launch the application:

    ```bash
    python3 bug_xploit.py
    ```

## Usage

1. **Launch BugXploit**: Run the application using the command above.
2. **Enter Target**: Input the target IP address or hostname in the provided text field.
3. **Choose Scan Type**: Select the type of scan you wish to perform (Port Scan, Vulnerability Scan, or Security Header Scan) by clicking the corresponding button.
4. **View Results**: Results will be displayed in the output area in real-time.
5. **Copy Results**: Click the "Copy Results" button to copy the scan output to your clipboard.
6. **Open BugXploit**: Click the "Open BugXploit" button to visit the BugXploit website.

## Contribution

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request on GitHub.

## License

This project is licensed under the GNU General Public License (GPL) v3.0 - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact Param Chauhan at [cloudparam75@gmail.com](mailto:cloudparam75@gmail.com).
