# test_weather.py
import pytest

from .weather import get_temperature

@pytest.mark.ydc
def ydc_get_temperature(mocker):
    mock_get = mocker.patch("my_test.practice.weather.requests.get")
    mock_get.return_value.json.return_value = {"temp": 25}


    result = get_temperature("Tokyo")
    print("\n" + str(result))
    assert result == 25
    # mock_get.assert_called_once_with("https://api.weather.com/Tokyo")