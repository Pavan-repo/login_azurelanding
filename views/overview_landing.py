import dash_bootstrap_components as dbc
from dash import html
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
import dash_dangerously_set_inner_html as ddsih
from helpers.styles import *
from helpers.layout_utils import *
from dash import Dash, dcc, html, Input, Output,callback, State
import dash_table
import pandas as pd
import dash
import os
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication

# Azure DevOps organization URL and personal access token
personal_access_token = os.getenv("PERSONAL_ACCESS_TOKEN")
organization_url = "https://dev.azure.com/NRG-Acceleration/"

# Connect to Azure DevOps
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)
wit_client = connection.clients.get_work_item_tracking_client()

def overview_landing():
    return dbc.Container(
        [
            #get_header(),
            #get_logo_header(),
            get_header_overview(),
            html.Br(),
            html.Br(),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                ddsih.DangerouslySetInnerHTML(
                                    """
                                    <b>Geben Sie bitte den Anforderer ein, um die erstellten Anforderungen anzuzeigen!</b>
                                    """
                                ),
                                style={
                                        "font-size": "3rem", 
                                        "textAlign": "center",
                                       # "whiteSpace": "pre-wrap",
                                },
                            ),
                        ],
                    width=12,

                    ),
                ],
               # justify="center",
            ),

            html.Br(),
            html.Br(),
            html.Br(),

            

            dbc.Row(
                dbc.Col(
                    html.Div(
                        [
                            dbc.Input(
                                id='anforderer-input',
                                type='search',
                                placeholder='Anforderer',
                                className='input-text',
                                style={
                                    'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                    'line-height': 'normal',
                                    'text-align': 'start',
                                    'opacity': '0.75',
                                    'color': '#000000',
                                    'letter-spacing': 'normal',
                                    'background': '#ffffff',
                                    'height': "48px",
                                    'padding': '0px 20px',
                                    'border-radius': '10px',
                                    'border': '1px solid rgba(0, 0, 0, 0.3)',
                                    "font-size": "20px",
                                    'margin-right': '10px',  
                                },
                            ),
                            dbc.Button(
                                html.Span([html.I(className="fa fa-search")]),
                                id='submit-button',
                                n_clicks=0,
                                style={
                                    'height': "46px",
                                    'width': "55px",
                                    "font-size": "20px",
                                    'border-radius': '10px',
                                    "backgroundColor": '#0066ff',
                                    "border": "none",
                                    "padding": 0,
                                },
                                color='primary',
                            ),
                        ],
                        className='d-flex',
                        style={'justify-content': 'center', 'margin': 'auto', 'width': '65%'},
                    ),
                    width=12,
                    md={'size': 8, 'offset': 2},
                    lg={'size': 6, 'offset': 3},
                    xl={'size': 6, 'offset': 3},
                ),
                className='mb-3',
            ),

            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            
            dbc.Row(
            [
                dbc.Col(
                    html.Div(
                        id='error-output-overview',
                        style={
                            "color": 'red',
                            "font-size": 20,
                            "textAlign": "center",
                            "whiteSpace": "pre-wrap",
                        },
                    ),
                    width={"size":4, "offset":4}  
                ),
            ],
            justify="left",
        ),
        

            html.Div(id='issue-overview-list'),
        ],
        style=CONTAINER_STYLE,
        fluid=True
    )






# Callback to fetch and display tickets based on the provided name
# @app.callback(
#     Output('issue-overview-list', 'children'),
#     [Input('submit-button', 'n_clicks')],
#     [State('anforderer-input', 'value')]
# )
# def fetch_tickets(n_clicks, anforderer):
#     if n_clicks > 0 and anforderer:
#         query = f"SELECT [System.Id], [System.WorkItemType], [System.Title], [System.Description], [System.State] FROM workitems WHERE [Microsoft.VSTS.CodeReview.ContextOwner] = '{anforderer}'"
#         tickets = wit_client.query_by_wiql({"query": query}).work_items
#         if tickets:
#             ticket_data = []
#             for ticket_ref in tickets:
#                 ticket = wit_client.get_work_item(ticket_ref.id)
#                 ticket_data.append({
#                     "Id": ticket.id,
#                     "Work Item Type": ticket.fields['System.WorkItemType'],
#                     "Title": ticket.fields['System.Title'],
#                     "Description": ticket.fields['System.Description'],
#                     "State": ticket.fields['System.State']
#                 })
#             return dash_table.DataTable(
#                         id='ticket-table',
#                         columns=[{"name": i, "id": i} for i in ticket_data[0].keys()],
#                         data=ticket_data,
#                         style_table={'overflowX': 'auto'},
#                         style_data={
#                             'whiteSpace': 'normal',
#                             'height': 'auto',
#                             'minWidth': '0px',
#                             'maxWidth': '500px',
#                             'wordBreak': 'break-word'
#                         },
#                         style_cell={
#                             'minWidth': '0px',
#                             'maxWidth': '500px',
#                             'whiteSpace': 'normal',
#                             'textAlign': 'left',
#                             'padding': '5px'
#                         },
#                         style_header={
#                             'backgroundColor': 'rgb(230, 230, 230)',
#                             'fontWeight': 'bold',
#                             'textAlign': 'center',
#                             'padding': '5px'
#                         }
#                     )
#         else:
#             return html.Div("No tickets found for the provided name.")
#     else:
#         return html.Div()

#app.layout = overview_landing


