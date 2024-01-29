from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def handle_requests():
    if request.method == 'POST':
        # Run stress_cpu.py in a separate process
        subprocess.Popen(['python3', 'stress_cpu.py'])
        return 'Stress CPU process started successfully'
    elif request.method == 'GET':
        # Get private IP address of the EC2 instance
        private_ip = socket.gethostbyname(socket.gethostname())
        return private_ip

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)