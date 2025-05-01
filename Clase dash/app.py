import dash
from dash import Dash, html, dcc

external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}
]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           external_scripts=external_scripts,
           title="Mi primer sitio en Dash",
           update_title="Cargando sitio...",
           use_pages=True)

nav = html.Header(className="text-blue-500",
                  children=[
                      dcc.Link(className="font-bold",
                               href="/",
                               children="Inicio"),
                      dcc.Link(className="font-bold",
                               href="/datos",
                               children="Datos"),
                      
                  ])

footer = html.Footer(
    className="bg-gray-600",
    children="Todos los derechos reservados"
)

app.layout = html.Div(
    children= [
        nav,
        dash.page_container,
        footer
    ]
)

if __name__ == "__main__":
    app.run(debug=True)