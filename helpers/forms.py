import dash_bootstrap_components as dbc
from dash import html
from helpers.styles import *
from helpers.layout_utils import *
from dash.exceptions import PreventUpdate


# def get_tab1_buttons():
#     tab_buttons = dbc.Container([
#                 html.Br(),
#                 dbc.Row(dbc.Col(html.P("   Bitte wählen Sie ihr Anliegen", style={'font-weight': 'bold', 'font-size': '20px'}), width={"size": 6, "offset": 0}), justify='center'),

#                         dbc.Row(dbc.Col(dbc.Button("ENC", id="btn_enc", n_clicks=0, className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
#                         dbc.Row(dbc.Col(dbc.Button("RPM", id="btn_rpm", className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
#                         dbc.Row(dbc.Col(dbc.Button("Allgemeine Anfrage", id="btn_allg", className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
#                         dbc.Row(dbc.Col(dbc.Button("Sonstiges", id="btn_sonst", className="mt-2", style=btn_selection_request_style), width={"size": 4, "offset": 0}), justify='center'),
#             ], fluid=True)
    
#     return tab_buttons

def get_form_enc():
    form_enc = dbc.Container([
                                html.Br(),
                dbc.Row(dbc.Col(html.Label(['Titel', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='title', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Standort-ID', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='location_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['ATC-Nummer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='atc_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Projekt-ID', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='project_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['NE-Nummer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='ne_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Beschreibung', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Textarea(id='description', className='input-text', style=input_style))),

                dbc.Row(dbc.Col(html.Label(['Anforderer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='anforderer', type='text', placeholder='Name des Anforderers', className='input-text', style=input_style_small))),
                html.Br(),

 
            ], fluid=True)
    return form_enc

def get_form_rpm():
    form_rpm = dbc.Container([
                                html.Br(),
                dbc.Row(dbc.Col(html.Label(['Titel', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='title', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Beschreibung', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Textarea(id='description', className='input-text', style=input_style))),

                dbc.Row(dbc.Col(html.Label(['Betroffene(r) Report(s)'], style={'font-weight': 'regular', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='location_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Anforderer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='anforderer', type='text', placeholder='Name des Anforderers', className='input-text', style=input_style_small))),
                html.Br(),

 
            ], fluid=True)
    return form_rpm
    
def get_form_incident():

    priority_dropdown = dbc.Row(
        dbc.Col(
            dcc.Dropdown(
                id='priority',
                options=[
                    {'label': 'Hoch', 'value': 'Hoch'},
                    {'label': 'Mittel', 'value': 'Mittel'},
                    {'label': 'Hinweis', 'value': 'Hinweis'}
                ],
                placeholder="Bitte Priorität auswählen",
                className='input-dropdown',
                #style
            ),
        ),
    )


    form_incident = dbc.Container([
                                html.Br(),

                priority_dropdown,
                html.Br(),
                dbc.Row(dbc.Col(html.Label(['Titel', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='title', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Standort-ID', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='location_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['ATC-Nummer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='atc_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Projekt-ID', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='project_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['NE-Nummer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='ne_id', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Beschreibung', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Textarea(id='description', className='input-text', style=input_style))),

                dbc.Row(dbc.Col(html.Label(['Anforderer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='anforderer', type='text', placeholder='Name des Anforderers', className='input-text', style=input_style_small))),
                html.Br(),

 
            ], fluid=True)
    return form_incident



def get_form_misc():

    form_sonst = dbc.Container([
                                html.Br(),
                dbc.Row(dbc.Col(html.Label(['Titel', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='title', type='text', className='input-text', style=input_style_small))),

                dbc.Row(dbc.Col(html.Label(['Beschreibung', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Textarea(id='description', className='input-text', style=input_style))),

                dbc.Row(dbc.Col(html.Label(['Anforderer', html.Span('*', style={'color': 'red'})], style={'font-weight': 'bold', 'font-size': '16px'}))),
                dbc.Row(dbc.Col(dbc.Input(id='anforderer', type='text', placeholder='Name des Anforderers', className='input-text', style=input_style_small))),
                html.Br(),

 
            ], fluid=True)

    return form_sonst