import unittest

from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        """Test city_country() function."""
        expected_result = "Santiago, Chile"
        result = city_country("sanTiaGO", "CHile")
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
