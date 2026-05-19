import pandas as pd
import numpy as np
import unidecode
import logging


def clean_column_names(df):

    logging.info('Cleaning column names')

    df.columns = [
        unidecode.unidecode(str(col))
        .lower()
        .replace(' ', '_')
        .replace('(', '')
        .replace(')', '')
        for col in df.columns
    ]

    return df


def remove_duplicates(df):

    logging.info('Removing duplicates')

    return df.drop_duplicates()


def handle_data_types(df):

    logging.info('Handling data types')

    # IMEI

    if 'imei' in df.columns:

        df['imei'] = df['imei'].astype(str)

    # LIMIT

    if 'data_limit_gb' in df.columns:

        df['data_limit_gb'] = (
            df['data_limit_gb']
            .replace('Nielimitowane', np.nan)
        )

        df['data_limit_gb'] = pd.to_numeric(
            df['data_limit_gb'],
            errors='coerce'
        )

    # USAGE

    if 'data_usage_gb' in df.columns:

        df['data_usage_gb'] = pd.to_numeric(
            df['data_usage_gb'],
            errors='coerce'
        )

    # COST

    if 'monthly_cost' in df.columns:

        df['monthly_cost'] = pd.to_numeric(
            df['monthly_cost'],
            errors='coerce'
        )

    return df


def create_kpi(df):

    logging.info('Creating KPI columns')

    if (
        'data_usage_gb' in df.columns and
        'data_limit_gb' in df.columns
    ):

        df['usage_percent'] = np.where(
            df['data_limit_gb'].isna(),
            np.nan,
            (
                df['data_usage_gb']
                / df['data_limit_gb']
            ) * 100
        )

    return df