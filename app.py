import streamlit as st
from apputil import *

# Load Titanic dataset
df = pd.read_csv('https://raw.githubusercontent.com/leontoddjohnson/datasets/main/data/titanic.csv')

# Exercise 1
st.write("Did younger children have a higher survival rate than older individuals?")

fig1 = visualize_demographic()
st.plotly_chart(fig1, use_container_width=True)

# Exercise 2

st.write("The output from the last_names() function seems" \
"to agree with the data table. If we pull up the raw .csv" \
"and use Ctrl+F and search up a given name, we'll see the" \
"count of the output match with the output of ctrl+F.")

st.write("Did males or females have a higher average fare?")
# Generate and display the figure
fig2 = visualize_families()
st.plotly_chart(fig2, use_container_width=True)

