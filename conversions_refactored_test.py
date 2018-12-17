import unittest
from conversions_refactored import *

class TestConversions(unittest.TestCase):
    
    def test_CelsiusToKelvin(self):
        result = round(convert("Celsius","Kelvin",300.00),4)
        self.assertEqual(result, 573.1500)

    def test_CelsiusToFahrenheit(self):
        result = round(convert("Celsius","Fahrenheit",300.00),4)
        self.assertEqual(result, 572.00)

    def test_FahrenheitToCelsius(self):
        result = round(convert("Fahrenheit","Celsius",572.00),4)
        self.assertEqual(result, 300.0000)

    def test_FahrenheitToKelvin(self):
        result = round(convert("Fahrenheit","Kelvin",572.00),4)
        self.assertEqual(result, 573.1500)

    def test_KelvinToCelsius(self):
        result = round(convert("Kelvin","Celsius",573.15),4)
        self.assertEqual(result, 300.0000)

    def test_KelvinToFahrenheit(self):
        result = round(convert("Kelvin","Fahrenheit",573.15),4)
        self.assertEqual(result, 572.0000)

    def test_MilesToMeters(self):
        result = round(convert("Miles","Meters",2.00),4)
        self.assertEqual(result, 3218.6880)

    def test_MilesToYards(self):
        result = round(convert("Miles","Yards",2.00),4)
        self.assertEqual(result, 3520.0000)

    def test_YardsToMiles(self):
        result = round(convert("Yards","Miles",3520.00),4)
        self.assertEqual(result, 2.0000)

    def test_YardsToMeters(self):
        result = round(convert("Yards","Meters",2.00),4)
        self.assertEqual(result, 1.8282)

    def test_MetersToMiles(self):
        result = round(convert("Meters","Miles",2.00),4)
        self.assertEqual(result, 0.0012)

    def test_MetersToYards(self):
        result = round(convert("Meters","Yards",2.00),4)
        self.assertEqual(result, 2.1880)

    def test_SameUnit(self):
        result = round(convert("Yards","Yards",2.00),4)
        self.assertEqual(result, 2.0000)

    def test_ConversionNotPossible(self):
        self.assertRaises(ConversionNotPossible, convert,"Yards","Kelvin",2.00)

if __name__ == '__main__':
    unittest.main()
