import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
data = pd.read_excel("C:/Users/aryam/OneDrive/Desktop/HARVARD GEOGRAPHIC INSIGHTS/Final Underlying Dashboard Data Extracted Jan21", sheet_name="NFHS Change Data")

# Sidebar for user input
st.sidebar.title("Visualization Options")
chart_type = st.sidebar.selectbox(
    "Choose chart type", [
        "Line Chart", "Bar Chart", "Column Chart", "Column Stacking Chart", "Bar Stacking Chart",
        "Area Chart", "Area Stacking Chart", "Spline Chart", "Pie Chart", "Waterfall Chart", 
        "Scatter Chart", "Donut Chart", "Ranking", "Bubble Chart", "Map", "Table"
    ]
)
x_axis = st.sidebar.selectbox("Select X-axis", data.columns)
y_axis = st.sidebar.selectbox("Select Y-axis", data.columns)

# Create visualizations based on user input
st.title("Customizable Dashboard")

if chart_type == "Line Chart":
    fig, ax = plt.subplots()
    sns.lineplot(x=x_axis, y=y_axis, data=data, ax=ax)
    st.pyplot(fig)
elif chart_type == "Bar Chart":
    fig, ax = plt.subplots()
    sns.barplot(x=x_axis, y=y_axis, data=data, ax=ax)
    st.pyplot(fig)
elif chart_type == "Column Chart":
    fig = px.bar(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Column Stacking Chart":
    fig = px.bar(data, x=x_axis, y=y_axis, barmode='stack')
    st.plotly_chart(fig)
elif chart_type == "Bar Stacking Chart":
    fig = px.bar(data, x=x_axis, y=y_axis, orientation='h', barmode='stack')
    st.plotly_chart(fig)
elif chart_type == "Area Chart":
    fig = px.area(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Area Stacking Chart":
    fig = px.area(data, x=x_axis, y=y_axis, groupnorm='fraction')
    st.plotly_chart(fig)
elif chart_type == "Spline Chart":
    fig, ax = plt.subplots()
    sns.lineplot(x=x_axis, y=y_axis, data=data, ax=ax)
    ax.lines[0].set_linestyle("--")
    st.pyplot(fig)
elif chart_type == "Pie Chart":
    fig = px.pie(data, names=x_axis, values=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Waterfall Chart":
    fig = px.bar(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Scatter Chart":
    fig = px.scatter(data, x=x_axis, y=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Donut Chart":
    fig = px.pie(data, names=x_axis, values=y_axis, hole=0.3)
    st.plotly_chart(fig)
elif chart_type == "Ranking":
    fig = px.bar(data, x=x_axis, y=y_axis)
    fig.update_layout(yaxis={'categoryorder':'total descending'})
    st.plotly_chart(fig)
elif chart_type == "Bubble Chart":
    fig = px.scatter(data, x=x_axis, y=y_axis, size=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Map":
    fig = px.scatter_geo(data, locations=x_axis, size=y_axis)
    st.plotly_chart(fig)
elif chart_type == "Table":
    st.write(data)
