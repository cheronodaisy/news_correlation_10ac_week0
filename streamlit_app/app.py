'''
Streamlit app to visualize output of data analysis
'''
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


@st.cache_data
def load_data(file_path):
    """
    Load data from a CSV file.

    Parameters:
    - file_path (str): The path to the CSV file.

    Returns:
    - DataFrame: The loaded data.
    """
    return pd.read_csv(file_path)


df = load_data('../data/domains_location.csv')

add_selectbox = st.sidebar.selectbox(
    "Contact Us",
    ("Email", "Home phone", "Mobile phone")
)

country_counts = df['Country'].value_counts()

sorted_country_counts = country_counts.sort_values(ascending=False)

st.title('Countries with the Highest Number of Media Organizations')
plt.figure(figsize=(10, 6))
top_countries = sorted_country_counts.head(10)
top_countries.plot(kind='bar')
plt.xlabel('Country')
plt.ylabel('Number of Media Organizations')
plt.xticks(rotation=45)
st.pyplot(plt.gcf())

st.title('Sentiment Analysis Visualization')

left_column, right_column, col3 = st.columns(3)
with left_column:
    st.image('output.png', caption='Sentiment count')

with right_column:
    st.image('plot.png', caption='Content length vs sentiment analysis')

with col3:
    st.image('topics.png', caption='Topic trends over time')
