import streamlit as st
import pandas as pd
import plotly.express as px
from bs4 import BeautifulSoup

# Function to display sliders for ethnic groups
def display_ethnic_group_sliders(renamed_columns):
    col2 = st.columns(2)
    with col2[0]:
        st.markdown("#### Ethnic")
        for column_name in renamed_columns.values():
            st.markdown("##### " + column_name)

    with col2[1]:
        st.markdown("#### Turnout forecast")
        slider_values1 = {}
        for column_name in renamed_columns.values():
            key = f"slider_col1_{column_name}"
            if key not in st.session_state:
                st.session_state[key] = 72
            slider_values1[column_name] = st.slider("", 0, 100, st.session_state[key], key=key, format='%d%%')

    col3 = st.columns(2)
    with col3[0]:
        st.markdown("#### A support forecast")
        slider_values = {}
        for column_name in renamed_columns.values():
            key = f"slider_col2_{column_name}"
            if key not in st.session_state:
                st.session_state[key] = 70
            slider_values[column_name] = st.slider("", 0, 100, st.session_state[key], key=key, format='%d%%')

    with col3[1]:
        st.markdown("#### Vote count forecast")
        all_data = {}
        Avote = 0
        for column_name in renamed_columns.values():
            value = int(dfnew[column_name].values[0] * slider_values1[column_name] / 100 * slider_values[column_name] / 100)
            all_data[f"{column_name} | Pct Turnout Forecast"] = slider_values1[column_name]
            all_data[f"{column_name} | Pct A Support Forecast"] = slider_values[column_name]
            all_data[f"{column_name} | Vote Count Forecast"] = value
            Avote += value

    nonAvote = total.values - Avote
    Awin = int(total.values[0] / 2 + 1)
    Awin23 = int(total.values[0] / 3 + Awin)
    remAvote = abs(Avote - Awin)
    st.markdown(f"#### In order for A to earn a simple majority, it needs {Awin} support while to earn 2/3 votes, it needs {Awin23} support")
    st.markdown(f"#### Currently, it is expected to garner {Avote} support")

    result = get_result_text(Avote, nonAvote, Awin23, remAvote)
    st.markdown(result, unsafe_allow_html=True)
    soup = BeautifulSoup(result, 'html.parser')
    text_result = soup.h2.text