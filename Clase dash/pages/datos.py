import dash
from dash import html, dcc, dash_table
import dash_ag_grid as dag
import plotly.express as px
import pandas as pd

dash.register_page(__name__,
                   path="/datos",
                   title="Exploración de datos",
                   name="datos")

def load_data():
    df = pd.read_csv("tips.csv")
    df["Timestamp"] = pd.to_datetime(df["Timestamp"])
    return df

def scatter_plot(df):
    fig = px.scatter(
        df,
        x="Total",
        y="Tip",
        color="User",
        size="Tip",
        labels={"Tip": "Propina por cliente", "Total": "Total de la cuenta a pagar"}
    )
    fig.update_layout(
        xaxis = {
            "tickmode": "linear",
            "tick0": 40,
            "dtick": 10
        }
    )
    return fig

def scatter_plot_category(df):
    fig = px.scatter(
        df,
        x="Total",
        y="Tip",
        color="User",
        size="Tip",
        labels={"Tip": "Propina por cliente", "Total": "Total de la cuenta a pagar"}
    )
    fig.update_layout(
        xaxis = {
            "title": "¿Qué tan cara fue la cuenta?",
            "tickmode": "array",
            "tickvals": [40, 100, 150, 230],
            "ticktext": [
                "Baratísima",
                "Barata",
                "Cara",
                "Carísima"
            ]
        }
    )
    return fig

df = load_data()

layout = html.Div(
    className="bg-gray-100",
    children=[
        html.H1(
            className="text-4xl",
            children="Datos del proyecto"
            ),
        html.H2(
            className="text-xl",
            children="Tabla con dash_table"
        ),
        dash_table.DataTable(data=df.to_dict(orient="records"), page_size=10),
        html.H2(
            className="text-xl",
            children="Tabla con Dash AG Grid"
        ),
        dag.AgGrid(
            rowData=df.to_dict(orient="records"),
            columnDefs=[{"field": col, "sortable": True, "filter": True} for col in df.columns],
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True, "paginationPageSize": 10}
        ),
        html.H2(
            className="text-xl",
            children="Gráfica de dispersión"
        ),
        dcc.Graph(figure=scatter_plot(df)),
        html.H2(
            className="text-xl",
            children="Gráfica de dispersión con categorías"
        ),
        dcc.Graph(figure=scatter_plot_category(df)),
    ]
)