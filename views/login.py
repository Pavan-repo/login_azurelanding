import dash
import dash_bootstrap_components as dbc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
from dash import html, dcc, Input, Output, State
from helpers.styles import *
#from app_singlepage import app
#import dash_core_components as dcc
from dash.exceptions import PreventUpdate

# Hardcoded username and password
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

# Login screen layout
def login_landing():
    return dbc.Container(
        [
            html.Br(),
            html.Br(), 
            html.Br(), 
            html.Br(),
            html.Br(),
            
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                ddsih(
                                    """Hello!👋 \nLogin to <span style="color: rgb(0,83,159)"><b>T-Req's</b></span>"""

                                ),
                                style={
                                    "font-size": 50,
                                    "textAlign": "center",
                                    "whiteSpace": "pre-wrap",
                                },
                            ), 
                        ], width="auto"
                              
                    ),
                ], justify="center"
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            
            
            
            dbc.Row(
            [
                #dbc.Col(html.Label('Username' ,style={'font-weight': 'bold', 'font-size': '20px'}),width=1),
                dbc.Col(dbc.Input( id = 'username-input',
                                    type='text',
                                    placeholder = 'Type your username',
                                    className = 'inputbox1',
                                    style = {
                                        
                                        'width':'570px',
                                        'height':"50px",
                                        'padding':"10px",
                                        "font-size":"18px",
                                        "border-width":"3px",  
                                    }
                                    ),
         
                         width=4
                        ), 
            ], 
            justify="center",
            ),
            html.Br(),
            html.Br(),
            
            dbc.Row(
            [
                #dbc.Col(html.Label('Password' ,style={'font-weight': 'bold', 'font-size': '22px'}),width=1),
                dbc.Col(dbc.Input( id = 'password-input',
                                    type='password',
                                    placeholder = 'Type your password',
                                    className = 'inputbox2',
                                    style = {
                                        
                                        'width':'570px',
                                        'height':"50px",
                                        'padding':"10px",
                                        "font-size":"18px",
                                        "border-width":"3px",
                                        
                                    }
                                    
                                    
                                    
                                    ),
                                   
                                  
                         width=4
                        ), 
            ], 
            justify="center",
            ),
            html.Br(),
            html.Br(),
            
            dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='login-output',
                        style={
                            "color": 'red',
                            "font-size": 25,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width={"size":4, "offset":0}  
                ),
            ],
            justify="center",
        ),
        
            # html.Div(id='login-output', 
            #          style={
            #              'textAlign': 'center',
            #              'color': 'red', 
            #              'font-size': '20px',
            #              'margin': '10px'
            #              }
            #          ),
             html.Br(),
             html.Br(),
             
            dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Button('Login', 
                            id= 'login-button',
                            style = badge_style,
                             color='primary',
                             ), 
                    ],width=4 
                ),
             ],
             justify='center'
        ),   
        ],
        style= CONTAINER_STYLE,
        fluid=True
    )