
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def display_trigonometric_functions(angle_degrees):
    angle_radians = np.radians(angle_degrees)
    angles = np.linspace(0, 2 * np.pi, 100)

    # Calculate sine, cosine, and tangent values 
    sin_values = np.sin(angles)
    cos_values = np.cos(angles)
    tan_values = np.tan(angles)
    
    # Create a plotly figure
    fig = go.Figure()
    
    # Add sin, cos, and tan traces
    fig.add_trace(go.Scatter(x=angles, y=sin_values, mode='lines', name='sin(θ)', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=angles, y=cos_values, mode='lines', name='cos(θ)', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=angles, y=tan_values, mode='lines', name='tan(θ)', line=dict(color='green')))
    
    # Set layout
    fig.update_layout(title='Trigonometric Functions', xaxis_title='Angle (radians)', yaxis_title='Function Value', 
                      width=700, height=700, showlegend=True)

    st.plotly_chart(fig)

def main():
    st.title("Trigonometric Functions Explorer")
    
    angle = st.sidebar.slider("Select an angle (degrees)", 0, 360, 0)
    
    display_trigonometric_functions(angle)
    
    # Display calculated values
    st.write(f"**sin(θ)**: {np.sin(np.radians(angle)):.4f}")
    st.write(f"**cos(θ)**: {np.cos(np.radians(angle)):.4f}")
    if np.cos(np.radians(angle)) != 0:
        st.write(f"**tan(θ)**: {np.tan(np.radians(angle)):.4f}")
    else:
        st.write("**tan(θ)**: Undefined (cos(θ) is 0)")

if __name__ == "__main__":
    main()
