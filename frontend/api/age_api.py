import requests

BASE_URL = "http://127.0.0.1:8000"


def calculate_age(date_of_birth):

    url = f"{BASE_URL}/age/calculate"

    payload = {
        "date_of_birth": date_of_birth
    }

    try:
        response = requests.post(
            url,
            json=payload,
        )
        response.raise_for_status()

        return response.json()

    except requests.RequestException as e:
        return {
            "error": str(e)
        }