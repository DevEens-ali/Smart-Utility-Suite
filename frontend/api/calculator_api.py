import requests

BASE_URL = "http://127.0.0.1:8000"


def calculate_basic(num1, num2, operation):
    url = f"{BASE_URL}/calculator/calculate"

    payload = {
        "num1": num1,
        "num2": num2,
        "operation": operation,
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        return {
            "error": str(e)
        }