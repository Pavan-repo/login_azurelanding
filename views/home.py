import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
import dash_dangerously_set_inner_html as ddsih
from helpers.styles import *
from helpers.layout_utils import *


import pandas as pd


def layout_home():
    return dbc.Container(
        [
            get_home_header(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        ddsih.DangerouslySetInnerHTML(
                            """ \nWillkommen zu T-Reqs"""
                        ),
                        style={
                            "font-size": "3.7rem",
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
            html.Br(),
            html.Br(),
            dbc.Row(
                    dbc.Col(
                        dbc.Button(
                    'Neue Anfrage erstellen', 
                    id='create_new_request',
                    color='primary', 
                    size='me-1',
                    href="/Treq-azure",
                    style=btn_selection_request_style),
                    width=8, md={'size': 4, 'offset': 0}, lg={'size': 4, 'offset': 0}, xl={'size': 3, 'offset': 0},
            ),
            justify='center'
    )
        ],
        style=CONTAINER_STYLE,
        fluid=True,
    )


