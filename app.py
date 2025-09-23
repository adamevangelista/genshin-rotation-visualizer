from flask import Flask, jsonify, render_template, send_from_directory
import gsim_parser 
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')

app = Flask(__name__, 
            template_folder=TEMPLATE_FOLDER, 
            static_folder=STATIC_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(STATIC_FOLDER, filename)

@app.route('/get_rotation/<filename>')
def get_rotation_data(filename):
    filepath = os.path.join(BASE_DIR, f"{filename}.gsim")
    rotation_sequence = gsim_parser.parse_gsim_file(filepath)
    return jsonify(rotation_sequence)

if __name__ == '__main__':
    print("--- Starting development server on http://127.0.0.1:8080 ---")
    app.run(debug=True, port=8080)

