import dash
import dash_html_components as html
import dash_table
import pandas as pd

df = pd.DataFrame({
    'Date': ['2018-08-30 22:52:25', '2021-09-29 13:33:49'],
    'Ticket ID': [1444008, 1724734],
    'Work Order': ['119846184', '122445397'],
    'Link(s)': ['[Google](https://www.google.com)', '[Twitter](https://www.twitter.com), [Facebook](https://www.facebook.com)'],
})

app = dash.Dash()

app.layout = html.Div(children=[

    dash_table.DataTable(
        data=df.to_dict(orient='records'),
        columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x == 'Link(s)' else {'id': x, 'name': x} for x in df.columns],
        style_table={'position': 'relative', 'top': '5vh', 'left': '5vw', 'width': '60vw'}
    ),

])

if __name__ == '__main__':
    app.run_server(host='127.0.0.1', debug=True)