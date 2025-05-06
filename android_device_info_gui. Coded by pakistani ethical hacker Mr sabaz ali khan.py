import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading

class AndroidDeviceGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Android Device Info Tool - Ethical Use Only")
        self.root.geometry("600x400")
        
        # Main frame
        self.main_frame = tk.Frame(self.root, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Title label
        tk.Label(self.main_frame, text="Android Device Info Tool", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Output text area
        self.output_text = scrolledtext.ScrolledText(self.main_frame, height=15, width=60, wrap=tk.WORD)
        self.output_text.pack(pady=10)
        
        # Buttons frame
        self.button_frame = tk.Frame(self.main_frame)
        self.button_frame.pack(pady=10)
        
        # Buttons
        tk.Button(self.button_frame, text="Check ADB Devices", command=self.check_devices).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="List Installed Apps", command=self.list_apps).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Get Battery Status", command=self.get_battery).pack(side=tk.LEFT, padx=5)
        tk.Button(self.button_frame, text="Clear Output", command=self.clear_output).pack(side=tk.LEFT, padx=5)
        
        # Disclaimer
        tk.Label(self.main_frame, text="For educational purposes only. Use ethically and with permission.", 
                font=("Arial", 8), fg="red").pack(pady=10)

    def run_adb_command(self, command):
        """Run ADB command and return output."""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=30)
            return result.stdout if result.stdout else result.stderr
        except subprocess.TimeoutExpired:
            return "Error: Command timed out."
        except Exception as e:
            return f"Error: {str(e)}"

    def check_devices(self):
        """Check connected ADB devices."""
        self.output_text.insert(tk.END, "Checking for connected devices...\n")
        threading.Thread(target=self._check_devices_thread, daemon=True).start()

    def _check_devices_thread(self):
        output = self.run_adb_command("adb devices")
        self.output_text.insert(tk.END, output + "\n")
        self.output_text.see(tk.END)

    def list_apps(self):
        """List installed apps on the device."""
        self.output_text.insert(tk.END, "Fetching installed apps...\n")
        threading.Thread(target=self._list_apps_thread, daemon=True).start()

    def _list_apps_thread(self):
        output = self.run_adb_command("adb shell pm list packages")
        self.output_text.insert(tk.END, output + "\n")
        self.output_text.see(tk.END)

    def get_battery(self):
        """Get battery status of the device."""
        self.output_text.insert(tk.END, "Fetching battery status...\n")
        threading.Thread(target=self._get_battery_thread, daemon=True).start()

    def _get_battery_thread(self):
        output = self.run_adb_command("adb shell dumpsys battery")
        self.output_text.insert(tk.END, output + "\n")
        self.output_text.see(tk.END)

    def clear_output(self):
        """Clear the output text area."""
        self.output_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AndroidDeviceGUI(root)
    root.mainloop()