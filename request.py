import requests

def run_request():
    url = "http://localhost:5000/api"
    r = requests.post(url, json={'exp': 1.8,})
    print(r.json())


if __name__ == '__main__':
    run_request()