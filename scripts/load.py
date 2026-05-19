import logging
import sys
from pathlib import Path
import pandas as pd
from sqlalchemy import create_engine, text


PROJECT_DIR = Path(__file__).resolve().parents[1]

if str(PROJECT_DIR) not in sys.path:
    sys.path.insert(0, str(PROJECT_DIR))

from config.config import (
    DB_USER,
    DB_PASSWORD,
    DB_HOST,
    DB_PORT,
    DB_NAME
)


engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@'
    f'{DB_HOST}:{DB_PORT}/{DB_NAME}'
)

def save_raw_table(df):

    logging.info('Saving RAW table')

    df.to_sql(
        'sim_cards_raw',
        engine,
        if_exists='replace',
        index=False
    )


def save_employees(df):

    logging.info('Saving employees')

    if (
        'employee_name' in df.columns and
        'department' in df.columns
    ):

        employees = (
            df[['employee_name', 'department']]
            .drop_duplicates()
            .reset_index(drop=True)
        )

        with engine.begin() as connection:

            connection.execute(
                text(
                    'TRUNCATE TABLE employees '
                    'RESTART IDENTITY CASCADE'
                )
            )

            employees.to_sql(
                'employees',
                con=connection,
                if_exists='append',
                index=False
            )

def save_devices(df):

    logging.info('Saving devices')

    if (
        'imei' in df.columns and
        'device_type' in df.columns
    ):

        devices = (
            df[['imei', 'device_type']]
            .drop_duplicates()
            .reset_index(drop=True)
        )

        with engine.begin() as connection:

            connection.execute(
                text(
                    'TRUNCATE TABLE devices '
                    'RESTART IDENTITY CASCADE'
                )
            )

            devices.to_sql(
                'devices',
                con=connection,
                if_exists='append',
                index=False
            )


def save_tariff(df):

    logging.info('Saving tariff')

    if 'tariff_plan' in df.columns:

        tariff = (
            df[['tariff_plan']]
            .drop_duplicates()
            .reset_index(drop=True)
        )

        with engine.begin() as connection:

            connection.execute(
                text(
                    'TRUNCATE TABLE tariff '
                    'RESTART IDENTITY CASCADE'
                )
            )

            tariff.to_sql(
                'tariff',
                con=connection,
                if_exists='append',
                index=False
            )


def save_fact_table(df):

    logging.info('Saving fact table')


    # =========================
    # LOAD DIMENSIONS
    # =========================

    employees_sql = pd.read_sql(
        'SELECT * FROM employees',
        engine
    )

    devices_sql = pd.read_sql(
        'SELECT * FROM devices',
        engine
    )

    devices_sql['imei'] = (
        devices_sql['imei'].astype(str)
    )

    tariff_sql = pd.read_sql(
        'SELECT * FROM tariff',
        engine
    )


    # =========================
    # MAP EMPLOYEE IDs
    # =========================

    fact_df = df.merge(
        employees_sql,
        on=['employee_name', 'department'],
        how='left'
    )


    # =========================
    # MAP DEVICE IDs
    # =========================

    fact_df = fact_df.merge(
        devices_sql,
        on=['imei', 'device_type'],
        how='left'
    )


    # =========================
    # MAP TARIFF IDs
    # =========================

    fact_df = fact_df.merge(
        tariff_sql,
        on=['tariff_plan'],
        how='left'
    )


    # =========================
    # BUILD FINAL FACT TABLE
    # =========================

    fact_df = fact_df[[
        'iccid',

        'employee_id',
        'device_id',
        'tariff_id',

        'monthly_cost',

        'data_limit_gb',
        'data_usage_gb',

        'usage_percent',

        'status'
    ]]


    # =========================
    # SAVE FACT TABLE
    # =========================

    with engine.begin() as connection:

        connection.execute(
            text(
                'TRUNCATE TABLE fact_sim_usage '
                'RESTART IDENTITY CASCADE'
            )
        )

        fact_df.to_sql(
            'fact_sim_usage',
            con=connection,
            if_exists='append',
            index=False
        )
