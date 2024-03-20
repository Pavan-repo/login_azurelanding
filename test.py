import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import requests

# Initialize the Dash app
app = dash.Dash(__name__)

# Define layout of the web application
app.layout = html.Div([
    html.H1("zu welche thema moglich"),
    dcc.Dropdown(
        id='topic-dropdown',
        options=[
            {'label': 'Fragen zu jira/confluence', 'value': 'jira_confluence'},
            {'label': 'report-RPM', 'value': 'report_RPM'},
            {'label': 'create incident', 'value': 'create_incident'}
        ],
        value=None
    ),
    html.Div(id='input-fields'),
    html.Div(id='output')
])

# Callback to update input fields based on dropdown selection
@app.callback(
    Output('input-fields', 'children'),
    [Input('topic-dropdown', 'value')]
)
def update_input_fields(topic):
    if topic == 'create_incident':
        return html.Div([
            html.Label('ATC'),
            dcc.Input(id='atc', type='text'),
            html.Label('Standort-ID'),
            dcc.Input(id='standort-id', type='text'),
            html.Label('Name'),
            dcc.Input(id='name', type='text'),
            html.Label('Incident ID'),
            dcc.Input(id='incident-id', type='text'),
            html.Label('Phone num'),
            dcc.Input(id='phone-num', type='text'),
            html.Label('Address'),
            dcc.Input(id='address', type='text'),
            html.Button('Submit', id='submit-val', n_clicks=0)
        ])
    else:
        return html.Div()

# Callback to create ticket in Azure DevOps
@app.callback(
    Output('output', 'children'),
    [Input('submit-val', 'n_clicks')],
    [State('atc', 'value'),
     State('standort-id', 'value'),
     State('name', 'value'),
     State('incident-id', 'value'),
     State('phone-num', 'value'),
     State('address', 'value')]
)
def create_ticket(n_clicks, atc, standort_id, name, incident_id, phone_num, address):
    if n_clicks > 0:
        ticket_description = f"ACT: {atc}\nStandort-ID: {standort_id}\nName: {name}\nIncident ID: {incident_id}\nPhone num: {phone_num}\nAddress: {address}"
        # Code to create ticket in Azure DevOps using REST API
        # Replace 'YOUR_AZURE_DEVOPS_URL' and 'YOUR_PERSONAL_ACCESS_TOKEN' with appropriate values
        url = '_AZURE_DEVOPS_URL/_apis/wit/workitems/$bug?api-version=6.0'
        headers = {
            
            'Content-Type': 'application/json-patch+json',
            'Authorization': 'Bearer _PERSONAL_ACCESS_TOKEN'
        }
        
        data = [
            {
                "op": "add",
                "path": "/fields/System.Title",
                "value": "New Incident"
            },
            {
                "op": "add",
                "path": "/fields/System.Description",
                "value": ticket_description
            }
        ]
        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 200:
            return html.Div('Ticket created successfully!')
        else:
            return html.Div('Error occurred while creating ticket.')
    else:
        return html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
