import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
import dash_dangerously_set_inner_html as ddsih
from helpers.styles import *
from helpers.layout_utils import *
from dash import Dash, dcc, html, Input, Output,callback, State

#from app_singlepage import app, cache
import pandas as pd
def layout_azure_landing():
    return dbc.Container(
    [
        get_header(),
        get_logo_header(),
        html.Br(),
        html.Br(),
        html.Br(),

        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                        ddsih.DangerouslySetInnerHTML(
                                """Bitte geben Sie alle notwendigen Informationen ein, um eine Anfrage zu erstellen 🚀"""

                        ),#<span style="color: rgb(0,83,159)"><b>Submit your issue details here! 🚀📝</b></span>

                        style={
                            "font-size": "3rem",
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },   
                        ),
                    ],width="auto"
                    #{"size":10, "offset":1} ,
                ),
            ],justify="center",
        ),
        html.Br(),
        html.Br(),
        html.Br(),

            dbc.Row(
                dbc.Col(
                    html.Label(['Titel', html.Span('*', style={'color': 'red'})], 
                               style={'font-weight': 'bold', 'font-size': '20px'}),
                    width=12, md=6, lg=6, xl=5,
                ),justify="center",
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Input(id='title',
                              type='text',
                              className='input-text',
                              style=input_style_small),
                    width=12, md=6, lg=6, xl=5,
                ),
                justify="center",
            ),

        html.Br(),
        
            dbc.Row(
                dbc.Col(
                    html.Label(['Beschreibung', html.Span('*', style={'color': 'red'})], 
                               style={'font-weight': 'bold', 'font-size': '20px'}),
                    width=12, md=6, lg=6, xl=5,
                ),
                justify="center",
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Textarea(id='description',
                                 className='input-text',
                                 style=input_style),
                    width=12, md=6, lg=6, xl=5,
                ),
                justify="center",
            ),
            
        html.Br(),
        
            dbc.Row(
                dbc.Col(
                    html.Label(['Anforderer', html.Span('*', style={'color': 'red'})], 
                               style={'font-weight': 'bold', 'font-size': '20px'}),
                    width=12, md=6, lg=6, xl=5,
                ),
                justify="center",
            ),
            dbc.Row(
                dbc.Col(
                    dbc.Input(id='anforderer',
                              type='text',
                              placeholder='Name des Anforderers',
                              className='input-text',
                              style=input_style_small),
                    width=12, md=6, lg=6, xl=5,
                ),
                justify="center",
            ),
        html.Br(),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='error-output-azure',
                        style={
                            "color": 'red',
                            "font-size": 24,
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
                    dbc.Button('Anfrage erstellen', 
                            id= 'create_azure_ticket_button',
                            style = {
                                 'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                    'font-size': '20px',
                                    'line-height': 'normal',
                                       "fontWeight": 600,
                                       'text-align': 'center',
                                       'letter-spacing': 'normal',
                                       'color': '#ffffff',
                                       'background': '#0066ff',
                                       'opacity': '0.75',
                                       'width': '100%',
                                       'height': '60px',
                                       'border-radius': '20px',
                                       'border': '1px solid rgba(0, 0, 0, 0.3)',
                            },
                             color='primary',
                             ), 
                    ],                    width=8,
                    md={'size': 3, 'offset': 0},
                    lg={'size': 3, 'offset': 0},
                    xl={'size': 2, 'offset': 0},
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
                            "font-size": 24,
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
    
input_style = {
                'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                'font-size': '20px',
                'line-height': 'normal',
                'text-align': 'start',
                'letter-spacing': 'normal',
                'color': '#000000',
                'background': '#ffffff',
                'opacity': '0.75',
                'width': '100%',
                'height': '125px',
                'padding': '0px 20px',
                'border-radius': '5px',
                'border': '2px solid rgba(0, 0, 0, 0.3)',
}

input_style_small = {
                'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                'font-size': '20px',
                'line-height': 'normal',
                'text-align': 'start',
                'letter-spacing': 'normal',
                'color': '#000000',
                'background': '#ffffff',
                'opacity': '0.75',
                'width': '100%',
                'height': '48px',
                'padding': '0px 20px',
                'border-radius': '5px',
                'border': '2px solid rgba(0, 0, 0, 0.3)',
}