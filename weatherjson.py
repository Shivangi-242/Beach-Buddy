from flask import Flask, jsonify
import json

app = Flask(__name__)

# Root route for testing server
@app.route('/')
def home():
    return "Server is running"

# Weather API route
@app.route('/beachbuddy', methods=['GET'])
def get_weather_data():
    try:
        # Load the JSON data from the file
        with open('weather.json') as f:
            jsondata = json.load(f)

        # Check if 'CurrentsDATA' exists in the data
        if 'CurrentsJson' in jsondata:
            currents_json = jsondata['CurrentsJson']
            formatted_data = []

            # Extract each entry in 'CurrentsJson' with safety checks
            for current in currents_json:
                entry = {
                    "District": current.get('District', 'No district specified'),
                    "State": current.get('STATE', 'No state specified'),
                    "Message": current.get('Message', 'No message specified'),
                    "Alert": current.get('Alert', 'No alert'),
                    "Color": current.get('Color', 'No color specified'),
                    "Issue Date": current.get('Issue Date', 'No issue date specified')
                }
                formatted_data.append(entry)
        else:
            formatted_data = []  # Set to an empty list if 'CurrentsDATA' is missing

        # Prepare the response, adding 'LatestCurrentsDate' if available
        response = {
            "LatestCurrentsDate": jsondata.get('LatestCurrentsDate', "No date specified"),
            "CurrentsDATA": formatted_data
        }

        # Return the data as a JSON response
        return jsonify(response)

    except FileNotFoundError as e:
        # Handle file not found error
        return jsonify({"error": f"File not found: {e}"}), 404
    except json.JSONDecodeError as e:
        # Handle JSON parsing error
        return jsonify({"error": f"Invalid JSON format: {e}"}), 400
    except Exception as e:
        # Catch other exceptions
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)