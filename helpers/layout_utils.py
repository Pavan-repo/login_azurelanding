# layout_utils
# functions to generate dynamic layout for dash

from helpers.styles import *

import dash_bootstrap_components as dbc
from dash import Dash ,dcc, dash_table, html, Input,Output, State

#from app_singlepage import app, cache


import pandas as pd

###########################################################################################################################


# top header
def get_login_header():
    return dbc.NavbarSimple(
        [
            dbc.NavItem(
                dbc.NavLink(
                    "Logout",
                    href="/Treq/",
                    style=Ribbon_Style,
                    id="home",
                )
            )

        ],
        sticky="top",
        fluid=True,
        color=bg_color_2,
        id="get-login-header-navbar",
    )


# logo header
def get_logo_header():
    return dbc.Navbar(
        dbc.Container(
            [
                html.A(
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Img(
                                    src="assets/images/tef_logo.png", height="75px"
                                )
                            ),
                        ],
                        align="center",
                        justify="between",
                    ),
                    href="/Treq/",
                ),
            ],
            fluid=True,
        ),
    )

