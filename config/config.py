from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[1]

DB_USER = 'postgres'
DB_PASSWORD = '1234'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'sim_db'

EXCEL_FILE_PATH = BASE_DIR / 'data' / 'baza_kart_sim.xlsx'
LOG_FILE_PATH = BASE_DIR / 'logs' / 'etl.log'
