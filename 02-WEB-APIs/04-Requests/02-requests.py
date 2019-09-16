import requests

def main():
    payload = {"base": "RUB", "symbols": "USD,EUR"}
    response = requests.get("https://api.ratesapi.io/api/latest", 
                            params=payload)
    if response.status_code != 200:
        print("Status code: ", response.status_code)
        raise Exception("There was an error")
    
    rates = response.json()['rates']
    for currency in rates:
        print(1, currency, "=", 1/rates[currency], "RUB")

if __name__ == "__main__":
    main()
