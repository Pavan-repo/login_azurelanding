import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
import dash_dangerously_set_inner_html as ddsih
from helpers.styles import *
from dash import Dash, dcc, html, Input, Output,callback, State

#from app_singlepage import app, cache
import pandas as pd
def layout_azure_landing():
    return dbc.Container(
    [
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                        ddsih.DangerouslySetInnerHTML(
                                """<span style="color: rgb(0,83,159)"><b>Submit your issue details here! 🚀 </b></span>"""

                        ),#<span style="color: rgb(0,83,159)"><b>Submit your issue details here! 🚀📝</b></span>

                        style={
                            "font-size": 49,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },   
                        ),
                    ],width="auto",
                ),
            ],justify="center",
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        
        
        dbc.Row(
            [
                dbc.Col(html.Label(['Title',  html.Span('*', style={'color': 'red'})],style={'font-weight': 'bold', 'font-size': '20px'}), width=5),
                dbc.Col(dbc.Input( id = 'title',
                                    type='text',
                                    placeholder = 'Enter title',
                                    className = 'input-text',
                            
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"55px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                    ),
                         width={"size":11, "offset":6} 
                        ), 
            ], 
            justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label(['Description',  html.Span('*', style={'color': 'red'})],  style={'font-weight': 'bold', 'font-size': '20px'}), width=5),
                dbc.Col(dbc.Textarea(id = 'description',
                                     placeholder = 'Enter description',
                                     className = 'input-text',
                                     
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"75px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                     )
                        ,width={"size":11, "offset":6} )
             ], 
             justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label(['Anforderer',  html.Span('*', style={'color': 'red'})] ,style={'font-weight': 'bold', 'font-size': '20px'}), width=5),
                dbc.Col(dbc.Input( id = 'anforderer',
                                    type='text',
                                    placeholder = 'Enter your name',
                                    className = 'input-text',
                                    
                                    style = {
                                        
                                        'width':'700px',
                                        'height':"45px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"1px",
                                        
                                    }
                                    ),
                         width={"size":11, "offset":6} 
                        ), 
            ], 
            justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='error-output-azure',
                        style={
                            "color": 'red',
                            "font-size": 30,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width={"size":4, "offset":4}  
                ),
            ],
            justify="left",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Button('Create Ticket', 
                            id= 'create_azure_ticket_button',
                             style = badge_style,
                             color='primary',
                             ), 
                    ],width={"size":5, "offset":3} 
                ),
             ],
             justify='center'
        ),

        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='success-output-azure',
                        style={
                            "color": 'green',
                            "font-size": 30,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width={"size":4, "offset":4} 
                ),
            ],
            justify="left",
        ),
         
        
    ],
    style=CONTAINER_STYLE,
    fluid=True
)
    
###########################################################################################################################
# Call backs
###########################################################################################################################

# @app.callback(
#     Output('error-output-azure', 'children'),
#     [
#         Input('create_azure_ticket_button', 'n_clicks'),
#     ],
#     [   
#         State('title', 'value'),
#         State('description', 'value'),
#         State('anforderer', 'value'),
#         State('story_points', 'value'),
#         State('type_picker', 'value'),
#     ]
# )
# def validate_inputs(n_clicks, title, description, anforderer ,story_points, type_picker):
#     if n_clicks:
#         if not all ([title, description, anforderer, story_points, type_picker]):
#             return "Please enter text in all the fields."
#         else:
#             #create_azure_issue(title, description, anforderer, story_points, type_picker)
#             return None 


