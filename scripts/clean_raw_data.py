import os
import pandas as pd

def clean_data(input_file, output_file):
    """
    Cleans raw data from a CSV file and saves the cleaned data to a new file.
    
    Args:
        input_file (str): Path to the raw data CSV file.
        output_file (str): Path to save the cleaned data CSV file.
    """
    try:
        # Load the raw data
        print(f"Loading raw data from {input_file}...")
        data = pd.read_csv(input_file)
        
        # Drop duplicate rows
        print("Removing duplicate rows...")
        data = data.drop_duplicates()
        
        # Handle missing values (e.g., fill with mean for numeric columns)
        print("Handling missing values...")
        for column in data.select_dtypes(include=['float64', 'int64']).columns:
            data[column] = data[column].fillna(data[column].mean())
        
        # Standardize column names (e.g., lowercase and replace spaces with underscores)
        print("Standardizing column names...")
        data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Save the cleaned data
        print(f"Saving cleaned data to {output_file}...")
        os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure the output directory exists
        data.to_csv(output_file, index=False)
        
        print(f"Data cleaning complete. Cleaned data saved to {output_file}")
    except Exception as e:
        print(f"An error occurred while cleaning {input_file}: {e}")

if __name__ == "__main__":
    # Define input and output directories
    input_dir = os.path.join("data", "raw")  # Use os.path.join for cross-platform compatibility
    output_dir = os.path.join("data", "prepared")
    
    # Ensure the input directory exists
    if not os.path.exists(input_dir):
        print(f"Error: Input directory '{input_dir}' does not exist.")
    else:
        # Process all CSV files in the input directory
        for file_name in os.listdir(input_dir):
            if file_name.endswith(".csv"):
                input_file = os.path.join(input_dir, file_name)
                output_file = os.path.join(output_dir, file_name.replace(".csv", "_cleaned.csv"))
                
                # Clean the data
                clean_data(input_file, output_file)