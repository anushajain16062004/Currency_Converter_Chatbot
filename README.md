Currency Conversion Bot with Dialogflow and Flask
This project demonstrates how to build a currency conversion bot using **Dialogflow** and **Flask**.

Overview
The bot takes user input (source currency, target currency, and amount) and performs currency conversion using the **Currency API**. It responds with the converted amount in the desired currency.

How It Works
- The Flask API is set up to receive POST requests from Dialogflow.
- Dialogflow triggers a POST request to the Flask endpoint when the user asks for currency conversion.
- The Flask server processes the request, calls the Currency API to fetch the conversion rate, performs the calculation, and returns the result to Dialogflow.

Key Features:
- **Dialogflow Integration**: Allows users to interact with the bot using natural language.
- **Currency Conversion**: Fetches real-time conversion rates from the Currency API.
- **Error Handling**: Catches potential errors and sends a user-friendly message.

Requirements
- Flask (`pip install flask`)
- Requests library (`pip install requests`)
- Dialogflow webhook configuration for triggering this Flask server.

How to Run
1. Clone the repository and install the required dependencies.
2. Set up your Dialogflow agent and configure the webhook to point to your Flask API.
3. Run the Flask app with `python app.py`.
4. Test the currency conversion functionality by interacting with the Dialogflow agent.

API Used
- **Currency API**: Provides live exchange rates for multiple currencies.


<img width="548" alt="Screenshot 2024-12-05 204521" src="https://github.com/user-attachments/assets/b9a6bc2d-5e01-4f24-9d2a-ffa327654489">

