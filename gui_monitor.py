import tkinter as tk
from tkinter import scrolledtext, messagebox
from pynput import keyboard
import threading
import logging
import os

# --- Configuration ---
LOG_FILE = "app_log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.DEBUG, format='%(asctime)s: %(message)s')

class MonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Secure Endpoint Monitor (DLP Version)")
        self.root.geometry("400x350")
        self.root.resizable(False, False)

        self.listener = None
        self.is_running = False

        # --- UI Elements ---
        
        # Title
        self.label_title = tk.Label(root, text="Endpoint Activity Monitor", font=("Arial", 14, "bold"))
        self.label_title.pack(pady=10)

        # Status Indicator
        self.status_var = tk.StringVar()
        self.status_var.set("Status: STOPPED")
        self.lbl_status = tk.Label(root, textvariable=self.status_var, fg="red", font=("Arial", 10))
        self.lbl_status.pack(pady=5)

        # Buttons Frame
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        self.btn_start = tk.Button(btn_frame, text="Start Monitoring", bg="green", fg="white", width=15, command=self.start_logging)
        self.btn_start.pack(side=tk.LEFT, padx=10)

        self.btn_stop = tk.Button(btn_frame, text="Stop Monitoring", bg="red", fg="white", width=15, state=tk.DISABLED, command=self.stop_logging)
        self.btn_stop.pack(side=tk.LEFT, padx=10)

        # Analysis Area (The "GenAI" Feature)
        self.btn_analyze = tk.Button(root, text="Run Threat Analysis (DLP)", width=30, command=self.run_analysis)
        self.btn_analyze.pack(pady=10)

        self.txt_output = scrolledtext.ScrolledText(root, height=8, width=45)
        self.txt_output.pack(pady=5)

    # --- Logic ---

    def on_press(self, key):
        try:
            logging.info(str(key.char))
        except AttributeError:
            logging.info(str(key))

    def start_logging(self):
        if not self.is_running:
            self.is_running = True
            self.listener = keyboard.Listener(on_press=self.on_press)
            # We must start the listener in a separate thread, or the GUI will freeze!
            self.listener.start()
            
            # Update UI
            self.status_var.set("Status: RUNNING (Recording...)")
            self.lbl_status.config(fg="green")
            self.btn_start.config(state=tk.DISABLED)
            self.btn_stop.config(state=tk.NORMAL)

    def stop_logging(self):
        if self.is_running and self.listener:
            self.listener.stop()
            self.is_running = False
            
            # Update UI
            self.status_var.set("Status: STOPPED")
            self.lbl_status.config(fg="red")
            self.btn_start.config(state=tk.NORMAL)
            self.btn_stop.config(state=tk.DISABLED)

    def run_analysis(self):
        # This simulates the "GenAI" analysis logic
        suspicious_keywords = ['password', 'login', 'bank', 'credit', 'admin']
        self.txt_output.delete(1.0, tk.END) # Clear previous text
        
        if not os.path.exists(LOG_FILE):
            self.txt_output.insert(tk.END, "Error: No log file found. Start monitoring first.\n")
            return

        self.txt_output.insert(tk.END, "--- Scanning Logs for Threats ---\n")
        
        try:
            with open(LOG_FILE, 'r') as f:
                content = f.read()
                found = False
                for word in suspicious_keywords:
                    if word in content:
                        self.txt_output.insert(tk.END, f"⚠️ ALERT: Found keyword '{word}'\n")
                        found = True
                
                if not found:
                    self.txt_output.insert(tk.END, "✅ No immediate threats detected.\n")
        except Exception as e:
            self.txt_output.insert(tk.END, f"Error reading file: {e}")

# --- Main Loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = MonitorApp(root)
    root.mainloop()