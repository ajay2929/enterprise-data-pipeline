```python
import logging
from abc import ABC, abstractmethod
import pandas as pd

# Professional Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DataTransformer(ABC):
    """Abstract Base Class to ensure all transformers follow the same contract."""
    @abstractmethod
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        pass

class FinanceDataTransformer(DataTransformer):
    """Specific logic for cleaning financial records."""
    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        logger.info("Cleaning Financial Data...")
        # Remove nulls and format currency
        df = df.dropna(subset=['transaction_id'])
        df['amount'] = df['amount'].round(2)
        return df

class ETLEngine:
    """The main engine that orchestrates the Extract, Transform, Load flow."""
    def __init__(self, transformer: DataTransformer):
        self.transformer = transformer

    def run(self, raw_data: pd.DataFrame):
        try:
            logger.info("Starting ETL Job...")
            # 1. Transform
            clean_data = self.transformer.transform(raw_data)
            
            # 2. Load (Simulated)
            logger.info(f"Loading {len(clean_data)} rows into Cloud Warehouse.")
            return True
        except Exception as e:
            logger.error(f"Pipeline Failed: {str(e)}")
            return False

if __name__ == "__main__":
    # Simulated Raw Data
    data = pd.DataFrame({
        'transaction_id': [1, 2, None],
        'amount': [100.555, 200.1, 50.0]
    })
    
    # Initialize with specialized logic
    finance_logic = FinanceDataTransformer()
    etl = ETLEngine(finance_logic)
    etl.run(data)
