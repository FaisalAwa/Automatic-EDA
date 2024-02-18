# import streamlit as st
# import pandas as pd
# import io
# import chardet
# from streamlit_lottie import st_lottie
# from ydata_profiling import ProfileReport
# import dtale
# from skimpy import skim

# # Attractive Title of the app
# st.markdown(
#     """
#     <style>
#         .title {
#             font-size: 50px;
#             color: #ff6347;
#             text-align: center;
#         }
#     </style>
#     <div class="title">
#         📊 Quick EDA Explorer 💫
#     </div>
#     """,
#     unsafe_allow_html=True,
# )
# # Description
# st.markdown("""
#     Quick EDA Explorer is a powerful web app that allows you to perform exploratory data analysis (EDA) on your CSV files within seconds. 
#     Upload your CSV file and select from three powerful EDA packages: YData Profiling, Skimpy, or D-Tale. 
#     Explore your data and gain valuable insights effortlessly! 💡
# """)
# # Lottie Animation
# lottie_url = "https://lottie.host/0d8f0ae1-d257-4bb4-b95d-c2bc7576be39/uRPjGpvVH8.json"
# st_lottie(lottie_url, speed=1, width=800, height=400, key="lottie")



# # Upload CSV file
# uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# # Create a sidebar
# st.sidebar.header('Package Selection')

# # Create a dropdown menu in the sidebar
# options = ['YData Profiling', 'Skimpy', 'D-Tale']
# selected_option = st.sidebar.selectbox('Select the package type:', options)

# st.write(f'You selected: {selected_option}')

# if uploaded_file is not None:
#     st.write('File Uploaded Successfully')
    
#     # Detect the file encoding
#     result = chardet.detect(uploaded_file.read())
#     encoding = result['encoding']
#     uploaded_file.seek(0)
    
#     data = pd.read_csv(uploaded_file, encoding=encoding)
#     st.write(data)
    
#     if selected_option == 'YData Profiling':
#         st.write('Generating YData Profiling Report...')
#         profile = ProfileReport(data)
#         st.components.v1.html(profile.to_html(), height=600, scrolling=True)
#     elif selected_option == 'Skimpy':
#         st.write('Generating Skimpy Report...')
#         report = skim(data)
#         st.write(report)
#     elif selected_option == 'D-Tale':
#         st.write('Displaying D-Tale...')
#         # Start D-Tale app
#         d = dtale.show(data)
#         # Get D-Tale app url and display in Streamlit
#         st.write(f'D-Tale is running at: {d._url}')
#         st.write(f'Please open the above URL in a new tab to access D-Tale')
# else:
#     st.write('Please upload a CSV file')


import streamlit as st
import pandas as pd
import io
import chardet
from streamlit_lottie import st_lottie
from ydata_profiling import ProfileReport
import dtale
from skimpy import skim

# Attractive Title of the app
st.markdown(
    """
    <style>
        .title {
            font-size: 50px;
            color: #ffffff;
            text-align: center;
        }
    </style>
    <div class="title">
        🚀 Superfast EDA Explorer 🚀
    </div>
    """,
    unsafe_allow_html=True,
)
# Lottie Animation
lottie_url = "https://lottie.host/0d8f0ae1-d257-4bb4-b95d-c2bc7576be39/uRPjGpvVH8.json"
st_lottie(lottie_url, speed=1, width=800, height=400, key="lottie")
# Description
st.markdown("""
    Superfast EDA Explorer is an incredibly powerful web app that enables you to perform exploratory data analysis (EDA) on your CSV files in minutes. 
    Upload your CSV file and choose from three of the most robust EDA packages available: 
    
    - **YData Profiling**: A package that creates beautiful and comprehensive profiling reports with just one line of code. 
      It helps in understanding the data and making data cleaning and preprocessing faster and easier. 💎
      
    - **Skimpy**: A lightweight and fast package for generating summary statistics of your dataset. 
      It provides essential insights without the overhead of more extensive packages. 🚀
      
    - **D-Tale**: A flexible and interactive web-based tool for data analysis. 
      It provides a wide variety of analysis and visualization options right in your browser. 🌍
      
    Upload your data, choose your package, and let the app do the rest. Gain valuable insights effortlessly and quickly! 🧠✨
""")

# # Lottie Animation
# lottie_url = "https://lottie.host/0d8f0ae1-d257-4bb4-b95d-c2bc7576be39/uRPjGpvVH8.json"
# st_lottie(lottie_url, speed=1, width=800, height=400, key="lottie")

# Upload CSV file
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")

# Create a sidebar
st.sidebar.header('Choose EDA Package')

# Create a dropdown menu in the sidebar
options = ['','YData Profiling', 'Skimpy', 'D-Tale']
selected_option = st.sidebar.selectbox('Select the package type:', options)

st.write(f'You selected: {selected_option}')

if uploaded_file is not None:
    st.write('File Uploaded Successfully')
    
    # Detect the file encoding
    result = chardet.detect(uploaded_file.read())
    encoding = result['encoding']
    uploaded_file.seek(0)
    
    data = pd.read_csv(uploaded_file, encoding=encoding)
    st.write(data)
    
    if selected_option == 'YData Profiling':
        st.write('Generating YData Profiling Report...')
        profile = ProfileReport(data)
        st.components.v1.html(profile.to_html(), height=600, scrolling=True)
    elif selected_option == 'Skimpy':
        st.write('Generating Skimpy Report...')
        report = skim(data)
        st.write(report)
    elif selected_option == 'D-Tale':
        st.write('Displaying D-Tale...')
        # Start D-Tale app
        d = dtale.show(data)
        # Get D-Tale app url and display in Streamlit
        st.write(f'D-Tale is running at: {d._url}')
        st.write(f'Please open the above URL in a new tab to access D-Tale')
else:
    st.write('Please upload a CSV file')
