from flask import Flask, request, jsonify , send_from_directory
import util

app = Flask(__name__ , static_folder='../client')

@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        data = request.get_json()

        location = data['location']
        sqft = float(data['total_sqft'])
        bhk = int(data['bhk'])
        bath = int(data['bath'])

        response = {
            'estimated_price': util.get_estimated_price(location, sqft, bhk, bath)
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
@app.route('/')
def serve_index():
    return send_from_directory('../client', 'app.html')

@app.route('/app.js')
def serve_js():
    return send_from_directory('../client', 'app.js')

@app.route('/app.css')
def serve_css():
    return send_from_directory('../client', 'app.css')

if __name__ == '__main__':
        util.load_saved_artifacts()
        import os
        port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
        app.run(host='0.0.0.0', port=port)
        app.run(debug=True)
