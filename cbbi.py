import requests
from datetime import datetime

def get_bitcoin_price():
    url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1'
    response = requests.get(url)
    data = response.json()
    prices = data['prices']
    opening_price = prices[0][1]
    current_price = prices[-1][1]
    percentage_change = ((current_price - opening_price) / opening_price) * 100
    return current_price, percentage_change

def get_confidence_data():
    url = "https://colintalkscrypto.com/cbbi/data/latest.json"
    user_agent = "curl/8.4.0"
    headers = {"User-Agent": user_agent}
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            confidence_data = data.get("Confidence", {})
            confidence_keys = list(confidence_data.keys())[-7:]
            confidence_values = [confidence_data[key] for key in confidence_keys]
            confidence_values_percentage = [f"{round(value * 100)}%" for value in confidence_values]
            return confidence_values_percentage
        else:
            print("Failed to fetch data. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

confidence_values_percentage = get_confidence_data()
current_price, percentage_change = get_bitcoin_price()

if confidence_values_percentage is not None:
    recommendation = "Buy" if all(float(value.replace('%', '')) < 60 for value in confidence_values_percentage) else "Hold"
    print("Last 7 CBBI values:", ", ".join(confidence_values_percentage))
    print("Current price of Bitcoin: $", round(current_price, 2))
    print("Percentage change since opening: {:.2f}%".format(percentage_change))
    print("Recommendation:", recommendation)
else:
    print("Failed to fetch confidence data.")
