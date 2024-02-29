import flask
import dash_auth
import dash_bootstrap_components as dbc
import dash
from dash import Dash, html, dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Input, Output, State
import warnings
import pandas as pd 
pd.set_option("display.max_columns", 100)
warnings.filterwarnings("ignore")

from helpers.layout_utils import *
from helpers.create_azure_ticket import create_azure_issue

from views import login as LoginScreen, azure_ticket_landing as AzureLanding

app = Dash(
    __name__,
    title="T-Req's",
    update_title="T-Req's is working",
    serve_locally=True,
    prevent_initial_callbacks=False,
    routes_pathname_prefix="/",
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
server = app.server
app.config.suppress_callback_exceptions = True



base_layout = html.Div(
    [
        get_login_header(),
        get_logo_header(),
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
    
    elif pathname in ["/Treq-azure"]:
         return AzureLanding.layout_azure_landing()
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
            return  dcc.Location(pathname="/Treq-azure", id="url")
        else:
            return "Invalid username or password 😞. Please try again."

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
            return "required fields are missing! 😞"
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
        return f"Issue created successfully✔️ with ID: {create_issue.id}"

    return None

if __name__ == "__main__":
    app.run()