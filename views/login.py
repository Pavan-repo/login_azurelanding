import dash
import dash_bootstrap_components as dbc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
from dash import html, dcc, Input, Output, State
from helpers.styles import *
from helpers.layout_utils import *

# Hardcoded username and password
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

# Login screen layout
def login_landing():
    return dbc.Container(
        [   
            
            #get_login_header(),
            get_logo_header(),
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
                                    """Hello!👋 \nLogin to T-Req's"""

                                ),
                                style={
                                    "font-size": 50,
                                    "textAlign": "center",
                                    "whiteSpace": "pre-wrap",
                                },
                            ), 
                        ], width="auto"
                        #{"size":3, "offset":0}
                              
                    ),
                ], justify="center"
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            
            dbc.Row(
            [
                dbc.Col(dbc.Input( id='username-input',
                                   type='text',
                                   placeholder='Username',
                                   className='input-text',
                                   style={
                                       'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '20px',
                                       'line-height': 'normal',
                                       'text-align': 'start',
                                       'letter-spacing': 'normal',
                                       'color': '#666666',
                                       'background': '#ffffff',
                                       'opacity': '0.75',
                                       'width': '450px',
                                       'height': '68px',
                                       'padding': '0px 20px',
                                       'border-radius': '20px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                   },
                                   ),
                         width={"size":3, "offset":0} 
                        ), 
            ], 
            justify="center",
            ),
            html.Br(),
            html.Br(),
            
            dbc.Row(
            [
                dbc.Col(dbc.Input( id='password-input',
                                   type='password',
                                   placeholder='Password',
                                   className='input-text',
                                   style={
                                       'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '20px',
                                       'line-height': 'normal',
                                       'text-align': 'start',
                                       'letter-spacing': 'normal',
                                       'color': '#000000',
                                       'background': '#ffffff',
                                       'opacity': '0.75',
                                       'width': '450px',
                                       'height': '68px',
                                       'padding': '0px 20px',
                                       'border-radius': '20px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                   },
                                   ),
                         width={"size":3, "offset":0} 
                        ), 
            ], 
            justify="center",
            ),
            html.Br(),
            dbc.Row(
            [
                dbc.Col(
                    html.A("Forgot Password?", href="#", style={"font-size": "16px", 'background': '#ffffff'}),
                    width={"size":3, "offset":0}  
                ),
            ],
            justify="center",
            ),
           
            
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
                        width={"size":3, "offset":0}  
                    ),
                ],
                justify="center",
            ),
        
            html.Br(),
            html.Br(),
            
            dbc.Row(
                [
                    dbc.Col(
                        dbc.Button('Anmelden', 
                                   id='login-button',
                                   style={
                                       'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '30px',
                                       'line-height': 'normal',
                                       "fontWeight": 700,
                                       'text-align': 'center',
                                       'letter-spacing': 'normal',
                                       'color': '#ffffff',
                                       'background': '#0066ff',
                                       'opacity': '0.75',
                                       'width': '450px',
                                       'height': '68px',
                                       'border-radius': '5px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                   },
                                   color='primary',
                                   ), 
                        width={"size":3, "offset":0} 
                    ),
                ],
                justify='center'
            ),   
        ],
        style=CONTAINER_STYLE,
        fluid=True,
    )