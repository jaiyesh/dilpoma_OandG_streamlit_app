import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt

st.title("Dynamic circle")

st.sidebar.title("Inputs")

r = st.sidebar.slider("Enter the radius of circle", min_value = 0, max_value = 20, value=10 )


x = np.linspace(-r,r,1000)
    
y_p = (r**2 - x**2)**0.5
    
y_n = -y_p



b = st.sidebar.button(f"Create Circle of radius {r}")


if b: 
    st.write(f"Circle Craetion of radius {r}")

    plt.style.use("classic")

    plt.figure(figsize=(6,12))

    fig,ax = plt.subplots()

    ax.plot(x,y_p, linewidth =4)
    ax.plot(x,y_n, linewidth = 4)

    ax.grid(True)

    ax.set_title("CIRCLE")

    ax.set_xlabel("X axis")
    ax.set_ylabel("Y axis")

    ax.set_xlim(-20,20)

    ax.set_ylim(-20,20)

    st.pyplot(fig)

   

