import pandas as pd 
import plotly.express as px
from stringcolor import *
import dash_html_components as html
import dash
import dash_core_components as dcc    
from dash.dependencies import Input, Output 

app = dash.Dash(__name__)

def mainui():

    print("""



 __  __   ________   _________  ________      
/_/\/_/\ /_______/\ /________/\/_______/\     
\ \ \ \ \\::: _  \ \\__.::.__\/\::: _  \ \    
 \:\_\ \ \\::(_)  \ \  \::\ \   \::(_)  \ \   
  \::::_\/ \:: __  \ \  \::\ \   \:: __  \ \  
    \::\ \  \:.\ \  \ \  \::\ \   \:.\ \  \ \ 
     \__\/   \__\/\__\/   \__\/    \__\/\__\/ 
                                              
                          V1.0
 
    """)



mainui()

getdata = input(""" 

Please enter your dataset file name. 
It is recommended that you put the file inside this folder!.

filename : """)

if getdata == "":
    print(cs("Please provide a valid input.","red"))
else:
    df = pd.read_csv(getdata)
    
    
    maxy = int(input(""" 
    
      How much do you want to output?
      Just a note, this might take a longer period.
       Amount: """))


    about_data1 = input("""
    What is this data about?: """)


    about_data2 = input("""
    Project title: """)
   


def generate_table(dataframe, max_rows=maxy):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children= about_data2),
    generate_table(df)
])

if __name__ == '__main__':
    app.run_server(debug=False)


