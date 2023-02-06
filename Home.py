import streamlit as st


_, logo, _ = st.columns(3)
logo.image('foxy.png')
st.header('Bregis stat')
st.markdown('Lorem ipsum dolor sit amet consectetur adipisicing elit. Optio aliquam ex rerum, doloribus magnam adipisci facilis fugiat amet dicta libero dolorum. Facere sint dolorum maiores reprehenderit quaerat vero et quisquam? Lorem, ipsum dolor sit amet consectetur adipisicing elit. Autem consectetur totam quisquam deleniti non modi sunt eaque maxime, ducimus debitis sint quia accusantium est voluptatum ut repellat obcaecati fuga consequuntur?')

author, data = st.columns(2)
author.info('Кто придумал: Мухаааааа', icon='💡')
data.info('Данные берутся из json', icon='🧠')