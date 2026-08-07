import requests

BASE_URL = "http://127.0.0.1:8000"


def calculate_bmi(height, weight):

    url = f"{BASE_URL}/bmi/calculate"

    payload = {
        "height": height,
        "weight": weight,
    }

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        return {
            "error": str(e)
        }