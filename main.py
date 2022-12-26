# To run, use the command 'streamlit run main.py'

from datasets import *
import streamlit as st
import pandas as pd
import altair as alt


df: pd.DataFrame = None
columns: list = None


def getNumericPartOfDataframe(df: pd.DataFrame) -> pd.DataFrame:
    numeric_dtypes = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    return df.select_dtypes(include=numeric_dtypes)


def buildPage(): # Main
    st.title("Linear Regrassion App")
    buildHowToUse()

    try:
        buildInputs()
        buildOutputs()
    except:
        st.error("Data processing error")

    buildSamples()


def buildHowToUse():
    st.subheader("How to use")
    st.text("1 - Select a dataset")
    st.text("2 - Select two columns (numerics only)")
    st.text("3 - Observe the chart with the linear regression")


def buildInputs():
    global df, columns
    st.subheader("Inputs")
    dataset_name = st.selectbox("Choose some dataset", getDatasetNames())
    df = getDataFrameByDatasetName(dataset_name)
    columns = st.multiselect("Numeric columns", getNumericPartOfDataframe(df).columns)


def buildOutputs():
    st.subheader("Outputs")

    with st.expander('DataFrame'):
        st.dataframe(df)

    with st.expander('Chart'):
        if len(columns) != 2:
            st.warning('Select two numeric columns')
        else:
            chart = alt.Chart(df).mark_point(size=25, filled=True, color="red").encode(
                x=columns[0],
                y=columns[1]
            )
            chart += chart.transform_regression(columns[0], columns[1]).mark_line()
            st.altair_chart(chart)


def buildSamples():
    st.subheader('Correlation Samples')
    st.table(pd.DataFrame({
        'DF Name': ['cars', 'cars', 'cars', 'cars', 'cars', 'seattle-weather', 'countries'],
        'Column 1': ['Weight_in_lbs', 'Weight_in_lbs', 'Cilynders', 'Horsepower', 'Weight_in_lbs', 'temp-min', 'fertility'],
        'Column 2': ['Miles_per_Gallon', 'Acceleration', 'Miles_per_Gallon', 'Miles_per_Gallon', 'Horsepower', 'temp_max', 'life_expect'],
    }))


buildPage()
