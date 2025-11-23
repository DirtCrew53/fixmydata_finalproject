import pandas as pd
import numpy as np

class OutlierDetector:
    def __init__(self, data):
        """
        Initialize with a pandas DataFrame
        :param data: pandas DataFrame
        """
        self._data = data  # Private attribute

    def z_score_outliers(self, threshold=3):
        """
        Detects outliers using Z-score method.
        :param threshold: Z-score value to detect outliers
        """
        z_scores = np.abs((self._data - self._data.mean()) / self._data.std())
        return self._data[(z_scores < threshold).all(axis=1)]

    def iqr_outliers(self):
        """
        Detects outliers using the IQR method.
        """
        Q1 = self._data.quantile(0.25)
        Q3 = self._data.quantile(0.75)
        IQR = Q3 - Q1
        return self._data[~((self._data < (Q1 - 1.5 * IQR)) | (self._data > (Q3 + 1.5 * IQR))).any(axis=1)]

