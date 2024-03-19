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
            get_logo_header(), 
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            
            dbc.Row(
                dbc.Col(
                    html.Div(
                        ddsih("""Hello!👋 <b>\nLogin to T-Reqs</b>"""),
                        style={
                            "font-size": "3rem", 
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width=12,
                    md={'size': 8, 'offset': 2},
                    lg={'size': 6, 'offset': 3},
                    xl={'size': 4, 'offset': 4},
                ),
               
            ),

            html.Br(),
            html.Br(),

            
            dbc.Row(
                dbc.Col(
                    dbc.Input(
                        id='username-input',
                        type='text',
                        placeholder='Username',
                        className='input-text',
                        style=input_style,
                    ),
                    width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
                ),
justify="center"
            ),
            
            html.Br(),
            
            dbc.Row(
                dbc.Col(
                    dbc.Input(
                        id='password-input',
                        type='password',
                        placeholder='Password',
                        className='input-text',
                        style=input_style,
                    ),
                    width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
                ),
justify="center"
            ),
            
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            id='login-output',
                            style={
                                "color": 'red',
                                "font-size": 20,
                                "textAlign": "center",
                                "whiteSpace": "pre-wrap",
                            },
                        ),
                        width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
                    ),
                ],
justify="center",
            ),
            
            html.Br(),
            
             dbc.Row(
                dbc.Col(
                    html.A("Forgot Password?", href="#", style={"font-size": "14px", "textAlign": "center"}),
                    width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
                ),
justify="center"
            ),
             
             html.Br(),
             html.Br(),
             
             
            
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        'Anmelden',
                        id='login-button',
                        color='primary',
                        style=button_style,
                    ),
                    width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
                ),
justify="center"
            ),

            html.Br(),

           

        ],
        style=CONTAINER_STYLE,
        fluid=True,
    )

input_style = {
    'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
    'font-size': '20px',
    'text-align': 'start',
    'color': '#666666',
    'background': '#ffffff',
    'opacity': '0.75',
    'width': '100%',
    'height': '48px',
    'padding': '0px 20px',
    'border-radius': '20px',
    'border': '2px solid rgba(0, 0, 0, 0.3)',
}

button_style = {
    'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
    'font-size': '18px',
    'fontWeight': 500,
    'color': '#ffffff',
    'background': '#0066ff',
    'opacity': '0.75',
    'width': '100%',
    'height': '48px',
    'border-radius': '5px',
    'border': '2px solid rgba(0, 0, 0, 0.3)',
}
