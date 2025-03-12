
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Unit Circle Explorer", layout="wide")
st.sidebar.image("https://www.quantuniversity.com/assets/img/logo5.jpg")
st.sidebar.divider()
st.title("Unit Circle Explorer")
st.divider()

# Page Navigation
st.sidebar.header("Navigation")
pages = {
    "Home": "home",
    "Unit Circle": "unit_circle",
    "Trigonometric Functions": "trig_functions"
}
selected_page = st.sidebar.selectbox("Select a page:", options=list(pages.keys()))

# Home Page
if selected_page == "Home":
    st.write("Welcome to the Unit Circle Explorer!")
    st.write("This app allows you to explore trigonometric functions and their relationships.")
    st.write("Use the navigation on the left to switch pages.")

# Unit Circle Page
elif selected_page == "Unit Circle":
    st.header("Unit Circle Visualization")
    
    # Slider for angle selection
    angle = st.slider("Select an angle (degrees):", 0, 360, 0)
    angle_rad = np.radians(angle)

    # Calculating coordinates
    x = np.cos(angle_rad)
    y = np.sin(angle_rad)

    # Plotting the unit circle
    fig = go.Figure()

    # Circle
    circle = go.Scatter(
        x=np.cos(np.linspace(0, 2*np.pi, 100)),
        y=np.sin(np.linspace(0, 2*np.pi, 100)),
        mode='lines',
        name='Unit Circle'
    )
    fig.add_trace(circle)

    # Angle Line
    fig.add_trace(go.Scatter(
        x=[0, x],
        y=[0, y],
        mode='lines',
        name='Angle',
        line=dict(color='red')
    ))
    
    # Point on the unit circle
    fig.add_trace(go.Scatter(
        x=[x],
        y=[y],
        mode='markers+text',
        name='Point',
        marker=dict(size=10, color='blue'),
        text=[f"({x:.2f}, {y:.2f})"],
        textposition="top center"
    ))

    fig.update_layout(
        title="Unit Circle and Angle",
        xaxis_title="Cosine Value",
        yaxis_title="Sine Value",
        showlegend=True,
        width=700,
        height=700
    )
    
    st.plotly_chart(fig)

# Trigonometric Functions Page
elif selected_page == "Trigonometric Functions":
    st.header("Trigonometric Functions Values")
    
    # Slider for angle selection
    angle_trig = st.slider("Select an angle (degrees):", 0, 360, 0)
    angle_rad_trig = np.radians(angle_trig)

    # Calculate trigonometric values
    sin_value = np.sin(angle_rad_trig)
    cos_value = np.cos(angle_rad_trig)
    if angle_rad_trig % np.pi == 0:  # Prevent division by zero for tan
        tan_value = "undefined"
    else:
        tan_value = np.tan(angle_rad_trig)

    # Displaying values
    st.write(f"sin({angle_trig}°) = {sin_value:.2f}")
    st.write(f"cos({angle_trig}°) = {cos_value:.2f}")
    st.write(f"tan({angle_trig}°) = {tan_value}")

st.divider()
st.write("© 2025 QuantUniversity. All Rights Reserved.")
st.caption("The purpose of this demonstration is solely for educational use and illustration. "
           "To access the full legal documentation, please visit this link. Any reproduction of this demonstration "
           "requires prior written consent from QuantUniversity.")
