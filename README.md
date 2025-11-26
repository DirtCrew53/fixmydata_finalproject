# fixmydata - A Python Library for Data Cleaning

## Overview
**fixmydata** is a Python library designed for cleaning and preprocessing data. It implements essential data cleaning tasks, such as handling missing values, removing duplicates, detecting outliers, and validating dataset quality. The library applies Object-Oriented Programming (OOP) principles to make these tasks modular, reusable, and easy to extend.

### Features:
- **Remove Duplicates**: Easily remove duplicate rows from your data.
- **Fill Missing Values**: Automatically fill missing values using mean, median, or mode.
- **Detect Outliers**: Use statistical methods like Z-score and IQR to detect and remove outliers.
- **Data Validation**: Ensure that data meets certain criteria (e.g., valid ranges, non-empty).
- **Modular OOP Design**: Encapsulation, inheritance, and polymorphism for scalability.

## Installation

You can install the **fixmydata** library from PyPI using pip:

```bash
pip install fixmydata

# Example Usage

import pandas as pd
from fixmydata.data_cleaner import DataCleaner
from fixmydata.outlier_detector import OutlierDetector
from fixmydata.data_validator import DataValidator

# Example DataFrame
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, None, 30, 28],
    'City': ['NY', 'LA', 'SF', 'NY']
})

# Data cleaning
cleaner = DataCleaner(data)
data_cleaned = cleaner.remove_duplicates().fill_missing(strategy="mean").standardize_columns()

# Remove outliers
outlier_detector = OutlierDetector(data_cleaned[['Age']])
data_no_outliers = outlier_detector.z_score_outliers()

# Data validation
validator = DataValidator(data_no_outliers)
validated_data = validator.validate_range('Age', 18, 100)

# Display result
print(validated_data)

