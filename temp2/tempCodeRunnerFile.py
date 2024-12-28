import requests

# ProxyScrape API URL to get HTTP proxies
url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"

try:
    # Fetch the proxy list from the API
    response = requests.get(url)
    response.raise_for_status()  # Check if request was successful
    proxies = response.text.splitlines()

    # Display the first 10 proxies for verification
    for proxy in proxies[:10]:
        print(proxy)
except requests.exceptions.RequestException as e:
    print("Error fetching proxies:", e)
