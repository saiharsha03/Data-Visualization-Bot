import google.generativeai as genai
import streamlit as st
import pandas as pd
import re
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import statsmodels.api as sm
import geopandas as gpd


def execute_code_snippet(code):
    local_context = {}
    try:
        exec(code, globals(), local_context)
    except Exception as e:
        print(f"Error executing code snippet: {e}")

gen_ai_key=st.secrets["gemini_key"]

genai.configure(api_key=gen_ai_key)

model = genai.GenerativeModel('models/gemini-1.5-flash')

st.title('CSV File Reader')

# Create file uploader widget
input = st.text_input("Enter basic queries")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None and input is not None:
    st.write(input)
    df = pd.read_csv(uploaded_file)
    df_sample = df.sample(5)
    df_sample = df_sample.to_string()
    response = model.generate_content(f"""Do not provide any import statements. Do not read csv. Assume it is already loaded into variable df. If there are many unique values try to display only top 10 on the visuals. Use only plotly, matplotlib and Seaborn for visuals.
                                      Do not use any additonal libraries. 
                                      Only provide code assume dataframe is already loaded.
                                      make it such that it is displayed on streamlit website.  
                                      From the attached sample dataset,give me code for visualizations that can be generated. 
                                      The sample is attached, Based on understadninf from the sample geenrate 4 visualizations.
                                       Ensure to start each piece of code with code_start and end with code_end. Do not use plt.show use streamlit specific code to display it. reverify the code before providing the output. Ensure there are no errors as this is displayed directly.
                                        Along with this do the additional task provided by user. This is the input from user: {input}. This is a sample dataframe converted to string: {df_sample}""")
    text = response.text
    st.write(text)
    matches = re.findall(r'code_start(.*?)code_end', text, re.DOTALL)

    code_snippets = [match.strip() for match in matches]

    # Print the list of code snippets
    for i, snippet in enumerate(code_snippets, 1):
        print(f"Code snippet {i}:\n{snippet}\n")


    for i, snippet in enumerate(code_snippets, 1):
        print(f"Executing code snippet {i}...\n")
        execute_code_snippet(snippet)
        print("\n" + "="*40 + "\n")

