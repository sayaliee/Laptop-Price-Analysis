import streamlit as st
import plotly_express as px
import numpy as np
import pandas as pd

df = pd.read_csv('Cleaned.csv')

st.title("Price Analysis Dashboard")
st.markdown("Explore the variation of Price with other columns in the dataset")

# Sidebar for column selection
categorical_cols = ['Company', 'TypeName', 'Cpu', 'Gpu', 'OpSys']
numerical_cols = ['Ram', 'Weight', 'Touchscreen', 'IPS', 'ppi','HDD','SSD','Hybrid','Flash_Storage']

all_columns = categorical_cols + numerical_cols
selected_column = st.sidebar.selectbox("Select a column to compare with Price:", all_columns)

# Plotting
if selected_column:
    if selected_column in categorical_cols:
        # Bar chart for categorical columns
        fig = px.bar(df, x=selected_column, y="Price", title=f"Price variation by {selected_column}")
    else:
        # Scatter plot for numerical columns
        fig = px.scatter(df, x=selected_column, y="Price", trendline="ols",
                         title=f"Price vs {selected_column}")

    st.plotly_chart(fig)