import streamlit as st
import pandas as pd
import seaborn as sns

# Laden des Titanic-Datensets
@st.cache
def load_data():
    df = sns.load_dataset('titanic')
    return df

df = load_data()

# Streamlit-Seitenkonfiguration
st.set_page_config(page_title="Titanic Dataset Explorer")
st.title("Titanic Dataset Explorer")

# Eingabefelder zur Datenfilterung
class_filter = st.sidebar.multiselect('Wähle die Klassen:', options=df['class'].unique(), default=df['class'].unique())
sex_filter = st.sidebar.multiselect('Wähle das Geschlecht:', options=df['sex'].unique(), default=df['sex'].unique())
survived_filter = st.sidebar.radio('Überlebensstatus:', ['All', 'Survived', 'Not Survived'])

# Filteranwendung basierend auf der Auswahl
filtered_data = df[(df['class'].isin(class_filter)) & (df['sex'].isin(sex_filter))]
if survived_filter == 'Survived':
    filtered_data = filtered_data[filtered_data['survived'] == 1]
elif survived_filter == 'Not Survived':
    filtered_data = filtered_data[filtered_data['survived'] == 0]

# Datenanzeige
st.write("Anzahl der angezeigten Einträge:", filtered_data.shape[0])
st.dataframe(filtered_data)

# Visualisierungen
st.write("Verteilung der Überlebenden nach Klasse und Geschlecht")
fig = sns.catplot(data=filtered_data, kind='count', x='class', hue='sex', col='survived', palette='viridis', aspect=.7)
st.pyplot(fig)
