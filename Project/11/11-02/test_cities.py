import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test city_country() function."""
        expected_result = "Santiago, Chile"
        current_result = city_country("sanTiaGO", "CHile")
        self.assertEqual(current_result, expected_result)

    def test_city_country_population(self):
        """Test city_country() function with optional population."""
        expected_result = "Santiago, Chile - population 5000000"
        current_result = city_country("SANtiAGO", "chile", population=5000000)
        self.assertEqual(current_result, expected_result)


if __name__ == '__main__':
    unittest.main()
