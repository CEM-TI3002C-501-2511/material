import dash
from dash import html, dcc, dash_table, callback, Input, Output, State
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

def bar_plot(df):
    df_total_by_day = df.groupby(df["Timestamp"].dt.floor("d"))["Total"].sum().reset_index()
    # Se puede agregar color para hacer una gráfica de barras apilada
    # Se puede agregar color y barmode="group" para hacer una gráfica de barras comparativa
    fig = px.bar(df_total_by_day, x="Timestamp", y="Total")
    return fig

def line_plot(df):
    fig = px.line(df, x="Timestamp", y="Tip")
    return fig

def pie_plot(df):
    fig = px.pie(df, names="User", values="Total", hole=0.5)
    return fig

def box_plot(df):
    fig = px.box(df, y="Tip")
    return fig

def violin_plot(df):
    # color genera un violín por cada categoría dentro de la columna elegida
    fig = px.violin(df, y="Tip")
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
        html.H2(
            className="text-xl",
            children="Gráfica de barras del total por día"
        ),
        dcc.Graph(figure=bar_plot(df)),
        html.H2(
            className="text-xl",
            children="Gráfica de líneas de las propinas por fecha"
        ),
        dcc.Graph(figure=line_plot(df)),
        html.H2(
            className="text-xl",
            children="Gráfica de pastel del total de ventas por usuario"
        ),
        dcc.Graph(figure=pie_plot(df)),
        html.H2(
            className="text-xl",
            children="Gráfica cajas de las propinas"
        ),
        dcc.Graph(figure=box_plot(df)),
        html.H2(
            className="text-xl",
            children="Gráfica de violín de las propinas"
        ),
        dcc.Graph(figure=violin_plot(df)),
        html.P("Nombre de usuario"),
        dcc.Input(type="text", className="bg-white", id="username"),
        html.P("Contraseña"),
        dcc.Input(type="password", className="bg-white"),
        html.P("Elige los usuarios que desees graficar"),
        dcc.Checklist(options=df["User"].unique(),
                      value=df["User"].unique(),
                      inline=True,
                      className="mr-4",
                      id="user checklist"),
        html.P("Elige el tipo de gráfica a crear"),
        dcc.RadioItems(options=[
            {"label": "Barras", "value": "bar"},
            {"label": "Líneas", "value": "line"}
        ], value="bar", inline=True, className="mr-4", id="plot type"),
        html.Div(id="gráfica personalizada")
    ]
)

# Output -> Elemento que se va a modificar
# Input -> Elementos que accionan nuestra función cuando hay una modificación en ellos
# State -> Lee el valor del elemento cuando se acciona la función
@callback(
    Output("gráfica personalizada", "children"),
    Input("user checklist", "value"),
    Input("plot type", "value"),
    State("username", "value"),
    # prevent_initial_call=True
)
def custom_plot(user_checklist, plot_type, username):
    df_user_filter = df[df["User"].isin(user_checklist)]
    if plot_type == "bar":
        fig = px.bar(df_user_filter, x="User", y="Total")
    else:
        fig = px.line(df_user_filter, x="Timestamp", y="Total", color="User")
    return html.Div(children=[
        html.H2(className="text-xl", children=f"Gráfica personalizada de {username}"),
        dcc.Graph(figure=fig)
    ])