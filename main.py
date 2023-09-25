import streamlit as st
import pandas as pd
import datetime
import pytz
import plotly.express as px
from bs4 import BeautifulSoup
import gspread
from oauth2client.service_account import ServiceAccountCredentials

tz = pytz.timezone('Asia/Kuala_Lumpur')

st.set_page_config(layout="wide")
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

url = "https://github.com/your/csv"
df = pd.read_csv(url)

age_columns = [col for col in df.columns if col.startswith('age_group|')]

def clean_and_convert_age_columns(df):
    for col in age_columns:
        df[col] = df[col].str.replace(',', '').astype(int)

def create_level_selectbox():
    level_index = st.session_state.get("level_index", 0)
    levels = df['P'].dropna().unique().tolist()
    level = st.selectbox("Select level:", levels, index=level_index)
    st.session_state["level_index"] = levels.index(level)
    return level

def create_dname_selectbox(filtered_df):
    dname_index = st.session_state.get("dname_index", 0)
    d_names = filtered_df['D'].dropna().unique().tolist()
    d_name = st.selectbox("Select dname:", d_names, index=dname_index)
    st.session_state["dname_index"] = d_names.index(d_name)
    return d_name

def filter_data(level):
    return df[df['P'] == level]

def create_recent_save_data_selectbox(worksheet, d_name):
    data = worksheet.get_all_values()
    df2 = pd.DataFrame(data[1:], columns=data[0])
    filtered_df2 = df2.loc[df2["District"] == d_name]
    selectname_options = filtered_df2["Name Save Data"].dropna().unique().tolist()
    return st.sidebar.selectbox('Recent Save Data:', selectname_options, disabled=not selectname_options)

def display_registered_voters(selected_rows, column_names, chart_title):
    st.markdown(f"### {chart_title}")
    total = selected_rows[column_names].sum(axis=1)
    total_df = pd.DataFrame({'Total': total})
    dfnew = pd.concat([selected_rows[column_names], total_df], axis=1)
    percentages = dfnew[column_names].div(total, axis=0).mul(100)
    dfnew = dfnew.append(percentages.applymap(to_percentage), ignore_index=True)
    dfnew.insert(0, chart_title, ['Vote', 'Percentage (%)'])
    dfnew.at[1, dfnew.columns[len(column_names)]] = 100
    dfnew['Total'] = dfnew['Total'].astype(int)
    html = (
        dfnew
        .style.set_properties(**{'text-align': 'center'})
        .hide_index()
        .render()
    )
    st.write(html, unsafe_allow_html=True)

def create_and_display_bar_chart(x, y, chart_title):
    fig = px.bar(x=x, y=y, color=y, height=400)
    fig.add_scatter(x=x, y=y, mode='lines', name='Curve')
    fig.update_layout(
        xaxis_title=chart_title,
        yaxis_title="Registered Voters",
        font=dict(
            family="Courier New, monospace",
            size=18,
            color="RebeccaPurple"
        )
    )
    st.plotly_chart(fig)

def reset_sliders(renamed_columns):
    for column_name in renamed_columns.values():
        st.session_state[f"slider_col1_{column_name}"] = 72
        st.session_state[f"slider_col2_{column_name}"] = 70

def get_result_text(Avote, nonAvote, Awin23, remAvote):
    if Avote >= Awin23:
        result = "<h2 style='color: green; animation: pulse 3s infinite'>A is Winning. It is forecast to win 2/3</h2>"
    elif Avote > nonAvote:
        result = "<h2 style='color: green; animation: pulse 3s infinite'>A is Winning</h2>"
    else:
        result = f"<h2 style='color: red; animation: pulse 3s infinite'>A is Losing - it needs {remAvote} support to win</h2>"
    return result

def to_percentage(val):
    return '{:.2f}'.format(val)

scope = ["https://your/spreadsheets", "https://your/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["A_service_account"], scope)
client = gspread.authorize(credentials)
sheet = client.open_by_url(st.secrets["private_gsheets_url"])

chart_type = st.sidebar.radio('Select Category', ('Ethnic', 'Age'))

df['P'] = df.apply(lambda row: row['P_code'] + ' ' + row['P_name'], axis=1)
df['D'] = df.apply(lambda row: row['D_code'] + ' ' + row['D_name'], axis=1)
level = create_level_selectbox()
filtered_df = filter_data(level)
d_name = create_dname_selectbox(filtered_df)

if chart_type == "Ethnic":
    worksheet = sheet.get_worksheet(0)
    data = worksheet.get_all_values()
    df2 = pd.DataFrame(data[1:], columns=data[0])
    selected_name = create_recent_save_data_selectbox(worksheet, d_name)
    column_names = [col for col in df.columns if col.startswith('ethnic|')]
    chart_title = "Number of Registered Voters by Ethnicity"
elif chart_type == "Age":
    worksheet = sheet.get_worksheet(1)
    data = worksheet.get_all_values()
    df2 = pd.DataFrame(data[1:], columns=data[0])
    selected_name = create_recent_save_data_selectbox(worksheet, d_name)
    column_names = [col for col in df.columns if col.startswith('age_group|')]
    chart_title = "Number of Registered Voters by Age Group"

display_registered_voters(df[df['D'] == d_name], column_names, chart_title)
create_and_display_bar_chart(list(renamed_columns.values()), df[column_names].iloc[0, :], chart_title)
if chart_type == "Age":
    display_age_group_sliders(renamed_columns)
elif chart_type == "Ethnic":
    display_ethnic_group_sliders(renamed_columns)
resetBtn = st.button("Reset", on_click=reset_sliders(renamed_columns))

if not st.sidebar.button("Load"):
    name = st.text_input("Enter a name for save data:", value=st.session_state["name"])
    description = st.text_input("Enter a description for save data:", value=st.session_state["desc"])
    updateBtn = st.button("Update", disabled=False)
elif st.sidebar.button("Load") and "name" in st.session_state:
    updateBtn = st.button("Update", disabled=False)
else:
    name = st.text_input("Enter a name for save data:", value=st.session_state["name"])
    description = st.text_input("Enter a description for save data:", value=st.session_state["desc"])
    updateBtn = st.button("Update", disabled=False)

if updateBtn:
    dfall = pd.DataFrame(all_data, index=[0])
    dfall["Total Vote Count Forecast"] = Avote
    dfall["Not Vote A"] = nonAvote
    dfall["Total Voter"] = total.values
    dfall["Simple Majority Votes"] = Awin
    dfall["Two Third Winning"] = Awin23
    dfall["Result"] = text_result
    dfall.insert(0, "Name Save Data", name)
    dfall.insert(1, "Description Save Data", description)
    dfall.insert(2, "Parliament", level, True)
    dfall.insert(3, "District", d_name, True)
    dfall["Datetime"] = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
    update_data_in_google_sheets(chart_type, sheet, dfall)

if chart_type == "Ethnic":
    submit_data_to_google_sheets(chart_type, sheet, name, description, dfall)

resetBtn = st.button("Reset", on_click=reset_sliders(renamed_columns))