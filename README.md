# Endpoint-Activity-Monitor-DLP
A Python-based endpoint security tool with automated threat detection logic
# Endpoint Activity Monitor with DLP Analysis

## 🛡️ Project Overview
This project is a host-based security tool designed to monitor endpoint activity and detect potential data exfiltration attempts. It features a **Graphical User Interface (GUI)** for control and a **Rule-Based Threat Detection Engine** that simulates basic Data Loss Prevention (DLP) logic.

**Note:** This tool was built for educational purposes to understand user behavior analytics (UBA) and endpoint telemetry.

## 🚀 Features
* **Real-Time Monitoring:** Captures keyboard input streams using `pynput` hooks.
* **DLP Analysis Engine:** automated script that parses logs to identify high-risk keywords (e.g., "password", "confidential", "admin").
* **Stealth Mode Capable:** Can be compiled to run as a background process using PyInstaller.
* **Multi-Threaded GUI:** Built with Tkinter, ensuring the UI remains responsive while the listener runs on a background thread.

## 🛠️ Technology Stack
* **Language:** Python 3.x
* **Libraries:** `tkinter`, `pynput`, `threading`, `logging`
* **DevOps:** PyInstaller (for executable creation)

## ⚙️ How to Run
1.  Clone the repository:
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Endpoint-Activity-Monitor-DLP.git](https://github.com/YOUR_USERNAME/Endpoint-Activity-Monitor-DLP.git)
    ```
2.  Install dependencies:
    ```bash
    pip install pynput
    ```
3.  Run the application:
    ```bash
    python gui_monitor.py
    ```

## ⚠️ Disclaimer
This software is provided for educational use only. Unauthorized monitoring of users without their consent is a violation of privacy laws. The author assumes no liability for misuse.
