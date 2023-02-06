import time
import pandas as pd

def read_pickle():
    start = time.time()
    pd.read_pickle('datasets/bregis.bsevents.pickle')
    print(f'Считывание датасета pickle (сек): {time.time() - start}')

def read_json():
    start = time.time()
    pd.read_json("datasets/bregis.bsevents.json")
    print(f'Считывание датасета json (сек): {time.time() - start}')

read_pickle()
read_json()