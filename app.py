pip install streamlit
import streamlit as st
import numpy as np
from scipy.optimize import minimize

def objective_function(x):
    return x[0]*x[3]*(x[0]+x[1]+x[2])+x[2]

def constraint_1(x):
    return x[0]*x[1]*x[2]*x[3]-25.0

def constraint_2(x):
    sum_eq = 40.0
    for i in range(4):
        sum_eq = sum_eq - x[i]**2
    return sum_eq

st.title("Simple Optimization App")

x0 = [1,5,5,1]

b = (1.0,5.0)
bnds = (b, b, b, b)

con1 = {'type':'ineq','fun':constraint_1}
con2 = {'type':'eq','fun':constraint_2}
cons = [con1,con2]

solution = minimize(objective_function,x0,method='SLSQP',\
                   bounds=bnds,constraints=cons)

st.write("Solution")
st.write("x1 = ",solution.x[0])
st.write("x2 = ",solution.x[1])
st.write("x3 = ",solution.x[2])
st.write("x4 = ",solution.x[3])

st.write("Objective function value")
st.write(solution.fun)
streamlit run my_app.py
