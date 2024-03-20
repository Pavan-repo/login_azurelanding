import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import requests
import os
from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
from dotenv import find_dotenv, load_dotenv

load_dotenv()

# Initialize the Dash app
app = dash.Dash(__name__)

personal_access_token = os.getenv("PERSONAL_ACCESS_TOKEN")

organization_url = "https://dev.azure.com/NRG-Acceleration/"
project = 'NRG-Acceleration'

# Connect to Azure DevOps
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Access work item tracking client
wit_client = connection.clients.get_work_item_tracking_client()

epic_id = 1060 
area_path = 'NRG_Agile_Enablement'
work_item_type = "Issue"

def create_azure_issue(title, standort_id, ATC_nummer, trouble_id, incident_id, description):
    
    new_work_item = [
            {
               "op": "add",
                "path": "/fields/System.Title",
                "from": None,
               "value": title
            },
            {
                "op": "add",
                "path": "/fields/System.Description",
                "from": None,
                "value": f"{description}\nStandort-ID: {standort_id}\nATC-Nummer: {ATC_nummer}\nIncident-ID: {incident_id}'\nTrouble-ID:{trouble_id}"
            },
            {
                "op": "add",
                "path": "/fields/System.Parent",
                "from": None,
                "value": epic_id
            },
            {
                "op": "add",
                "path": "/relations/-",
                "value": {
                    "rel": "System.LinkTypes.Hierarchy-Reverse",
                    "url": f"{organization_url}/{project}/_apis/wit/workItems/{epic_id}",
                    "attributes": {
                        "comment": "Parent link to Epic"
                    }
                }
            },
            
            {
                "op": "add",
                "path": "/fields/System.AreaPath",
                "from": None,
                "value":f"{project}\\{area_path}" 
            }
        ]
    created_work_item = wit_client.create_work_item(project=project,document=new_work_item, type=work_item_type)
    return created_work_item

# Define layout of the web application
app.layout = html.Div([
    html.H1(':blue[Submit your request]'),
    html.Div([
        html.Label("Title"),
        dcc.Input(id='title', type='text', value=''),
        html.Label("Standort-ID"),
        dcc.Input(id='standort_id', type='text', value=''),
        html.Label("ATC-Nummer"),
        dcc.Input(id='ATC_nummer', type='text', value=''),
        html.Label("Trouble-ID"),
        dcc.Input(id='trouble_id', type='text',value=''),
        html.Label("Incident-ID"),
        dcc.Input(id='incident_id', type='text', value=''),
        html.Label("Description"),
        dcc.Input(id='description',type='text', value=''),
        html.Button('Create Work Item', id='submit-val', n_clicks=0)
    ]),
    html.Div(id='output')
])

# Callback to handle work item creation
@app.callback(
        Output('output', 'children'),
    [Input('submit-val', 'n_clicks')],
    [State('title', 'value'),
     State('standort_id', 'value'),
     State('ATC_nummer', 'value'),
     State('trouble_id', 'value'),
     State('incident_id', 'value'),
     State('description', 'value'),
     ]
)
def create_azure_issue_callback(n_clicks, title, standort_id, ATC_nummer, trouble_id, incident_id, description):
    if n_clicks and all([title, standort_id, ATC_nummer, trouble_id, incident_id, description]):
        create_issue = create_azure_issue(title, standort_id, ATC_nummer, trouble_id, incident_id, description)
        return f"Anfrage erfolgreich erstellt✔️ with ID: {create_issue.id}"

    return None

if __name__ == '__main__':
    app.run_server(debug=True)
