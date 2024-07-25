import streamlit as st
import pandas as pd
import json

try:
    from StringIO import StringIO  ## for Python 2
except ImportError:
    from io import StringIO  ## for Python 3
    
    
st.title(':zap: AddManuChain Dashboard')

import streamlit as st
import pandas as pd
from io import StringIO
with st.expander('Statistics'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        string_data = stringio.read()
        # st.write(string_data)

    data = json.loads(string_data)
    st.json(data)