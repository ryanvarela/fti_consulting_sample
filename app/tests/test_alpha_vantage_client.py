import unittest
from unittest.mock import patch
from app.alpha_vantage_client import get_intraday_data

class TestAlphaVantageClient(unittest.TestCase):
    @patch('app.alpha_vantage_client.requests.get')
    def test_get_intraday_data(self, mock_get):
        mock_response = {
            "Time Series (5min)": {
                "2023-07-04 16:00:00": {
                    "1. open": "140.67",
                    "2. high": "141.00",
                    "3. low": "140.56",
                    "4. close": "140.95",
                    "5. volume": "1200"
                }
            }
        }
        mock_get.return_value.json.return_value = mock_response

        data = get_intraday_data("IBM")
        self.assertIn("Time Series (5min)", data)

if __name__ == "__main__":
    unittest.main()
