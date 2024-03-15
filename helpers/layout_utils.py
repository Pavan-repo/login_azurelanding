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
                    "Abmelden",
                    href="/",
                    style=Ribbon_Style,
                    id="logout",
                )
            ),
        ],
        sticky="top",
        fluid=True,
        color=bg_color_2,
        id="get-login-header-navbar",
    )



def get_home_header():
    return dbc.NavbarSimple(
        [    
            dbc.NavItem(
                dbc.NavLink(
                    "Übersicht",
                    href="/Treq-overview",
                    style=Ribbon_Style,
                    id="overview",
                )
            ),
            
            dbc.NavItem(
                dbc.NavLink(
                    "Abmelden",
                    href="/",
                    style=Ribbon_Style,
                    id="home",
                )
            ),
        ],
        sticky="top",
        fluid=True,
        color=bg_color_2,
        id="get-login-header-navbar",
    )
    
def get_header():
    return dbc.NavbarSimple(
        [
            dbc.NavItem(
                dbc.NavLink(
                    "Startseite",
                    href="/Treq-home",
                    style=Ribbon_Style,
                    id="home",
                )
            ),
            
            dbc.NavItem(
                dbc.NavLink(
                    "Übersicht",
                    href="/Treq-overview",
                    style=Ribbon_Style,
                    id="overview",
                )
            ),
            
            dbc.NavItem(
                dbc.NavLink(
                    "Abmelden",
                    href="/",
                    style=Ribbon_Style,
                    id="home",
                )
            ),
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
                                    src="assets/images/tef_new_logo.png", height="55px"
                                )
                            ),
                        ],
                        align="center",
                        justify="between",
                    ),
                    href="/",
                    
                ),
            ],
            fluid=True,
        
        ),
    )

