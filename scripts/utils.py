import logging
import sys
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parents[1]

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from config.config import LOG_FILE_PATH


def setup_logging():

    logging.basicConfig(
        filename=LOG_FILE_PATH,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
