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
                        ddsih("""Hello!👋 \nLogin to T-Reqs"""),
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

            dbc.Row(
                dbc.Col(
                    html.A("Forgot Password?", href="#", style={"font-size": "12px", "textAlign": "center"}),
                    width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
                ),
justify="center"
            ),

        ],
        style=CONTAINER_STYLE,
        fluid=True,
    )
