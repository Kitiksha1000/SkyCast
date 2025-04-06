
import pandas as pd
import gradio as gr
import joblib

# Load your model and pipeline
model = joblib.load("model2.pkl")
pipeline = joblib.load("pipeline.pkl")  # if you're using a pipeline

# Define options for dropdowns
company_options = ['RVSN USSR', 'CASC', 'VKS RF', 'NASA', 'Arianespace', 'Lockheed',
       'Sea Launch', 'General Dynamics', 'ISRO', 'Kosmotras', 'Boeing',
       'Other', 'Martin Marietta', 'SpaceX', 'ILS', 'MHI', 'Roscosmos',
       'ISA', 'ESA', 'Blue Origin', 'ULA', 'US Air Force', 'Northrop',
       'US Navy', 'ISAS', 'Eurockot']
status_options = [0, 1]
year_options = list(range(1957, 2021))
month_options = list(range(1, 13))
rocket_type_options = ['Voskhod', 'Other', 'Cosmos-2I (63SM)', 'Molniya-M /Block ML',
       'Tsyklon-3', 'Soyuz U', 'Cosmos-3M (11K65M)', 'Tsyklon-2',
       'Vostok-2M', 'Delta II 7925', 'Ariane 5 ECA',
       'Molniya-M /Block 2BL'] # add all types you use
country_options = ['Russia', 'China', 'Kazakhstan', 'USA', 'France', 'Others',
       'India', 'Japan']

def predict(company, status, year, month, rocket_type, country):
    # Create a DataFrame from input
    input_df = pd.DataFrame([{
        'Company Name': company,
        'Status Rocket': status,
        'Extracted_Year': year,
        'Extracted_Month': month,
        'Rocket_type_Grouped': rocket_type,
        'Country': country
    }])
    
    # Preprocess
    processed_input = pipeline.transform(input_df)

    # Predict
    pred = model.predict(processed_input)[0]
    result = "Yes" if pred == 1 else "No"

    return f"🚀 Mission Status Prediction: {result}"

# Create dropdown-based form
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(company_options, label="Company Name"),
        gr.Dropdown(status_options, label="Status Rocket"),
        gr.Dropdown(year_options, label="Extracted Year"),
        gr.Dropdown(month_options, label="Extracted Month"),
        gr.Dropdown(rocket_type_options, label="Rocket Type Grouped"),
        gr.Dropdown(country_options, label="Country")
    ],
    outputs=gr.Textbox(label="Prediction"),
    title="Space Mission Outcome Predictor",
    description="Fill in the mission details below to predict whether the mission will succeed."
)

demo.launch(share=True)
