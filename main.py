import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import openai
import json

client = openai.OpenAI(api_key= '')

summary = ''' 
{
    "name": "cars.csv",
    "file_name": "cars.csv",
    "dataset_description": "",
    "fields": [
        {
            "column": "Name",
            "properties": {
                "dtype": "string",
                "samples": [
                    "Nissan Altima S 4dr",
                    "Mercury Marauder 4dr",
                    "Toyota Prius 4dr (gas/electric)"
                ],
                "num_unique_values": 385,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Type",
            "properties": {
                "dtype": "category",
                "samples": [
                    "SUV",
                    "Minivan",
                    "Sports Car"
                ],
                "num_unique_values": 5,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "AWD",
            "properties": {
                "dtype": "number",
                "std": 0,
                "min": 0,
                "max": 1,
                "samples": [
                    1,
                    0
                ],
                "num_unique_values": 2,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "RWD",
            "properties": {
                "dtype": "number",
                "std": 0,
                "min": 0,
                "max": 1,
                "samples": [
                    1,
                    0
                ],
                "num_unique_values": 2,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Retail_Price",
            "properties": {
                "dtype": "number",
                "std": 19724,
                "min": 10280,
                "max": 192465,
                "samples": [
                    22775,
                    37245
                ],
                "num_unique_values": 370,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Dealer_Cost",
            "properties": {
                "dtype": "number",
                "std": 17901,
                "min": 9875,
                "max": 173560,
                "samples": [
                    18030,
                    31558
                ],
                "num_unique_values": 384,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Engine_Size__l_",
            "properties": {
                "dtype": "number",
                "std": 1.0266787710109588,
                "min": 0.0,
                "max": 6.0,
                "samples": [
                    2.2,
                    5.3
                ],
                "num_unique_values": 40,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Cyl",
            "properties": {
                "dtype": "number",
                "std": 1,
                "min": 0,
                "max": 12,
                "samples": [
                    4,
                    9
                ],
                "num_unique_values": 8,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Horsepower_HP_",
            "properties": {
                "dtype": "number",
                "std": 70,
                "min": 73,
                "max": 493,
                "samples": [
                    126,
                    138
                ],
                "num_unique_values": 100,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "City_Miles_Per_Gallon",
            "properties": {
                "dtype": "number",
                "std": 50,
                "min": 10,
                "max": 1000,
                "samples": [
                    59,
                    32
                ],
                "num_unique_values": 29,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Highway_Miles_Per_Gallon",
            "properties": {
                "dtype": "number",
                "std": 57,
                "min": -1100,
                "max": 66,
                "samples": [
                    43,
                    37
                ],
                "num_unique_values": 33,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Weight",
            "properties": {
                "dtype": "number",
                "std": 706,
                "min": 1850,
                "max": 6400,
                "samples": [
                    4473,
                    3472
                ],
                "num_unique_values": 315,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Wheel_Base",
            "properties": {
                "dtype": "number",
                "std": 8,
                "min": 0,
                "max": 130,
                "samples": [
                    110,
                    0
                ],
                "num_unique_values": 34,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Len",
            "properties": {
                "dtype": "number",
                "std": 13,
                "min": 143,
                "max": 221,
                "samples": [
                    197,
                    183
                ],
                "num_unique_values": 60,
                "semantic_type": "",
                "description": ""
            }
        },
        {
            "column": "Width",
            "properties": {
                "dtype": "number",
                "std": 4,
                "min": 2,
                "max": 81,
                "samples": [
                    72,
                    70
                ],
                "num_unique_values": 19,
                "semantic_type": "",
                "description": ""
            }
        }
    ],
    "field_names": [
        "Name",
        "Type",
        "AWD",
        "RWD",
        "Retail_Price",
        "Dealer_Cost",
        "Engine_Size__l_",
        "Cyl",
        "Horsepower_HP_",
        "City_Miles_Per_Gallon",
        "Highway_Miles_Per_Gallon",
        "Weight",
        "Wheel_Base",
        "Len",
        "Width"
    ]
}
'''

goal = "Goal(question='What is the distribution of Horsepower_HP_?', visualization='histogram of Horsepower_HP_', rationale='Analyzing the distribution of Horsepower_HP_ can provide insights into the performance capabilities and potential power differences among the car models in the dataset.', index=0)"

system_prompt = "You are a helpful assistant highly skilled in analyzing the given  dataset summary , goals and based  on it give specifications for plotting the plotly functions. you complete the template to generate configuration of the plotly function for  given  dataset  summary and the goal described. The confguration you provide MUST FOLLOW VISUALIZATION BEST PRACTICES ie. meet the specified goal,use the right visualization type, use the right data fields to plot and etc."

additional_prompt = f"The visualization config MUST only use data fields that exist in the dataset. Just genereate a json in the response which has field called plot_type , The plot type must be only of 4 types - scatter ,histogram,line,bar. And based on plot_type give additionl config fields , the additonl config fields must be the x axis or y axis or both which suits the plot.The name of the axis MUST ALWAYS be choosen from the array of columns which is . "

def generate_plot(df,config):
    if config["plot_type"] == "histogram":
        fig = px.histogram(df, x=config["x_axis"])
    elif config["plot_type"] == "scatter":
        fig = px.scatter(df, x=config["x"], y=config["y"])
    elif config["plot_type"] == "bar":
        fig = px.bar(df, x=config["x"], y=config["y"])
    elif config["plot_type"] == "line":
        fig = px.line(df,x=config["x"],y=config["y"])
    else:
        raise ValueError(f"Unsupported plot type: {config['plot_type']}")

    return fig

def generate_config(cols):
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "system", "content": f"The dataset summary is : {summary} \n\n"},
            {"role":"system","content":f"The goal is : {goal} \n\n"},
            {"role": "user","content":additional_prompt + f"{cols}" }]
    
    response = client.chat.completions.create(model="gpt-3.5-turbo",messages=messages)
    return json.loads(response.choices[0].message.content)


def main():
    df = pd.read_csv("https://raw.githubusercontent.com/uwdata/draco/master/data/cars.csv")
    config = generate_config(df.columns)
    print(config)
    print(df.columns)
    # config["x_axis"]="Horsepower(HP)"
   
    plot = generate_plot(df,config)
    plot.show()


if __name__ == "__main__":
    main()
