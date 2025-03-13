
import streamlit as st
import numpy as np
import plotly.graph_objects as go

def display_unit_circle(angle_degrees):
    angle_radians = np.radians(angle_degrees)
    
    # Circle data
    theta = np.linspace(0, 2 * np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)
    
    # Coordinates for the selected angle
    x_angle = np.cos(angle_radians)
    y_angle = np.sin(angle_radians)
    
    # Create a plotly figure
    fig = go.Figure()
    
    # Add unit circle
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Unit Circle'))
    # Add the selected angle line
    fig.add_trace(go.Scatter(x=[0, x_angle], y=[0, y_angle], mode='lines+markers', name=f'Angle: {angle_degrees}°', marker=dict(color='red')))
    # Add point on the circle
    fig.add_trace(go.Scatter(x=[x_angle], y=[y_angle], mode='markers', name='Point on Circle', marker=dict(color='blue', size=10)))
    
    # Set layout
    fig.update_layout(title='Unit Circle', xaxis_title='Cos(θ)', yaxis_title='Sin(θ)', showlegend=True, 
                      xaxis=dict(scaleanchor='y'), yaxis=dict(scaleanchor='x'), 
                      width=700, height=700)
    
    st.plotly_chart(fig)
    
def main():
    st.title("Unit Circle Explorer")
    
    angle = st.sidebar.slider("Select an angle (degrees)", 0, 360, 0)
    
    display_unit_circle(angle)
    
    # Calculate trigonometric values
    st.write(f"**sin(θ)**: {np.sin(np.radians(angle)):.4f}")
    st.write(f"**cos(θ)**: {np.cos(np.radians(angle)):.4f}")
    if np.cos(np.radians(angle)) != 0:
        st.write(f"**tan(θ)**: {np.tan(np.radians(angle)):.4f}")
    else:
        st.write("**tan(θ)**: Undefined (cos(θ) is 0)")

if __name__ == "__main__":
    main()
