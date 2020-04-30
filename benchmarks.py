import pandas as pd
import requests
from trading_calendars import get_calendar
from datetime import datetime
import pytz
import logbook

import pandas as pd

log = logbook.Logger(__name__)

def get_benchmark_returns(symbol='SPY'):
    """
    Get a Series of benchmark returns from a file
    Parameters
    ----------
    filelike : str or file-like object
        Path to the benchmark file.
        expected csv file format:
        date,return
        2020-01-02 00:00:00+00:00,0.01
        2020-01-03 00:00:00+00:00,-0.02
    """
    filelike = 'filepath of your personal data/file.csv'
    log.info("Reading benchmark returns from {}", filelike)

    df = pd.read_csv(
        filelike,
        index_col=['time'],
        parse_dates=['time'],
    ).tz_localize('utc')

    if 'adj_close' not in df.columns:
        raise ValueError("The column 'return' not found in the "
                         "benchmark file \n"
                         "Expected benchmark file format :\n"
                         "date, return\n"
                         "2020-01-02 00:00:00+00:00,0.01\n"
                         "2020-01-03 00:00:00+00:00,-0.02\n")

    return df['adj_close'].sort_index().pct_change().iloc[1:]
