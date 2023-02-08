import pandas as pd
import streamlit as st
from utils import bsevents as bs
from datetime import datetime as dt
from config.conf import bsevents

# дизайн графиков

DATAFRAME_DISPLAY_MAX_SIZE = bsevents.get('DATAFRAME_DISPLAY_MAX_SIZE', 200)
if st.session_state.get('input_update_btn', False):
    df = bs.get_dataframe(cached=False)
else:
    df = bs.get_dataframe()
df = bs.noramlize(df)
initial_df_count = len(df)

########################### USER INPUT ###########################

def input_period(df: pd.DataFrame):
    st.sidebar.header('Период')
    default_value = [bs.get_min_date(df), dt.now()]
    return st.sidebar.date_input(
        'Выберите дату',
        value=default_value,
        min_value=bs.get_min_date(df),
        max_value=dt.now(),
        key='date_range')

def input_clients(df: pd.DataFrame):
    st.sidebar.header('Клиенты')
    return st.sidebar.multiselect('Выберите клиенты', bs.get_client_names(df))

def input_events():
    st.sidebar.header('События')
    succeed_events = st.sidebar.multiselect('Успешные', bs.get_success_events())
    failed_events = st.sidebar.multiselect('Безуспешные', bs.get_fail_events())
    canceled_events = st.sidebar.multiselect('Отмененные', bs.get_cancel_events())
    return succeed_events, failed_events, canceled_events

########################### CONTENT ###########################

def color_type(event_type):
    if event_type in bs.get_success_events():
        return 'background-color: rgba(40, 167, 69, 0.4)'
    elif event_type in bs.get_fail_events():
        return 'background-color: rgba(220, 53, 69, 0.4)'
    elif event_type in bs.get_cancel_events():
        return 'background-color: rgba(255, 193, 7, 0.4)'
    else:
        return ''

df = bs.filter_by_dates(df, *input_period(df))
df = bs.filter_by_clients(df, input_clients(df))
selected_succ_evns, selected_fail_evns, selected_canc_evns = input_events()
df = bs.filter_by_events(df,
    [*selected_succ_evns, *selected_fail_evns, *selected_canc_evns])

st.title('BsEvents stat')
st.header('Датасет')
st.button('🔃 Обновить данные', key='input_update_btn')
st.empty()
st.dataframe(df.head(DATAFRAME_DISPLAY_MAX_SIZE).style.applymap(color_type, subset=['event']))
if len(df) > DATAFRAME_DISPLAY_MAX_SIZE:
    dataframe_caption = (f'Отображено записей {DATAFRAME_DISPLAY_MAX_SIZE} из {len(df)}')
else:
    dataframe_caption = (f'Отображено {len(df)} записей')
st.caption(f'{dataframe_caption}. Всего в базе данных {initial_df_count}.')
st.download_button('⬇️ Скачать таблицу ⬇️', df.to_csv(), 'bsevents.csv')

st.header('Кто сколько пульнул событий')
st.bar_chart(bs.get_common_info(df))

st.header('График статусов событий (все клиенты)')
st.bar_chart(bs.get_all_client_info(df))

st.title('Графики по каждому клиенту')
for client in bs.get_client_names(df):
    st.subheader(f'Клиент: {client}')
    client_info = bs.get_client_info(df, client)
    if client_info.count() == 1:
        st.bar_chart(client_info, width=300, use_container_width=False)
    else:
        st.bar_chart(client_info)
