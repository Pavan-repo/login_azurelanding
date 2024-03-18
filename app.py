import flask
import dash_auth
import dash_bootstrap_components as dbc
import dash
from dash import Dash, html, dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import warnings
import pandas as pd

#from .views import overview_landing as Overview 
pd.set_option("display.max_columns", 100)
warnings.filterwarnings("ignore")

from helpers.layout_utils import *
from views.overview_landing import *
from helpers.create_azure_ticket import create_azure_issue

from views import login as LoginScreen, azure_ticket_landing as AzureLanding, azure_ticket_landing_rpm as RpmLanding, home as HomeScreen, overview_landing as Overview

app = Dash(
    __name__,
    title="T-Req's",
    external_stylesheets=[dbc.themes.BOOTSTRAP, "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css"],
    update_title="T-Req's is working",
    serve_locally=True,
    prevent_initial_callbacks=False,
    routes_pathname_prefix="/",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1, maximum-scale=1.0, maximum-scale=1.2, minimum-scale=0.5"}],
)
server = app.server
app.config.suppress_callback_exceptions = True



base_layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        html.Div(id='page-content', style=base_div_style),
        dcc.Store(id="currentpage_store", storage_type="session"),
    ],
    style=CONTAINER_STYLE,
)
app.layout = base_layout

# Callback to render different pages based on URL
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def render_page_content(pathname):
    if pathname in ["/"]:
        return LoginScreen.login_landing()
    
    elif pathname in ["/Treq-home"]:
         return HomeScreen.layout_home()
    
    elif pathname in ["/Treq-azure"]:
         return AzureLanding.layout_azure_landing()
     
    elif pathname in ["/Treq-rpm"]:
         return RpmLanding.layout_azure_landing_rpm()
    
    elif pathname in ["/Treq-overview"]:
         return Overview.overview_landing()
    else:
        return None

#  callback for login authentication
@app.callback(
    Output('login-output', 'children'),
    [Input('login-button', 'n_clicks')],
    [State('username-input', 'value'),
     State('password-input', 'value')]
)
def authenticate_user(n_clicks, username_input, password_input):
    if n_clicks:
        if  username_input == 'admin' and password_input == 'password':
            # Redirect to Azure landing page,
            return  dcc.Location(pathname="/Treq-home", id="url")
        else:
            return "Falscher Benutzername oder Passwort 😞. Bitte versuchen Sie es erneut."

# callback for ticket submission
@app.callback(
    Output('error-output-azure', 'children'),
    [Input('create_azure_ticket_button', 'n_clicks')],
    [State('title', 'value'),
     State('description', 'value'),
     State('anforderer', 'value'),
    ]
)
def validate_inputs(n_clicks, title, description, anforderer):
    if n_clicks:
        if not all([title, description, anforderer]):
            return "Bitte alle benötigten Felder ausfüllen"
    else:
        return None


@app.callback(
        Output('success-output-azure','children'),
    [Input('create_azure_ticket_button', 'n_clicks')],
    [   
        State('title', 'value'),
        State('description', 'value'),
        State('anforderer', 'value'),
        
    ]

)

def create_azure_issue_callback(n_clicks, title, description, anforderer):
    if n_clicks and all([title, description, anforderer]):
        create_issue = create_azure_issue(title, description, anforderer)
        return f"Issue erfolgreich erstellt✔️ with ID: {create_issue.id}"

    return None



@app.callback(
    [Output('error-output-overview', 'children'),
     Output('issue-overview-list', 'children')],
    [Input('submit-button', 'n_clicks')],
    [State('anforderer-input', 'value')]
)
def fetch_tickets_and_validate(n_clicks, anforderer):
    if n_clicks > 0:
        if not anforderer:
            return "Bitte geben Sie den Anforderer-Namen ein.", None
        else:
            query = f"SELECT [System.Id], [System.WorkItemType], [System.Title], [System.Description], [System.State], [System.AssignedTo] FROM workitems WHERE [Microsoft.VSTS.CodeReview.ContextOwner] = '{anforderer}'"
            issues = wit_client.query_by_wiql({"query": query}).work_items
            #link_prefix = "https://dev.azure.com/NRG-Acceleration/NRG-Acceleration/_workitems/edit/"
            if issues:
                issue_data = []
                for issue_ref in issues:
                    issue = wit_client.get_work_item(issue_ref.id)
                    #print("Available fields:", issue.fields.keys())
                    assigned_to = issue.fields.get('System.AssignedTo', {}).get('displayName', 'Not Assigned')  # Getting assigned user's display name or 'Not Assigned' if it is empty
                    #link = f"[{issue.id}]({link_prefix}{issue.id})"
                    issue_data.append({
                        "Id": issue.id,
                        #"Id": link,
                        "WorkItem Type": issue.fields['System.WorkItemType'],
                        "Title": issue.fields['System.Title'],
                        "Description": issue.fields['System.Description'],
                        "State": issue.fields['System.State'],
                        "Assigned to": assigned_to,
                        
                    })
                    
                table = dash_table.DataTable(
                    id='ticket-table',
                    columns=[{"name": i, "id": i} if i == 'Id' else {"name": i, "id": i} for i in issue_data[0].keys()],
                    data=issue_data,
                    editable=False,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="multi",
                    #row_selectable="multi",
                    row_deletable=True,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current= 0,
                    page_size= 5,
                    style_table={'overflowX': 'auto'},
                    style_data={
                        'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                        'line-height': 'normal',
                        'text-align': 'start',
                        'letter-spacing': 'normal',
                        'color': '#000000',
                        'background': '#ffffff',
                        #'opacity': '0.75',
                        #'width': '650px',
                       # 'height': '45px',
                        'padding': '0px 20px',
                        #'border-radius': '0px',
                        'border': '1px solid rgba(0, 0, 0, 0.1)',
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        "font-size":"20px",
                        'minWidth': '0px',
                        'maxWidth': '300px',
                        #'wordBreak': 'break-word'
                    },
                    style_cell={
                        'minWidth': '0px',
                        'maxWidth': '200px',
                        #'opacity': '0.95',
                        'whiteSpace': 'normal',
                        'textAlign': 'left',
                        'padding': '5px'
                    },
                    style_header={
                        'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                        'backgroundColor': 'rgb(0,83,159)',
                        'color':'#ffffff',
                        'fontWeight': 'bold',
                        "font-size":"20px",
                        'textAlign': 'left',
                        'padding': '5px'
                    },
                    style_data_conditional=[
        {
            'if': {'column_id': 'State', 'filter_query': '{State} eq "Done"'},
            'backgroundColor': '#00FF00'  # Green color for Done
        },
        {
            'if': {'column_id': 'State', 'filter_query': '{State} eq "Doing"'},
            'backgroundColor': '#FFA500'  # Orange color for Doing
        },
        {
            'if': {'column_id': 'State', 'filter_query': '{State} eq "To Do"'},
            'backgroundColor': '#808080'  # Grey color for To Do
        }
    ]
         
                
                )
                
                return None, table
            else:
                return f"Es wurden keine Tickets für den angegebenen Namen gefunden '{anforderer}'.", None
    else:
        return None, None


if __name__ == "__main__":
    app.run()