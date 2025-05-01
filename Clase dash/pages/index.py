import dash
from dash import html

dash.register_page(__name__,
                   path="/",
                   title="Bienvenid@",
                   name="index")

layout = html.Div(
    children=[
        html.H1(
            className="text-4xl font-bold",
            children="Bienvenid@ a mi sitio de prueba"),
        html.P(
            className="bg-blue-100",
            children="Este es mi sitio de prueba de Dash."),
        html.Img(
            className="w-1/2",
            src=dash.get_asset_url("images/pexels-eugenia-remark-5767088-30335531.jpg"),
            alt="Frente de un café y dos personas caminando"
        )
    ]
)