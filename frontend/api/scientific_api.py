import requests

BASE_URL = "http://127.0.0.1:8000"


def calculate_scientific(input_expression):

    url = f"{BASE_URL}/scientific/calculate"

    payload = {
        "input_expression": input_expression
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