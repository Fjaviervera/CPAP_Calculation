import datetime
import streamlit as st

st.title(':blue[Cálculo de Horas de CPAP]')

previous_counter = st.number_input("Medida Contador Visita Anterior",0,999999, 0)

previous_date = st.date_input(
    "Fecha Visita Anterior",
    datetime.datetime.today()- datetime.timedelta(days=30))

current_counter = st.number_input("Medida Contador Visita Actual",0,999999, 0)



current_date = st.date_input(
    "Fecha de Calculo de Uso",
    datetime.datetime.now() - datetime.timedelta(days=1))

st.markdown('#')


if st.button('Calcular'):


    #calculate the number of days between two datetime objects
    date_substract = current_date - previous_date # type: ignore
    increment = current_counter - previous_counter
    calc = increment/date_substract.days
    st.markdown('#')
    c1, c2, c3 = st.columns(3)
    with st.container():
        c1.metric(label="Días", value=date_substract.days, delta=None, delta_color="normal")
        c2.metric(label="Horas Uso", value=increment, delta=None, delta_color="normal")
        c3.metric(label="Horas/día", value="{:.2f}".format(calc), delta=None, delta_color="normal")



