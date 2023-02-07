import pandas as pd
from datetime import datetime as dt
from datetime import date
from typing import List, Union


JSON_DATASET_PATH = 'datasets/bregis.bsevents.json'

_dataframe: Union[pd.DataFrame, None] = None
def get_dataframe(cached: bool = True):
    global _dataframe
    if _dataframe is None or not cached:
        print('reading dataframe')
        _dataframe = pd.read_json(JSON_DATASET_PATH)
    else:
        print('giving cached dataframe')
    return _dataframe.copy()

def noramlize(df: pd.DataFrame) -> pd.DataFrame:
    # this removes unnecessary columns
    # df = df[['event', 'timestamp', 'timestamp_human', 'client']]
    # parse timestamp
    df['timestamp'] = df['timestamp'].apply(
        lambda x: int(x['$date']['$numberLong'])) // 1000
    # add new column
    df['timestamp_human'] = df['timestamp'].apply(
        lambda x: dt.fromtimestamp(x)
    )
    # type optimizations
    df['event'] = df['event'].astype('category')
    df['client'] = df['client'].astype('string')
    return df

def get_common_info(df: pd.DataFrame) -> pd.DataFrame:
    return df['client'].value_counts().to_frame()

def get_all_client_info(df: pd.DataFrame):
    return df['event'].value_counts()

def get_client_names(df: pd.DataFrame):
    return df['client'].unique()

def get_client_info(df: pd.DataFrame, client: str):
    return df.query(f'client == "{client}"')['event'].value_counts()

def get_min_date(df: pd.DataFrame):
    return dt.fromtimestamp(df['timestamp'].min())

def filter_by_dates(df: pd.DataFrame, from_: date, until: date = None):
    if until is None:
        until = dt.now()
    from_ = dt.fromordinal(from_.toordinal()).timestamp()
    until = dt.fromordinal(until.toordinal()).timestamp()
    return df.query(f'timestamp > {from_} & timestamp < {until}')

def filter_by_clients(df: pd.DataFrame, clients: List[str]):
    if clients:
        return df.query(f'client in {clients}')
    return df

def filter_by_events(df: pd.DataFrame, events: List[str]):
    if events:
        return df.query(f'event in {events}')
    return df

def get_success_events():
    return (
        'SAMPLE_DELIVERED', 
        'ORDER_ACCEPTED', 
        'ORDER_DELIVERED', 
        'RESULT_ACCEPTED', 
        'RESULT_DELIVERED')

def get_fail_events():
    return (
        'ORDER_NOT_ACCEPTED',
        'ORDER_NOT_DELIVERED',
        'RESULT_NOT_ACCEPTED',
        'RESULT_NOT_DELIVERED'
    )

def get_cancel_events():
    return ('ORDER_CANCELLED', )

def get_all_events():
    return get_success_events() + get_fail_events() + get_cancel_events()
