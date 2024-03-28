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



# def get_home_header():
#     return dbc.NavbarSimple(
#         [    
#             dbc.NavItem(
#                 dbc.NavLink(
#                     "Übersicht",
#                     href="/Treq-overview",
#                     style=Ribbon_Style,
#                     id="overview",
#                 )
#             ),
            
#             dbc.NavItem(
#                 dbc.NavLink(
#                     "Abmelden",
#                     href="/",
#                     style=Ribbon_Style,
#                     id="home",
#                 )
#             ),
#         ],
#         sticky="top",
#         fluid=True,
#         color=bg_color_2,
#         id="get-login-header-navbar",
#     )
    
# def get_header():
#     return dbc.NavbarSimple(
#         [
#             dbc.NavItem(
#                 dbc.NavLink(
#                     "Startseite",
#                     href="/Treq-home",
#                     style=Ribbon_Style,
#                     id="home",
#                 )
#             ),
            
#             dbc.NavItem(
#                 dbc.NavLink(
#                     "Übersicht",
#                     href="/Treq-overview",
#                     style=Ribbon_Style,
#                     id="overview",
#                 )
#             ),
            
#             dbc.NavItem(
#                 dbc.NavLink(
#                     "Abmelden",
#                     href="/",
#                     style=Ribbon_Style,
#                     id="home",
#                 )
#             ),
#         ],
#         sticky="top",
#         fluid=True,
#         color=bg_color_2,
#         id="get-login-header-navbar",
#     )

def get_home_header():
    return dbc.Navbar(
        dbc.Container(
            [
                # Logo auf der linken Seite in einer Spalte
                dbc.Row(
                    dbc.Col(html.A(html.Img(src="assets/images/tef_new_logo.png", height="55px"), href="/")),
                    align="center",
                    className="g-0",  # Entfernt den Gap zwischen den Columns
                ),
                # Navigationslinks in einer weiteren Spalte, ausgerichtet am Ende (rechts)
                dbc.Row(
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Übersicht", href="/Treq-overview", style=Ribbon_Style, id="overview-nav")),
                                dbc.NavItem(dbc.NavLink("Abmelden", href="/", style=Ribbon_Style, id="logout-nav")),
                            ],
                            className="ms-auto",  # Schiebt die Links nach rechts
                            navbar=True,
                        ),
                        "auto",  # Ermöglicht Flexibilität in der Breiteneinstellung
                    ),
                    align="center",
                    className="g-0",
                ),
            ],
            fluid=True,
        ),
        color='light',
        dark=True,
        sticky="top",
        id="navbar",
    )

def get_header_ticket():
    return dbc.Navbar(
        dbc.Container(
            [
                # Logo auf der linken Seite in einer Spalte
                dbc.Row(
                    dbc.Col(html.A(html.Img(src="assets/images/tef_new_logo.png", height="55px"), href="/")),
                    align="center",
                    className="g-0",  # Entfernt den Gap zwischen den Columns
                ),
                # Navigationslinks in einer weiteren Spalte, ausgerichtet am Ende (rechts)
                dbc.Row(
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Startseite", href="/Treq-home", style=Ribbon_Style, id="home-nav")),
                                dbc.NavItem(dbc.NavLink("Übersicht", href="/Treq-overview", style=Ribbon_Style, id="overview-nav")),
                                dbc.NavItem(dbc.NavLink("Abmelden", href="/", style=Ribbon_Style, id="logout-nav")),
                            ],
                            className="ms-auto",  # Schiebt die Links nach rechts
                            navbar=True,
                        ),
                        "auto",  # Ermöglicht Flexibilität in der Breiteneinstellung
                    ),
                    align="center",
                    className="g-0",
                ),
            ],
            fluid=True,
        ),
        color='light',
        dark=True,
        sticky="top",
        id="navbar",
    )

def get_header_overview():
    return dbc.Navbar(
        dbc.Container(
            [
                # Logo auf der linken Seite in einer Spalte
                dbc.Row(
                    dbc.Col(html.A(html.Img(src="assets/images/tef_new_logo.png", height="55px"), href="/")),
                    align="center",
                    className="g-0",  # Entfernt den Gap zwischen den Columns
                ),
                # Navigationslinks in einer weiteren Spalte, ausgerichtet am Ende (rechts)
                dbc.Row(
                    dbc.Col(
                        dbc.Nav(
                            [
                                dbc.NavItem(dbc.NavLink("Startseite", href="/Treq-home", style=Ribbon_Style, id="home-nav")),
                                dbc.NavItem(dbc.NavLink("Abmelden", href="/", style=Ribbon_Style, id="logout-nav")),
                            ],
                            className="ms-auto",  # Schiebt die Links nach rechts
                            navbar=True,
                        ),
                        "auto",  # Ermöglicht Flexibilität in der Breiteneinstellung
                    ),
                    align="center",
                    className="g-0",
                ),
            ],
            fluid=True,
        ),
        color='light',
        dark=True,
        sticky="top",
        id="navbar",
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


