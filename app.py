from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    # Run the face detection script
    subprocess.Popen(["python", "face_detection.py"])
    return "Started", 200

if __name__ == '__main__':
    app.run(debug=True)
