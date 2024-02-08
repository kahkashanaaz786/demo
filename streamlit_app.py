import pandas as pd 
import plotly.express as px
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title=" Iris Dashboard",
                   page_icon="🪴",
                   layout="wide"
)



# Read the CSV file into a DataFrame
df = pd.read_csv('Iris.csv')

st.sidebar.header("Description")
st.sidebar.markdown("""The Iris dataset is a classic dataset in 
machine learning containing 150 instances
                 of iris flowers,
each with four features: sepal length, 
                sepal width, petal length, 
and petal width (all in centimeters).
                 The goal is to classify each flower 
into one of three species: Setosa, Versicolor,
                 or Virginica. It's often used for 
teaching and practicing classification algorithms
                 due to its simplicity 
and well-defined nature.""")     


#-------------MAINPAGE--------------#
st.title("🪴IRIS FLOWER DASHBOARD")
st.markdown("##")
#
lef_colm,righ_colm=st.columns(2)
# Pie chart for Spieces
sp_distribution = df["Species"].value_counts(normalize=True) * 100
fig_SPE_pie = px.pie(
    values=sp_distribution,
    names=sp_distribution.index,
    title="Pie chart of spices",
    labels={},
    color_discrete_sequence=["#0083B8"] 
)
lef_colm.plotly_chart(fig_SPE_pie, use_container_width=True)

fig_SPE_bar = px.bar(
    x=sp_distribution.index,
    y=sp_distribution.values,
    labels={"x": "Species", "y": "Count"},
    title="Bar chart of species"
)
righ_colm.plotly_chart(fig_SPE_bar, use_container_width=True)




# Line chart for SepalLengthCm, SepalWidthCm, PetalLengthCm, and PetalWidthCm
fig_line_chart = px.line(
    df,
    x=df.index,
    y=["SepalLengthCm", "SepalWidthCm", "PetalLengthCm", "PetalWidthCm"],
    title="Line chart of Measurements",
    labels={"x": "Index", "y": "Measurement"}
)
st.plotly_chart(fig_line_chart, use_container_width=True)




col1,col2,col3=st.columns(3)

# Scatter plot for SepalLengthCm versus SepalWidthCm
fig_scatter_sepal = px.scatter(
    df,
    x='SepalLengthCm',
    y='SepalWidthCm',
    title='Scatter plot: Sepal Length vs. Sepal Width',
    labels={'SepalLengthCm': 'Sepal Length (cm)', 'SepalWidthCm': 'Sepal Width (cm)'}
)
col1.plotly_chart(fig_scatter_sepal, use_container_width=True)
# 3D SCATTER
fig_scatter_3d = px.scatter_3d(
    df,
    x='SepalLengthCm',
    y='SepalWidthCm',
    z='PetalLengthCm',
    title='3D Scatter plot: Sepal Length vs. Sepal Width vs. Petal Length',
    labels={'SepalLengthCm': 'Sepal Length (cm)', 'SepalWidthCm': 'Sepal Width (cm)', 'PetalLengthCm': 'Petal Length (cm)'}
)
col2.plotly_chart(fig_scatter_3d, use_container_width=True)


# Scatter plot for PetalLengthCm versus PetalWidthCm
fig_scatter_petal = px.scatter(
    df,
    x='PetalLengthCm',
    y='PetalWidthCm',
    title='Scatter plot: Petal Length vs. Petal Width',
    labels={'PetalLengthCm': 'Petal Length (cm)', 'PetalWidthCm': 'Petal Width (cm)'}
)
col3.plotly_chart(fig_scatter_petal, use_container_width=True)
