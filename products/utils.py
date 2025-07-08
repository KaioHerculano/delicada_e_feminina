import requests

def fetch_external_products():
    url = "https://kaioherculano12.pythonanywhere.com/api/v1/products/"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao buscar produtos externos: {e}")
        return []
