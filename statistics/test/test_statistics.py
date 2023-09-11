import unittest
from unittest.mock import patch
from statistics.statistics import calculate_statistics
class TestCalculateStatistics(unittest.TestCase):

    def test_avg_calculation(self):
        data = [
            ["Country", "Code", "Year", "Rate"],
            ["Country1", "Code1", "2000", "5.0"],
            ["Country1", "Code1", "2001", "6.0"],
            ["Country1", "Code1", "2002", "7.0"],
        ]
        country = "Country1"
        operation = "avg"
        result = calculate_statistics(data, country, operation)
        self.assertAlmostEqual(result, 6.0, places=2)

    def test_min_calculation(self):
        data = [
            ["Country", "Code", "Year", "Rate"],
            ["Country1", "Code1", "2000", "5.0"],
            ["Country1", "Code1", "2001", "6.0"],
            ["Country1", "Code1", "2002", "7.0"],
        ]
        country = "Country1"
        operation = "min"
        result = calculate_statistics(data, country, operation)
        self.assertAlmostEqual(result, 5.0, places=2)

    def test_max_calculation(self):
        data = [
            ["Country", "Code", "Year", "Rate"],
            ["Country1", "Code1", "2000", "5.0"],
            ["Country1", "Code1", "2001", "6.0"],
            ["Country1", "Code1", "2002", "7.0"],
        ]
        country = "Country1"
        operation = "max"
        result = calculate_statistics(data, country, operation)
        self.assertAlmostEqual(result, 7.0, places=2)

    def test_no_data_found(self):
        data = [
            ["Country", "Code", "Year", "Rate"],
            ["Country1", "Code1", "2000", "5.0"],
            ["Country1", "Code1", "2001", "6.0"],
            ["Country1", "Code1", "2002", "7.0"],
        ]
        country = "Country2"
        operation = "avg"
        result = calculate_statistics(data, country, operation)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
