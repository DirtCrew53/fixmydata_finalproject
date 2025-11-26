import pandas as pd
from fixmydata.data_cleaner import DataCleaner
from fixmydata.outlier_detector import OutlierDetector
from fixmydata.data_validator import DataValidator

# Example data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, None, 30, 28],
    'City': ['NY', 'LA', 'SF', 'NY']
})

# Clean the data
cleaner = DataCleaner(data)
data_cleaned = cleaner.remove_duplicates()
data_cleaned = cleaner.fill_missing(strategy="mean")
data_cleaned = cleaner.standardize_columns()

# Detect outliers
outlier_detector = OutlierDetector(data_cleaned[['Age']])
data_no_outliers = outlier_detector.z_score_outliers()

# Validate data
validator = DataValidator(data_no_outliers)
data_valid = validator.validate_range('Age', 18, 100)

print(data_valid)
