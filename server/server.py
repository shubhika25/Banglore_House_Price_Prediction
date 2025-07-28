from flask import Flask, request, jsonify, send_from_directory
import os
from . import util

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_FOLDER = os.path.join(BASE_DIR, '..', 'client')

app = Flask(__name__, static_folder=CLIENT_FOLDER, static_url_path='')

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()
        location = data['location']
        sqft = float(data['total_sqft'])
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        estimated_price = util.get_estimated_price(location, sqft, bhk, bath)
        return jsonify({'estimated_price': estimated_price})
    except Exception as e:
        app.logger.error(f"Error in prediction: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/')
def serve_index():
    return app.send_static_file('app.html')

if __name__ == '__main__':
    util.load_saved_artifacts()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)  # no debug=True in prod
