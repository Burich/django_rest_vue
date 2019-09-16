import requests

def main():
    # 404:
    # response = requests.get("http://www.google.com/1234")
    # 200:
    response = requests.get("http://www.google.com")
    print("Status code: ", response.status_code, response.headers['Content-Type'])

if __name__ == "__main__":
    main()