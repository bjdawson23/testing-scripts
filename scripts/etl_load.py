import sqlite3
import pandas as pd
import pathlib
import logging

# Configure a basic logger
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Constants
DW_DIR = pathlib.Path("data").joinpath("dw")
DB_PATH = DW_DIR.joinpath("smart_sales.db")
CLEANED_DATA_PATH = pathlib.Path("data").joinpath("prepared", "WM_Transactions_cleaned.csv")

def extract_data(file_path: pathlib.Path) -> pd.DataFrame:
    """Extract data from the cleaned CSV file."""
    try:
        logger.info(f"Extracting data from {file_path}...")
        data = pd.read_csv(file_path)
        logger.info("Data extraction complete.")
        return data
    except Exception as e:
        logger.error(f"Error extracting data: {e}")
        raise

def transform_data(data: pd.DataFrame) -> dict:
    """Transform the data into fact and dimension tables."""
    logger.info("Transforming data...")

    # Remove leading/trailing spaces in column names
    data.columns = data.columns.str.strip()

    # Create dimension tables
    dim_products = data[['product_id']].drop_duplicates().rename(columns={'product_id': 'product_id'})
    dim_customers = data[['cust_id']].drop_duplicates().rename(columns={'cust_id': 'cust_id'})
    dim_date = data[['purchase_date', 'glyear', 'week', 'glperiod']].drop_duplicates().rename(
        columns={'purchase_date': 'date_id'}
    )
    dim_branches = data[['selling_branch']].drop_duplicates().rename(columns={'selling_branch': 'branch_id'})

    # Create fact table
    fact_transactions = data[['trans_id', 'product_id', 'cust_id', 'purchase_date', 'selling_branch', 'tons']]

    logger.info("Data transformation complete.")
    return {
        "dim_products": dim_products,
        "dim_customers": dim_customers,
        "dim_date": dim_date,
        "dim_branches": dim_branches,
        "fact_transactions": fact_transactions
    }

def load_data(tables: dict, db_path: pathlib.Path) -> None:
    """Load the transformed data into the SQLite database."""
    try:
        logger.info(f"Loading data into the database at {db_path}...")
        conn = sqlite3.connect(db_path)

        # Load each table into the database
        for table_name, df in tables.items():
            logger.info(f"Loading table: {table_name}...")
            df.to_sql(table_name, conn, if_exists='replace', index=False)

        conn.commit()
        logger.info("Data loading complete.")
    except Exception as e:
        logger.error(f"Error loading data: {e}")
        raise
    finally:
        if conn:
            conn.close()

def main() -> None:
    """Main ETL process."""
    logger.info("Starting ETL process...")

    # Step 1: Extract
    data = extract_data(CLEANED_DATA_PATH)

    # Step 2: Transform
    tables = transform_data(data)

    # Step 3: Load
    load_data(tables, DB_PATH)

    logger.info("ETL process complete.")

if __name__ == "__main__":
    main()