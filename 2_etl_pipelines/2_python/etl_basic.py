# Import necessary libraries
import pandas as pd
import os

# Define the path to your dataset in the 02_etl_pipelines/5_data/ folder; Make sure the file name matches exactly with the actual file (case-sensitive)
file_path = os.path.join(os.getcwd(), '2_etl_pipelines', '5_data', 'AmesHousing.csv')

# Print the file path to confirm it's correct
print(f"File path is: {file_path}")

# Step 1: Extract - Load the dataset
def extract_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data loaded successfully.")
        
        # Print the first 10 rows
        print("\nFirst 10 rows of the dataset:")
        print(data.head(10))
        
        # Print the last 10 rows
        print("\nLast 10 rows of the dataset:")
        print(data.tail(10))
        
        return data
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

# Step 2: Transform - Basic data cleaning and aggregation (handle missing values)
def transform_data(data):
    # Handling missing values by filling with mean for numerical columns (example transformation)
    data_cleaned = data.fillna(data.mean())

    # Optionally, add an aggregation step: group by 'MS Zoning' and calculate the average SalePrice
    data_cleaned.rename(columns={"SalePrice": "Final_Sale_Price"}, inplace=True)
    grouped_data = data_cleaned.groupby('MS Zoning').agg({'Final_Sale_Price': 'mean'}).reset_index()
    
    print("\nAggregated data by 'MS Zoning' with average SalePrice:")
    print(grouped_data)

    print("Data transformation completed.")
    return grouped_data

# Step 3: Load - Save the transformed data into a new CSV
def load_data(data, output_path):
    data.to_csv(output_path, index=False)
    print(f"Data successfully saved to {output_path}")

# Running the ETL pipeline
if __name__ == "__main__":
    # Extract data
    ames_df = extract_data(file_path)
    
    if ames_df is not None:
        # Transform data
        transformed_data = transform_data(ames_df)
        
        # Define output path for the transformed data
        output_file_path = os.path.join(os.getcwd(), '2_etl_pipelines', '5_data', 'AmesHousing_transformed.csv')
        
        # Load the transformed data
        load_data(transformed_data, output_file_path)


def my_function ():
    """
    for fututre, may use 'dbt' or 'Fivetran', to expand this simple ETL pipeline by integrating it into a larger workflow in the future.
    """