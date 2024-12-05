from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def index():
    try:
        # Log the request method (for debugging)
        print(f"Request method: {request.method}")

        # Parse incoming JSON from Dialogflow
        data = request.get_json()
        print("Incoming Request:", data)  # Log incoming data for debugging

        # Extract parameters from the request
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        # Fetch the conversion factor
        cf = fetch_conversion_factor(source_currency, target_currency)

        # Perform conversion
        final_amount = amount * cf
        final_amount = round(final_amount, 2)

        # Prepare the response for Dialogflow
        response = {
            'fulfillmentText': f"{amount} {source_currency} is {final_amount} {target_currency}"
        }

        # Log the response (for debugging)
        print("Response:", response)

        return jsonify(response)

    except Exception as e:
        # Log any errors (for debugging)
        print(f"Error occurred: {e}")
        return jsonify({'fulfillmentText': 'An error occurred while processing your request.'})

# Optional route to handle GET requests with a message (if you want to debug GET method)
@app.route('/', methods=['GET'])
def get_index():
    return "This endpoint is for POST requests only. Use POST to interact with Dialogflow.", 200

# Function to fetch conversion factor from the Currency API
def fetch_conversion_factor(source, target):
    url = f"https://api.currencyapi.com/v3/latest?apikey=cur_live_yLMSrXuxBDfv1JUBvOtNL3U1V6rLxHPby0ucSpJL&base_currency={source}&currencies={target}"

    response = requests.get(url)
    response = response.json()

    # Extract the conversion factor
    if target in response['data']:
        return response['data'][target]['value']
    else:
        raise ValueError("Invalid response or unsupported currency")

if __name__ == "__main__":
    app.run(debug=True)
