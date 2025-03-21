import requests_mock
import pytest
import requests
from utils import historical_data

# Función mockeada
def test_fetch_crypto_data():
    mock_response = {
        "bitcoin": {
            "usd": 63243.275325
        }
    }
    
    # Usando requests-mock para simular la respuesta de la API de CoinGecko
    with requests_mock.Mocker() as m:
        m.get('https://api.coingecko.com/api/v3//coins/bitcoin/history?date=2024-10-01&localization=true', json=mock_response)
        result = historical_data('bitcoin','CG-SiWix6uuyKHPV8sdWZnpHNGZ','2024-10-01','usd')
        assert result == {"price": 63243.275325}