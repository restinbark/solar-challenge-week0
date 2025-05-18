import unittest
import pandas as pd
import matplotlib.pyplot as plt
from src import load_data, correlation_analysis_with_line_graphs, wind_speed_direction_analysis, bubble_chart, temperature_analysis, wind_rose_plot

class TestDataAnalysis(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        This method will run once before all tests. It will load the actual dataset.
        """
        # Load the data from the actual file (update the file path as per your setup)
        cls.data = load_data("./10acad/togo-dapaong_qc.csv")  # Replace with your actual dataset file path

    def test_load_data(self):
        # Test loading data function
        data = self.data
        self.assertTrue(isinstance(data, pd.DataFrame))
        self.assertIn('Timestamp', data.columns)  # Check if 'Timestamp' exists

    def test_column_existence(self):
        # Test if columns exist in the data
        self.assertIn('GHI', self.data.columns)
        self.assertIn('DNI', self.data.columns)
        self.assertIn('DHI', self.data.columns)
        self.assertIn('Tamb', self.data.columns)

    def test_data_shape(self):
        # Ensure that the data has the expected shape (number of rows, columns)
        # Adjust the shape as per your actual dataset size
        self.assertGreater(self.data.shape[0], 0)  # Ensure at least one row of data
        self.assertGreater(self.data.shape[1], 0)  # Ensure at least one column of data

    def test_correlation_analysis(self):
        # Test correlation analysis function with actual data
        correlation_analysis_with_line_graphs(self.data, ['GHI', 'DNI', 'DHI', 'Tamb'])
        plt.show()  # We are not mocking this time, so the plot will be generated

    def test_wind_speed_direction_analysis(self):
        # Test wind analysis function
        wind_speed_direction_analysis(self.data, 'GHI', 'DNI')
        plt.show()

    def test_temperature_analysis(self):
        # Test temperature analysis function
        temperature_analysis(self.data, ['GHI', 'DNI', 'DHI', 'Tamb'])
        plt.show()

    def test_bubble_chart(self):
        # Test bubble chart function
        bubble_chart(self.data, x_column='GHI', y_column='DNI', size_column='DHI', color_column='RH')
        plt.show()

    def test_wind_rose_plot(self):
        # Test wind rose plot function
        wind_rose_plot(self.data, 'GHI', 'DNI')
        plt.show()

if __name__ == '__main__':
    unittest.main()