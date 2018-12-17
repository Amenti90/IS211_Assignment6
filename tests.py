import unittest
from conversions import *

class TestConversions(unittest.TestCase):
    
    def test_CelsiusToKelvin(self):
        result = convertCelsiusToKelvin(300.00)
        self.assertEqual(result, 573.15)

    def test_CelsiusToFahrenheit(self):
        result = convertCelsiusToFahrenheit(300.00)
        self.assertEqual(result, 572.00)

    def test_FahrenheitToCelsius(self):
        result = convertFahrenheitToCelsius(572.00)
        self.assertEqual(result, 300.00)

    def test_FahrenheitToKelvin(self):
        result = convertFahrenheitToKelvin(572.00)
        self.assertEqual(result, 573.15)

    def test_KelvinToCelsius(self):
        result = convertKelvinToCelsius(573.15)
        self.assertEqual(result, 300.00)

    def test_KelvinToFahrenheit(self):
        result = convertKelvinToFahrenheit(573.15)
        self.assertEqual(result, 572.00)

if __name__ == '__main__':
    unittest.main()
