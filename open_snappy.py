import pandas as pd

# Replace with your actual file name
file_path = "veridion_entity_resolution_challenge.snappy.parquet"

# Read the Parquet file
df = pd.read_parquet(file_path)

# Show the first few rows
print(df.head())

# Optional: Save to CSV
df.to_csv("companies.csv", index=False)
print("CSV saved as 'companies.csv'")
