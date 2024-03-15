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
def layout_azure_landing_rpm():
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
                                """<b>Geben sie unten die details ein, um ein Issue zu erstellen 🚀</b> """

                        ),#<span style="color: rgb(0,83,159)"><b>Submit your issue details here! 🚀📝</b></span>

                        style={
                            "font-size": 45,
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
            [
                dbc.Col(html.Label(['Titel',  html.Span('*', style={'color': 'red'})],style={'font-weight': 'bold', 'font-size': '20px'}), width=4),
                dbc.Col(dbc.Input( id = 'title-rpm',
                                    type='text',
                                    #placeholder = 'Issue title',
                                    className = 'input-text',
                            
                                    style = {
                                        
                                        'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '20px',
                                       'line-height': 'normal',
                                       'text-align': 'start',
                                       'letter-spacing': 'normal',
                                       'color': '#000000',
                                       'background': '#ffffff',
                                       'opacity': '0.75',
                                       'width': '650px',
                                       'height': '55px',
                                       'padding': '0px 20px',
                                       'border-radius': '0px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                    }
                                    ),
                         width={"size":8, "offset":4} 
                        ), 
            ], 
            justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label(['Beschreibung',  html.Span('*', style={'color': 'red'})],  style={'font-weight': 'bold', 'font-size': '20px'}), width=4),
                dbc.Col(dbc.Textarea(id = 'description-rpm',
                                     #placeholder = 'Issue description',
                                     className = 'input-text',
                                     
                                    style = {
                                        
                                      'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '20px',
                                       'line-height': 'normal',
                                       'text-align': 'start',
                                       'letter-spacing': 'normal',
                                       'color': '#000000',
                                       'background': '#ffffff',
                                       'opacity': '0.75',
                                       'width': '650px',
                                       'height': '125px',
                                       'padding': '0px 20px',
                                       'border-radius': '0px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                        
                                    }
                                     )
                        ,width={"size":8, "offset":4} 
                        )
             ], 
             justify="center",
        ),
        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(html.Label(['Anforderer',  html.Span('*', style={'color': 'red'})] ,style={'font-weight': 'bold', 'font-size': '20px'}), width=4),
                dbc.Col(dbc.Input( id = 'anforderer-rpm',
                                    type='text',
                                    placeholder = 'Name des Anforderers',
                                    className = 'input-text',
                                    
                                    style = {
                                        
                                        'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '20px',
                                       'line-height': 'normal',
                                       'text-align': 'start',
                                       'letter-spacing': 'normal',
                                       'color': '#333333',
                                       'background': '#ffffff',
                                       'opacity': '0.75',
                                       'width': '650px',
                                       'height': '45px',
                                       'padding': '0px 20px',
                                       'border-radius': '0px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                        
                                    }
                                    ),
                         width={"size":8, "offset":4} 
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
                        id='error-output-azure-rpm',
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
                    dbc.Button('Issue erstellen', 
                            id= 'create_azure_ticket_button-rpm',
                            style = {
                                 'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                    'font-size': '27px',
                                    'line-height': 'normal',
                                       "fontWeight": 800,
                                       'text-align': 'center',
                                       'letter-spacing': 'normal',
                                       'color': '#ffffff',
                                       'background': '#0066ff',
                                       'opacity': '0.75',
                                       'width': '650px',
                                       'height': '60px',
                                       'border-radius': '5px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                            },
                             color='primary',
                             ), 
                    ],width=4
                ),
             ],
             justify='center'
        ),

        html.Br(),
        
        dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='success-output-azure-rpm',
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
    


