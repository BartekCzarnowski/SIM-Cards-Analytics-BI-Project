import pandas as pd
import logging
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from config.config import EXCEL_FILE_PATH


def extract_excel():

    try:

        logging.info('Reading Excel file')

        df = pd.read_excel(EXCEL_FILE_PATH)

        logging.info(
            f'Excel loaded successfully: {df.shape[0]} rows'
        )

        return df

    except Exception as e:

        logging.error(f'Error loading Excel: {e}')

        raise
