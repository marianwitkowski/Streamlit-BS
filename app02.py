
# Customizacja CSSów + dodatkowe widgety

import streamlit as st
import time
import datetime

def apply_custom_css():
    custom_css = '''
    <style>

        h1 {
            color: #00FF00;
        }

        .stButton>button {
            background-color: #00FF00;
            color: white;
        }
    </style>
    '''
    st.markdown(custom_css, unsafe_allow_html=True)

apply_custom_css()
st.title("Przykładowy formularz Streamlit")

#with st.spinner("Czekaj...."):
#    time.sleep(5)
#st.success("Done!")

with st.form("my_form1"):
    st.write("Formularz 1")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("slider", slider_val, "checkbox", checkbox_val)

with st.form("my_form2"):
    st.write("Formularz 2")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    text_input = st.text_input("Wprowadź swój tekst:")
    memo = st.text_area("Memo:", "aaa bbb cccc dddd eee fffff dddd")
    number_input = st.number_input("Wprowadź swoją liczbę:", min_value=0, max_value=100, value=50)

    # Pole jednorazowego wyboru
    radio_options = ["Opcja 1", "Opcja 2", "Opcja 3"]
    radio_choice = st.radio("Wybierz jedną z opcji:", radio_options)

    # Pole wielokrotnego wyboru
    multi_options = ["Element 1", "Element 2", "Element 3", "Element 4"]
    multi_choice = st.multiselect("Wybierz elementy:", multi_options)

    slider_discrete = st.select_slider('Wybierz kolor', options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])

    date_input = st.date_input("Wybierz datę:", value=datetime.date.today())
    time_input = st.time_input("Wprowadź czas:", value=datetime.time(6,45))

    submit_button = st.form_submit_button("Wyślij formularz")

    if submit_button:
        st.info('A oto wyniki', icon="ℹ️")
        st.write("Wprowadzone wartości:")
        st.write(f"Tekst: {text_input}")
        st.write(f"Liczba: {number_input}")
        st.write(f"Jednorazowy wybór: {radio_choice}")
        st.write(f"Wielokrotny wybór: {', '.join(multi_choice) if multi_choice else 'Brak'}")
        st.write(f"Suwak: {slider_discrete}")
        st.write(f"Data: {date_input}")
