import requests
from datetime import datetime

# Current date
current_date = datetime.now()

# Target date
target_date = datetime(2024, 4, 18)

# Calculate the difference in days
days_until_target = (target_date - current_date).days

# URL of the API
url = "https://colintalkscrypto.com/cbbi/data/latest.json"

# Define the user agent
user_agent = "curl/8.4.0"

# Define headers with the user agent
headers = {"User-Agent": user_agent}

# Send a GET request to the API with headers
response = requests.get(url, headers=headers)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Extract the "Confidence" object
    confidence_data = data.get("Confidence", {})

    # Get the keys and values of the "Confidence" object
    confidence_keys = list(confidence_data.keys())[-7:]
    confidence_values = [confidence_data[key] for key in confidence_keys]

    # Check the trend
    trend = "Up" if confidence_values[-1] > confidence_values[0] else "Down"

    # Convert values to percentages in whole numbers with percent sign
    confidence_values_percentage = [f"{round(value * 100)}%" for value in confidence_values]

    print("Estimated days until the Halving:", days_until_target)
    # Print the trend and the last 7 CBBI values as percentages with percent sign
    print("Trend:", trend)
    print("Last 7 CBBI values:", ", ".join(confidence_values_percentage))
else:
    print("Failed to fetch data. Status code:", response.status_code)
