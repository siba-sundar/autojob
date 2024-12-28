import requests
import time

# Function to fetch proxies from ProxyScrape API
def fetch_proxies():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text.splitlines()
    except requests.exceptions.RequestException as e:
        print("Error fetching proxies:", e)
        return []

# List proxies with refresh every 2 minutes
def list_proxies():
    while True:
        proxies = fetch_proxies()
        print("Fetched proxies:")
        for proxy in proxies:
            print(proxy)
        
        # Wait for 2 minutes before fetching proxies again
        time.sleep(120)

# Run the proxy listing
list_proxies()
