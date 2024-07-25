import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from io import StringIO

st.title(":zap: AddManuChain Dashboard")
st.image("../src/img/title.jpg", caption="Sunrise by the mountains")
with st.expander("Statistics"):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        st.write(string_data)

        # You can uncomment and use json.loads if your file is in JSON format
        # data = json.loads(string_data)
        # st.json(data)

        # Assuming the uploaded file is a CSV for the following example
        df = pd.read_csv(StringIO(string_data))
        st.write(df.head())  # Display the first few rows of the dataframe

    # Plotting a histogram using seaborn
    fig, ax = plt.subplots(1, 1, figsize=(5, 3))
    sns.histplot(np.random.randn(100), ax=ax)
    st.pyplot(fig)
with st.expander('User Profile'):
    col1, col2 = st.columns(2)
    col1.text_input('Name :')
    col2.text_input('Family :')
    st.camera_input('Camera Input', key='camera_input')
