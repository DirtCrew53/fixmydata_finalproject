import pandas as pd

class DataValidator:
    def __init__(self, data):
        """
        Initialize with a pandas DataFrame
        :param data: pandas DataFrame
        """
        self._data = data  # Private attribute

    def validate_range(self, column, min_val, max_val):
        """
        Ensures the values in a column are within a specified range.
        :param column: Column name to validate
        :param min_val: Minimum acceptable value
        :param max_val: Maximum acceptable value
        """
        if not self._data[column].between(min_val, max_val).all():
            raise ValueError(f"Values in {column} are out of the specified range.")
        return self._data

    def validate_non_empty(self):
        """Ensures there are no empty columns in the dataset."""
        if self._data.isnull().any().any():
            raise ValueError("Data contains missing values.")
        return self._data

