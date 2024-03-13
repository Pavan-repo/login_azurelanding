import dash
import dash_bootstrap_components as dbc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML as ddsih
from dash import html

# Hardcoded username and password
VALID_USERNAME = 'admin'
VALID_PASSWORD = 'password'

# Login screen layout
def login_landing():
    return dbc.Container(
        [
            #get_login_header(),
            get_logo_header(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),
            html.Br(),

            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.Div(
                                ddsih(
                                    """Hello!👋 \nLogin to T-Req's"""
                                ),
                                style={
                                    "font-size": "50px",
                                    "textAlign": "center",
                                    "whiteSpace": "pre-wrap",
                                },
                            ),
                        ], width={"size": 10, "offset": 1}  # Centering the text within the grid
                    ),
                ], justify="center"
            ),
            html.Br(),
            html.Br(),
            html.Br(),

            dbc.Row(
                [
                    dbc.Col(dbc.Input(id='username-input',
                                      type='text',
                                      placeholder='Username',
                                      className='inputbox1',
                                      style={
                                          'font-family': 'Netflix Sans, Helvetica Neue, Segoe UI, Roboto, Ubuntu, sans-serif',
                                          'font-size': '18px',
                                          'line-height': 'normal',
                                          'text-align': 'start',
                                          'letter-spacing': 'normal',
                                          'color': '#000000',
                                          'background': '#ffffff',
                                          'opacity': '0.75',
                                          'width': '450px',
                                          'height': '68px',
                                          'padding': '0px 20px',
                                          'border-radius': '20px',
                                          'border': '2px solid rgba(0, 0, 0, 0.3)',
                                      },
                                      ),
                            width={"size": 10, "offset": 1}  # Centering the input within the grid
                            ),
                ],
                justify="center"
            ),
            html.Br(),

        ],
        style=CONTAINER_STYLE,
        fluid=True
    )

# Mock function
def get_logo_header():
    return html.Div("Your Logo", style={"textAlign": "center"})

# Mock constant
CONTAINER_STYLE = {}

# Mock function
def get_login_header():
    return html.Div("Login Header", style={"textAlign": "center"})


if __name__ == '__main__':
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.layout = login_landing()
    app.run_server(debug=True)
