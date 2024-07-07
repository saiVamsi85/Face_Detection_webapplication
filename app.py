from flask import Flask, render_template, request, jsonify
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    try:
        # Path to the face detection script
        script_path = os.path.join(os.getcwd(), 'face_detection.py')
        subprocess.Popen(["python", script_path])
        return jsonify({"message": "Face detection started successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
