from extract import extract_excel

from transform import (
    clean_column_names,
    remove_duplicates,
    handle_data_types,
    create_kpi
)

from validation import validate_dataframe

from load import (
    save_raw_table,
    save_employees,
    save_devices,
    save_tariff,
    save_fact_table
)

from utils import setup_logging

import logging


# =========================
# SETUP LOGGING
# =========================

setup_logging()

logging.info('ETL started')


# =========================
# EXTRACT
# =========================

df = extract_excel()


# =========================
# TRANSFORM
# =========================

df = clean_column_names(df)

df = remove_duplicates(df)

df = handle_data_types(df)

df = create_kpi(df)


# =========================
# VALIDATION
# =========================

validate_dataframe(df)


# =========================
# LOAD
# =========================

save_raw_table(df)

save_employees(df)

save_devices(df)

save_tariff(df)

save_fact_table(df)


# =========================
# FINISH
# =========================

logging.info('ETL completed successfully')

print('ETL completed successfully')
