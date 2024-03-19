import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
import dash_dangerously_set_inner_html as ddsih
from helpers.styles import *
from helpers.layout_utils import *

import pandas as pd

def two_buttons_layout():
    return dbc.Row(
        dbc.Col(
            html.Div(
                [
                    dbc.Button(
                        'Fragen zu Jira/Confluence', 
                        id='jira-confluence',
                        color='primary', 
                        size="md",
                        style={
                            'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                            'font-size': '23px',
                            'line-height': 'normal',
                            "fontWeight": 700,
                            'text-align': 'center',
                            'letter-spacing': 'normal',
                            'color': '#ffffff',
                            'background': '#0066ff',
                            'opacity': '0.75',
                            'width': '450px',
                            'height': '63px',
                            'border-radius': '5px',
                            'border': '0px solid rgba(0, 0, 0, 0.3)',
                        },
                        href="/Treq-azure"
                    ),
                    dbc.Button(
                        'Report - RPM', 
                        id='rpm-report', 
                        color='primary', 
                        size="md",
                        style={
                            'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                            'font-size': '23px',
                            'line-height': 'normal',
                            "fontWeight": 700,
                            'text-align': 'center',
                            'letter-spacing': 'normal',
                            'color': '#ffffff',
                            'background': '#0066ff',
                            'opacity': '0.75',
                            'width': '450px',
                            'height': '61px',
                            'border-radius': '5px',
                            'border': '0px solid rgba(0, 0, 0, 0.3)',
                            'margin-left': '40px'
                        },
                        href="/Treq-rpm"
                    ),
                ],
                className='d-flex',
                style={'justify-content': 'center', 'margin': 'auto', 'width': '90%'},
            ),
            width=12,
            md={'size': 8, 'offset': 2},
            lg={'size': 6, 'offset': 3},
            xl={'size': 6, 'offset': 3},
        ),
        className='mb-3',
    )


def layout_home():
    return dbc.Container(
        [
            get_home_header(),
            get_logo_header(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                dbc.Col(
                    html.Div(
                        ddsih.DangerouslySetInnerHTML(
                            """ \nWelcome to T-Req's"""
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
            dbc.Row(
                dbc.Col(
                    html.Div(
                        ddsih.DangerouslySetInnerHTML(
                            """ <b>Zu welchem Thema möchtest du ein Ticket erstellen?</b>"""
                        ),
                        style={
                            "font-size": "3rem",
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width=12,
                    # md={'size': 8, 'offset': 2},
                    # lg={'size': 6, 'offset': 3},
                    # xl={'size': 4, 'offset': 4},
                ),
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            
            two_buttons_layout(),
            html.Br(),
            html.Br(),
        ],
        style=CONTAINER_STYLE,
        fluid=True,
    )


