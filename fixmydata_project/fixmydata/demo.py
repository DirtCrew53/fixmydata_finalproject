import pandas as pd
from fixmydata.data_cleaner import DataCleaner
from fixmydata.outlier_detector import OutlierDetector
from fixmydata.data_validator import DataValidator

# Sample data
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', None],
    'Age': [25, None, 25, 30, 22],
    'City': ['NY', 'LA', 'NY', 'SF', 'NY']
})

# DataCleaner usage
cleaner = DataCleaner(data)
cleaned_data = cleaner.remove_duplicates()
cleaned_data = cleaner.fill_missing(strategy="mean")
cleaned_data = cleaner.standardize_columns()

print("Cleaned Data:\n", cleaned_data)

# OutlierDetector usage
outlier_detector = OutlierDetector(data[['Age']])
data_no_outliers = outlier_detector.z_score_outliers(threshold=2)

print("\nData without outliers:\n", data_no_outliers)

# DataValidator usage
validator = DataValidator(cleaned_data)
validated_data = validator.validate_range('Age', 20, 40)

print("\nValidated Data:\n", validated_data)

