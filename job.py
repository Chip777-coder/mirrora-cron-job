import requests

def run_alert():
    response = requests.post("https://your-api-url.com/trigger-decision")
    print("Alert Triggered:", response.status_code, response.text)

if __name__ == "__main__":
    run_alert()
