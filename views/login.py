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
                                    """Hello! \nLogin to <span style="color: rgb(0,83,159)"><b>T-Req's</b></span>"""
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
                dbc.Col(html.Label('Username' ,style={'font-weight': 'bold', 'font-size': '20px'}),width=1),
                dbc.Col(dbc.Input( id = 'username-input',
                                    type='text',
                                    placeholder = 'Enter email',
                                    className = 'inputbox1',
                                    style = {
                                        
                                        'width':'500px',
                                        'height':"45px",
                                        'padding':"10px",
                                        "font-size":"16px",
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
                dbc.Col(html.Label('Password' ,style={'font-weight': 'bold', 'font-size': '20px'}),width=1),
                dbc.Col(dbc.Input( id = 'password-input',
                                    type='password',
                                    placeholder = 'Enter password',
                                    className = 'inputbox2',
                                    style = {
                                        
                                        'width':'500px',
                                        'height':"45px",
                                        'padding':"10px",
                                        "font-size":"16px",
                                        "border-width":"3px",
                                        
                                    }
                                    
                                    
                                    
                                    ),
                                   
                                  
                         width=4
                        ), 
            ], 
            justify="center",
            ),
            html.Br(),
        
            html.Div(id='login-output', 
                     style={
                         'textAlign': 'center',
                         'color': 'red', 
                         'font-size': '20px',
                         'margin': '10px'
                         }
                     ),
            
            dbc.Row(
            [
                dbc.Col(
                    [
                    dbc.Button('Login', 
                            id= 'login-button',
                            style = badge_style,
                             color='primary',
                             ), 
                    ],width={"size":2, "offset":1} 
                ),
             ],
             justify='center'
        ),   
        ],
        style= CONTAINER_STYLE,
        fluid=True
    )



# @app.callback(
#     Output('login-output', 'children'),
#     [Input('login-button', 'n_clicks')],
#     [
#     State('username-input', 'value'),
#     State('password-input','value')
        
#     ]
    
# )
# def authenticate_user(n_clicks, username_input, password_input):
#     if n_clicks:
#         if  username_input == VALID_USERNAME and password_input == VALID_PASSWORD:
#             # Redirect to Azure landing page
#             return dcc.Location(pathname="/Treq/azure-landing", id="url")
#         else:
#             return "Invalid username or password. Please try again."
#     else:
#         raise PreventUpdate

