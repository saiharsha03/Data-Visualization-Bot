# Data visualization bot

Upload a CSV, optionally type what you want to see, and the app generates and runs charts for it using Google's Gemini model.

## How it works

`demo.py` is a Streamlit app:

1. You upload a CSV and enter a short request.
2. The app sends Gemini (`gemini-1.5-flash`) a five-row sample of the data plus your request, and asks for code for four visualizations.
3. The reply is parsed for the code blocks, which are executed to draw the charts on the page. If the data does not suit analysis, the model says so and the app shows a message instead.

Charts use Plotly, Matplotlib and Seaborn. Two sample datasets are included: `iris.csv` and `covid_19_clean_complete.csv`.

## Run it

```bash
pip install -r requirements.txt
```

Add a Gemini API key to `.streamlit/secrets.toml`:

```toml
gemini_key = "your-key"
```

```bash
streamlit run demo.py
```

## Caveat

The app runs model-generated code with `exec`. That is fine for a personal demo and unsafe for untrusted users or shared hosting.
