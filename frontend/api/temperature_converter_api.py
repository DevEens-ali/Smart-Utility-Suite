import requests


BASE_URL = "http://127.0.0.1:8000"


def convert_temperature(value, from_unit, to_unit):

    url = f"{BASE_URL}/area/convert"

    payload = {
        "value": value,
        "from_unit": from_unit,
        "to_unit": to_unit
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