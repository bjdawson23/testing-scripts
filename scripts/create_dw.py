import sqlite3
import sys
import pathlib

# For local imports, temporarily add project root to Python sys.path
PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

# Now we can import local modules
from utils.logger import logger  # noqa: E402

# Constants
DW_DIR: pathlib.Path = pathlib.Path("data").joinpath("dw")
DB_PATH: pathlib.Path = DW_DIR.joinpath("smart_sales.db")

# Ensure the 'data/dw' directory exists
DW_DIR.mkdir(parents=True, exist_ok=True)


def create_dw() -> None:
    """Create the data warehouse by creating fact and dimension tables."""
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Create dimension tables
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_products (
            product_id TEXT PRIMARY KEY,
            product_name TEXT,
            category TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_customers (
            cust_id TEXT PRIMARY KEY,
            customer_name TEXT,
            region TEXT
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_date (
            date_id TEXT PRIMARY KEY,
            glyear INTEGER,
            week INTEGER,
            glperiod INTEGER
        );
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS dim_branches (
            branch_id TEXT PRIMARY KEY,
            branch_name TEXT,
            location TEXT
        );
        """)

        # Create fact table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS fact_transactions (
            trans_id INTEGER PRIMARY KEY,
            product_id TEXT,
            cust_id TEXT,
            purchase_date TEXT,
            selling_branch TEXT,
            tons REAL,
            FOREIGN KEY (product_id) REFERENCES dim_products(product_id),
            FOREIGN KEY (cust_id) REFERENCES dim_customers(cust_id),
            FOREIGN KEY (purchase_date) REFERENCES dim_date(date_id),
            FOREIGN KEY (selling_branch) REFERENCES dim_branches(branch_id)
        );
        """)

        # Commit changes and close the connection
        conn.commit()
        logger.info("Data warehouse created successfully.")

    except sqlite3.Error as e:
        logger.error(f"Error connecting to the database: {e}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
    finally:
        if conn:
            conn.close()

def main() -> None:
    """Main function to create the data warehouse."""
    logger.info("Starting data warehouse creation...")
    create_dw()
    logger.info("Data warehouse creation complete.")

if __name__ == "__main__":
    main()
