import os


bsevents = {
    'DATAFRAME_DISPLAY_MAX_SIZE': 200
}

database = {
    'CONN_STRING': os.getenv('DB_CONN'), # mongodb://...
    'bsevents_collection': 'bregis.bsevents'
}
