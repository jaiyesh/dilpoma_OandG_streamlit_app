import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt

st.title("Reservoir Engineering Application")

st.sidebar.title("User Inputs")


application = st.sidebar.selectbox("Select the Reservoir Engineering Application: ",
                                   ("Pressure Profile", "Klinkenberg Effect"),)


if application == "Pressure Profile":

    st.subheader("Pressure Profile Application")


    k = st.sidebar.slider("Permeability (md)", min_value=10, max_value=200, value= 100)

    mu = st.sidebar.slider("viscosity(cp)", min_value=10, max_value=50, value= 15)

    q = st.sidebar.slider("Flowrate (STB/Day)", min_value=100, max_value=500, value= 200)

    re = st.sidebar.number_input("Outer Radius of Reservoir(ft)", min_value=100, max_value=10000, value = 2500)

    rw = st.sidebar.number_input('Wellbore Radius (ft)',min_value=1,max_value=10,value = 1)

    pe = st.sidebar.number_input('Pressure at the boundary of Reservoir(psi)',min_value = 100,max_value=10000, value =4000)

    B = st.sidebar.number_input('Formation Volume Factor(bbl/stb)',min_value = 1,max_value=2, value =1)

    h= st.sidebar.number_input('Net pay thickness of Reservoir (feet)',min_value = 2,max_value=500, value =30)


    r = np.linspace(rw,re,1000)

    P = pe - (141.2*q*mu*B*(np.log(re/r))/k/h)

    y_min = P[np.where(r==rw)]


    b = st.button("Show pressure Profile")

    if b:

        plt.figure(figsize=(8,6))

        fig,ax = plt.subplots()

        ax.plot(r,P,linewidth =4)

        ax.grid(True)
        ax.axhline(y_min,linewidth = 4, color ="red")

        ax.set_xlabel("radius(feet)")
        ax.set_ylabel("Pressure at radius r, (PSI)")
        ax.set_title('Pressure Profile')
        ax.set_ylim(0,5000)


        st.pyplot(fig)

elif application == "Klinkenberg Effect":

    st.subheader("Klinkenberg Effect")

    kg = st.sidebar.number_input("Enter the gas perm.(md)", min_value=1, max_value=200, value = 50)

    pm = st.sidebar.number_input('Enter The mean pressure(psi)',min_value=1,max_value=10,value = 4)

    k = st.sidebar.number_input('Enter the initial guess of absolute permeability(md)',min_value = 1,max_value=1000, value =100)

    b = st.button("Run Klinkenberg Effect")

    if b:


        count = 0
        st.write(f"The value of kl_{count} is {k}")

        while (abs(6.9*(k**0.64)+pm*k-pm*kg)>0.000000000001):
            st.write("=======================")
            updated_value = (6.9*(k**0.64)+pm*k-pm*kg)/(4.416*(k**(-0.36)) + pm) #f(k_l)/f'(k_l)
            k = k - updated_value
            count = count+1
            st.write(f"The value of kl_{count} is {k}")
            

        st.write(f"The final value of Perm K is : {k}")

        m = (kg-k)/((1/pm)-0)

        x_axis = np.linspace(0,1,200)


        y_axis = m*x_axis+k

        plt.style.use("classic")
        plt.figure(figsize=(10,8))

        fig,ax = plt.subplots()

        ax.plot(x_axis, y_axis,label="Klinkenberg curve")

        ax.scatter(1/pm,kg,s=10,c="red",label = "Lab condtion reading")

        ax.axhline(k,color="black",lw=4,label = f"Absolute Perm: {k} mD")

        ax.set_ylim(0,100)
        ax.set_xlim(0,1.02)

        ax.set_xlabel("1/Mean_pressure (psi^-1)")
        ax.set_ylabel("Measured Gas Permeability(md)")
        ax.legend()
        ax.set_title("The Klinkenberg Effect")
        ax.grid(True)

        st.pyplot(fig)





