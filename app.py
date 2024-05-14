import streamlit as st
import pandas as pd
import seaborn as sns

# Ensure this is the first command executed:
st.set_page_config(page_title="Titanic Dataset Explorer", layout='wide')

# Updated caching using the new method
@st.cache_data
def load_data():
    df = sns.load_dataset('titanic')
    return df

df = load_data()

st.title("Titanic Dataset Explorer")

# Ensuring the column exists and using correct data type
if 'class' in df.columns:
    class_options = df['class'].unique().tolist()
else:
    st.error("Column 'class' not found in the dataset.")
    class_options = []

if 'sex' in df.columns:
    sex_options = df['sex'].unique().tolist()
else:
    st.error("Column 'sex' not found in the dataset.")
    sex_options = []

# Sidebar for user input
class_filter = st.sidebar.multiselect('Wähle die Klassen:', options=class_options, default=class_options)
sex_filter = st.sidebar.multiselect('Wähle das Geschlecht:', options=sex_options, default=sex_options)
survived_filter = st.sidebar.radio('Überlebensstatus:', ['All', 'Survived', 'Not Survived'])

# Applying filters based on user input
filtered_data = df[df['class'].isin(class_filter) & df['sex'].isin(sex_filter)]
if survived_filter == 'Survived':
    filtered_data = filtered_data[filtered_data['survived'] == 1]
elif survived_filter == 'Not Survived':
    filtered_data = filtered_data[filtered_data['survived'] == 0]

# Displaying the filtered data
st.write("Anzahl der angezeigten Einträge:", filtered_data.shape[0])
st.dataframe(filtered_data)

# Visualizations
st.write("Verteilung der Überlebenden nach Klasse und Geschlecht")
fig = sns.catplot(data=filtered_data, kind='count', x='class', hue='sex', col='survived', palette='viridis', aspect=.7)
st.pyplot(fig)
