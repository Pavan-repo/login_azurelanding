import dash
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output, State
from dash.exceptions import PreventUpdate

# Erstellen der Dash-Anwendung mit Bootstrap-Stilen
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Definieren des App-Layouts
def layout_azure_landing():
    layout = dbc.Container(
    [
        dbc.Tabs(
            [
                dbc.Tab(label="Anfragetyp", tab_id="tab-1", children=[
                    dbc.Container(
                        [
                            dbc.Button("ENC", id="btn_enc", className="mt-2"),
                            dbc.Button("RPM", id="btn_rpm", className="mt-2"),
                            dbc.Button("Allgemeine Anfrage", id="btn_allg", className="mt-2"),
                            dbc.Button("Sonstiges", id="btn_sonst", className="mt-2"),
                        ],
                        className="d-flex flex-column align-items-center justify-content-center"
                    ),
                ]),
                dbc.Tab(label="Details", tab_id="tab-2", children=[
                    html.Div(id="tab-content")
                ]),
            ],
            id="tabs",
            active_tab="tab-1",
        )
    ],
    fluid=True,
    className="py-3",
    )
    return layout

# Callback zum Wechseln der Tabs und Anzeigen des dynamischen Inhalts
@app.callback(
    [Output("tabs", "active_tab"),
     Output("tab-content", "children")],  # Rückgabe des aktualisierten Inhalts
    [Input("btn_enc", "n_clicks"),
     Input("btn_rpm", "n_clicks"),
     Input("btn_allg", "n_clicks"),
     Input("btn_sonst", "n_clicks")],
    [State("tabs", "active_tab")],  # Verwendung des aktuellen aktiven Tabs
)
def update_tab_content(btn_enc, btn_rpm, btn_allg, btn_sonst, active_tab):
    # Wenn keiner der Buttons geklickt wurde, wird eine Aktualisierung des Inhalts nicht durchgeführt
    if not any([btn_enc, btn_rpm, btn_allg, btn_sonst]):
        raise PreventUpdate

    # Initialisierung des Inhalts
    content = "Details..."

    # Überprüfen, welcher Button geklickt wurde, und den Inhalt entsprechend aktualisieren
    ctx = dash.callback_context
    if ctx.triggered:
        prop_id = ctx.triggered[0]["prop_id"].split(".")[0]
        if prop_id == "btn_enc":
            content = "Anzeigen"
        elif prop_id == "btn_rpm":
            content = "B"
        elif prop_id == "btn_allg":
            content = "C"
        elif prop_id == "btn_sonst":
            content = "D"

    # Rückgabe des aktualisierten Inhalts und des aktiven Tabs
    return "tab-2", content


app.layout = layout_azure_landing()

# Starten der Anwendung
if __name__ == "__main__":
    app.run_server(debug=True)
