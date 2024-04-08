import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, callback, State
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
from helpers.styles import *
from helpers.layout_utils import *
from dash.exceptions import PreventUpdate
from helpers.forms import *

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

def layout_azure_landing(inhalt="Details..."):

    tabs = dbc.Tabs(
        [
            dbc.Tab(label="Anfragetyp", active_tab_style={'font-size': '18px'}, tab_id="tab-1", children=[
                dbc.Container([
                html.Br(),
                dbc.Row(dbc.Col(html.P("   Bitte wählen Sie ihr Anliegen", style={'font-weight': 'bold', 'font-size': '20px'}), width={"size": 6, "offset": 0}), justify='center'),

                        dbc.Row(dbc.Col(dbc.Button("ENC", id="btn_enc", n_clicks=0, className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
                        dbc.Row(dbc.Col(dbc.Button("RPM", id="btn_rpm", className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
                        dbc.Row(dbc.Col(dbc.Button("Incident", id="btn_incident", className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
                        dbc.Row(dbc.Col(dbc.Button("Sonstiges", id="btn_misc", className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
            ], fluid=True),
            ]),
            dbc.Tab(label="Details", active_tab_style={'font-size': '18px'}, tab_id="tab-2", children=[
                html.Div(inhalt, id='tab-content'),
                dbc.Row(
                    dbc.Col(
                        dbc.Button('Anfrage erstellen',
                                    id='create_azure_ticket_button', 
                                    color='primary', 
                                    className='me-1', 
                                    style= btn_create_request_style),
                                    width=8, md={'size': 4, 'offset': 0}, lg={'size': 4, 'offset': 0}, xl={'size': 4, 'offset': 0},
                    ),
                    justify='center'
                ),
            ]),  # Tab 2 ist initial deaktiviert
 
        ],
        style={'fontSize': '14px'},
        id="tabs",
        #active_tab="tab-1",
    )


    tab_container = dbc.Row(
        [
            dbc.Col(
                tabs,
                width=8,
                md={'size': 8, 'offset': 0},
                lg={'size': 6, 'offset': 0},
                xl={'size': 4, 'offset': 0},
            )
        ],
        justify="center",
    )
    
    layout = dbc.Container(
        [
            get_header_ticket(),
            html.Br(),
            html.Br(),
            
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(
                        html.Div(
                            DangerouslySetInnerHTML("""Bitte geben Sie alle notwendigen Informationen ein, um eine Anfrage zu erstellen 🚀"""),
                            style={"font-size": "2rem", "textAlign": "center", "whiteSpace": "pre-wrap"},
                        ),
                        width="auto",
                    ),
                ],
                justify="center",
            ),
            html.Br(),
            html.Br(),
            html.Br(),
            tab_container,
            #tabs,

        
        
        
        ],
        style=CONTAINER_STYLE,
        fluid=True,

        
    )
    
    return layout



#app.layout = layout_azure_landing(None)



if __name__ == "__main__":
    app.run_server(debug=True)
