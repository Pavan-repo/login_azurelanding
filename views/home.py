import dash
import dash_bootstrap_components as dbc
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
import dash_dangerously_set_inner_html as ddsih
from helpers.styles import *
from helpers.layout_utils import *

import pandas as pd

###########################################################################################################################
# Requreid functions
###########################################################################################################################
def two_buttons_layout():

    return dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Button('Fragen zu Jira/Confluence', 
                                id='jira-confluence',
                                 color='primary', size="md",
                                 style={
                                        'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '27px',
                                       'line-height': 'normal',
                                       "fontWeight": 800,
                                       'text-align': 'center',
                                       'letter-spacing': 'normal',
                                       'color': '#ffffff',
                                       'background': '#0066ff',
                                       'opacity': '0.75',
                                       'width': '400px',
                                       'height': '60px',
                                       'border-radius': '5px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                   },
                                 href= "/Treq-azure"),
                ],#width= 3
                width={"size":2, "offset":2} 
            ),
            dbc.Col(
                [
                    dbc.Button('Report - RPM', 
                            id='rpm-report', color='primary', size="md",
                            style={
                                    'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                       'font-size': '27px',
                                       'line-height': 'normal',
                                       "fontWeight": 800,
                                       'text-align': 'center',
                                       'letter-spacing': 'normal',
                                       'color': '#ffffff',
                                       'background': '#0066ff',
                                       'opacity': '0.75',
                                       'width': '400px',
                                       'height': '60px',
                                       'border-radius': '5px',
                                       'border': '2px solid rgba(0, 0, 0, 0.3)',
                                   },
                             href= "/Treq-rpm",),
                ],width= 3
                #width={"size":4, "offset":0} 
            ),
            # dbc.Col(
            #     [
            #         dbc.Button('Ticket in RPM', 
            #                     id='RPM_create', color='primary', size="lg",
            #                     style=summary_btn_style),
            #     ], width= 3
            #     #width={"size":4, "offset":0} 
            # )
        ],
        justify='around'
    )

###########################################################################################################################
# App Layout 
###########################################################################################################################

def layout_home():
    return dbc.Container(
    [       get_home_header(),
            get_logo_header(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                ddsih.DangerouslySetInnerHTML(
                                    """ <b>\nWelcome to T-Req's</b>"""
                                ),
                                style={
                                    "font-size": 55,
                                    "textAlign": "center",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                        ],width="auto",
                    ),
                ],justify="center",
            ),
            # dbc.Row(
            #     [
            #         dbc.Col(
            #             [
            #                 html.Div(
            #                     ddsih.DangerouslySetInnerHTML(
            #                          """
            #                            One stop tool for creating all your requests 
            #                         """
            #                     ),
            #                     style={
            #                         "font-size": 30,
            #                         "textAlign": "center",
            #                     },
            #                 ),
            #             ],width="11",
            #         ),
            #     ],justify="center",
            # ),
        #     html.Div(
        #     ddsih(
        #         """Hello! \nWelcome to <span style="color: rgb(0,83,159)"><b>T-Req's</b></span>"""
        #     ),
        #     style={
        #         "font-size": 49,
        #         "textAlign": "center",
        #         "whiteSpace": "pre-wrap",
        #     },
        # # ),
        # html.Div(
        #     ddsih(
        #         """
        #         One stop tool for creating your requests 
        #         """,
        #     ),
        #     style={"font-size": 25, "textAlign": "center"},
        #     className='mb-3'
        # ),
            html.Br(),
            html.Br(),
            html.Br(),
            #html.Hr(),
            
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                ddsih.DangerouslySetInnerHTML(
                                    """ <b>Zu welchem Thema möchtest du ein Ticket erstellen?</b>"""
                                    
                                    #""" \nWelcome to <span style="color: rgb(0,83,159)"><b>T-Req's</b></span>"""
                                ),
                                style={
                                    "font-size": 35,
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
            html.Br(),
            html.Br(),
              
        

            two_buttons_layout(),

            html.Br(),
            html.Br(),

        #html.Hr()
    ],
    style=CONTAINER_STYLE,
    fluid=True,
)