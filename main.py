from decouple import config
import requests

# Replace API_KEY and API_SECRET with your own values
API_KEY = config("API_KEY")
API_SECRET = config("API_SECRET")

# API endpoint for getting user profile information
url = "https://kite.trade/connect/login?api_key=" + \
    API_KEY + "&api_secret=" + API_SECRET

response = requests.get(url)

if response.status_code == 200:
    # Successful API request, print the response
    print(response.json())
else:
    # Unsuccessful API request, print the error message
    print("Failed to get user profile with error: " + response.text)
