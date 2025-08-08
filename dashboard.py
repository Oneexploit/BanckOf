import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import plotly.graph_objs as go
import pandas as pd
import dash_table
import numpy as np

# ایجاد اپلیکیشن Dash
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# نمونه داده‌های پیش‌بینی و عملکرد بازار
data = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2023', periods=100),
    'Price': np.random.randn(100).cumsum() + 100
})

# نمونه استراتژی خرید و فروش
trading_data = pd.DataFrame({
    'Stock': ['AAPL', 'GOOG', 'AMZN', 'TSLA'],
    'Action': ['Buy', 'Sell', 'Buy', 'Sell'],
    'Price': [150, 2800, 3400, 650],
    'Shares': [10, 5, 8, 4]
})

# طراحی داشبورد
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1("هوش مصنوعی خرید و فروش سهام", className="text-center"), width=12)
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(
            id='market-graph',
            figure={
                'data': [
                    go.Scatter(
                        x=data['Date'],
                        y=data['Price'],
                        mode='lines',
                        name='Market Price'
                    )
                ],
                'layout': go.Layout(title='روند پیش‌بینی بازار سهام')
            }
        ), width=8),
        dbc.Col(dash_table.DataTable(
            id='trading-table',
            columns=[
                {"name": "سهام", "id": "Stock"},
                {"name": "عملیات", "id": "Action"},
                {"name": "قیمت", "id": "Price"},
                {"name": "تعداد", "id": "Shares"}
            ],
            data=trading_data.to_dict('records'),
            style_table={'height': '400px', 'overflowY': 'auto'}
        ), width=4)
    ]),
    dbc.Row([
        dbc.Col(html.Div([
            html.H5("مدیریت پورتفوی شما"),
            html.P("پورتفوی شما شامل سهام X است.")
        ]), width=4),
        dbc.Col(html.Div([
            html.Button("اجرای معاملات خودکار", id='auto-trade-button', n_clicks=0),
            html.Div(id='trade-output')
        ]), width=4),
        dbc.Col(html.Div([
            html.H5("اخبار مرتبط"),
            html.P("آخرین اخبار برای تصمیم‌گیری خرید/فروش")
        ]), width=4)
    ])
])

# callback برای اجرای عملیات خرید و فروش
@app.callback(
    dash.dependencies.Output('trade-output', 'children'),
    [dash.dependencies.Input('auto-trade-button', 'n_clicks')]
)
def execute_trade(n_clicks):
    if n_clicks > 0:
        return "معاملات خودکار در حال اجرا است..."
    return ""

# اجرای سرور
if __name__ == '__main__':
    app.run_server(debug=True)
