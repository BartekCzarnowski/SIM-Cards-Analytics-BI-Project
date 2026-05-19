import logging


def validate_dataframe(df):

    logging.info('Validating dataframe')

    required_columns = [
        'employee_name',
        'monthly_cost'
    ]

    missing_columns = [
        col
        for col in required_columns
        if col not in df.columns
    ]

    if missing_columns:

        error_message = (
            f'Missing columns: {missing_columns}'
        )

        logging.error(error_message)

        raise Exception(error_message)

    logging.info('Validation completed')