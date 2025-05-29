import dash
import dash_svg
import requests
from dash import Dash, html, dcc, callback, Input, Output, State
from datetime import datetime

backend_url = "http://localhost:8000"

external_stylesheets = []
external_scripts = [
    {"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}
]

app = Dash(__name__,
           external_stylesheets=external_stylesheets,
           external_scripts=external_scripts,
           title="Thales: Predicción de crimen",
           update_title="Cargando sitio...",
           suppress_callback_exceptions=True,
           use_pages=True)

header = html.Header(
    className="bg-white shadow-md",
    children=[
        html.Div(
            className="container mx-auto px-4 py-3 flex justify-between items-center",
            children=[
                html.Div(
                    className="flex items-center",
                    children=[
                        dcc.Link(
                            className="flex items-center",
                            href="/",
                            children=[
                                html.Img(
                                    alt="Thales Logo",
                                    className="h-12 mr-4",
                                    src=dash.get_asset_url("images/Thales.png"),
                                ),
                                html.Span(
                                    className="text-xl font-bold text-gray-800",
                                    children=["Thales"],
                                ),
                            ],
                        )
                    ],
                ),
                html.Nav(
                    children=[
                        html.Ul(
                            className="flex space-x-6",
                            children=[
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="text-gray-800 hover:text-blue-800 font-medium",
                                            href="/",
                                            children=["Inicio"],
                                            id="home-link"
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="text-gray-800 hover:text-blue-800 font-medium",
                                            href="/dashboards",
                                            children=["Dashboards"],
                                            id="dashboards-link"
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="text-gray-800 hover:text-blue-800 font-medium",
                                            href="/mapas",
                                            children=["Mapas"],
                                            id="mapas-link"
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="text-gray-800 hover:text-blue-800 font-medium",
                                            href="/predicciones",
                                            children=["Predicciones"],
                                            id="predicciones-link"
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        dcc.Link(
                                            className="text-indigo-600 hover:text-indigo-800 font-medium border-b-2 border-indigo-600",
                                            href="/acerca",
                                            children=["Acerca del sitio"],
                                            id="acerca-link"
                                        )
                                    ]
                                ),
                            ],
                        )
                    ]
                ),
            ],
        )
    ],
)

footer = html.Footer(
    className="bg-gray-800 text-white pt-12 pb-8",
    children=[
        html.Div(
            className="container mx-auto px-4",
            children=[
                html.Div(
                    className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8",
                    children=[
                        html.Div(
                            children=[
                                html.Div(
                                    className="flex items-center mb-4",
                                    children=[
                                        html.Img(
                                            alt="Thales Logo",
                                            className="h-10 mr-3",
                                            src=dash.get_asset_url("images/Thales.png"),
                                        ),
                                        html.Span(
                                            className="text-xl font-bold",
                                            children=["Thales"],
                                        ),
                                    ],
                                ),
                                html.P(
                                    className="text-gray-400 text-sm mb-6 pr-6",
                                    children=[
                                        "Plataforma integral de visualización y análisis de datos que transforma información compleja en insights accionables. Nuestra misión es hacer que el análisis de datos sea accesible para todos, permitiendo a las organizaciones tomar decisiones basadas en datos de manera más efectiva y eficiente."
                                    ],
                                ),
                                html.Div(
                                    className="flex space-x-4 mt-4",
                                    children=[
                                        dcc.Link(
                                            className="text-gray-400 hover:text-white",
                                            href="#",
                                            children=[
                                                dash_svg.Svg(
                                                    className="bi bi-facebook",
                                                    fill="currentColor",
                                                    height="20",
                                                    viewBox="0 0 16 16",
                                                    width="20",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M16 8.049c0-4.446-3.582-8.05-8-8.05C3.58 0-.002 3.603-.002 8.05c0 4.017 2.926 7.347 6.75 7.951v-5.625h-2.03V8.05H6.75V6.275c0-2.017 1.195-3.131 3.022-3.131.876 0 1.791.157 1.791.157v1.98h-1.009c-.993 0-1.303.621-1.303 1.258v1.51h2.218l-.354 2.326H9.25V16c3.824-.604 6.75-3.934 6.75-7.951z"
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dcc.Link(
                                            className="text-gray-400 hover:text-white",
                                            href="#",
                                            children=[
                                                dash_svg.Svg(
                                                    className="bi bi-twitter",
                                                    fill="currentColor",
                                                    height="20",
                                                    viewBox="0 0 16 16",
                                                    width="20",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dcc.Link(
                                            className="text-gray-400 hover:text-white",
                                            href="#",
                                            children=[
                                                dash_svg.Svg(
                                                    className="bi bi-linkedin",
                                                    fill="currentColor",
                                                    height="20",
                                                    viewBox="0 0 16 16",
                                                    width="20",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M0 1.146C0 .513.526 0 1.175 0h13.65C15.474 0 16 .513 16 1.146v13.708c0 .633-.526 1.146-1.175 1.146H1.175C.526 16 0 15.487 0 14.854V1.146zm4.943 12.248V6.169H2.542v7.225h2.401zm-1.2-8.212c.837 0 1.358-.554 1.358-1.248-.015-.709-.52-1.248-1.342-1.248-.822 0-1.359.54-1.359 1.248 0 .694.521 1.248 1.327 1.248h.016zm4.908 8.212V9.359c0-.216.016-.432.08-.586.173-.431.568-.878 1.232-.878.869 0 1.216.662 1.216 1.634v3.865h2.401V9.25c0-2.22-1.184-3.252-2.764-3.252-1.274 0-1.845.7-2.165 1.193v.025h-.016a5.54 5.54 0 0 1 .016-.025V6.169h-2.4c.03.678 0 7.225 0 7.225h2.4z"
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        dcc.Link(
                                            className="text-gray-400 hover:text-white",
                                            href="#",
                                            children=[
                                                dash_svg.Svg(
                                                    className="bi bi-instagram",
                                                    fill="currentColor",
                                                    height="20",
                                                    viewBox="0 0 16 16",
                                                    width="20",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M8 0C5.829 0 5.556.01 4.703.048 3.85.088 3.269.222 2.76.42a3.917 3.917 0 0 0-1.417.923A3.927 3.927 0 0 0 .42 2.76C.222 3.268.087 3.85.048 4.7.01 5.555 0 5.827 0 8.001c0 2.172.01 2.444.048 3.297.04.852.174 1.433.372 1.942.205.526.478.972.923 1.417.444.445.89.719 1.416.923.51.198 1.09.333 1.942.372C5.555 15.99 5.827 16 8 16s2.444-.01 3.298-.048c.851-.04 1.434-.174 1.943-.372a3.916 3.916 0 0 0 1.416-.923c.445-.445.718-.891.923-1.417.197-.509.332-1.09.372-1.942C15.99 10.445 16 10.173 16 8s-.01-2.445-.048-3.299c-.04-.851-.175-1.433-.372-1.941a3.926 3.926 0 0 0-.923-1.417A3.911 3.911 0 0 0 13.24.42c-.51-.198-1.092-.333-1.943-.372C10.443.01 10.172 0 7.998 0h.003zm-.717 1.442h.718c2.136 0 2.389.007 3.232.046.78.035 1.204.166 1.486.275.373.145.64.319.92.599.28.28.453.546.598.92.11.281.24.705.275 1.485.039.843.047 1.096.047 3.231s-.008 2.389-.047 3.232c-.035.78-.166 1.203-.275 1.485a2.47 2.47 0 0 1-.599.919c-.28.28-.546.453-.92.598-.28.11-.704.24-1.485.276-.843.038-1.096.047-3.232.047s-2.39-.009-3.233-.047c-.78-.036-1.203-.166-1.485-.276a2.478 2.478 0 0 1-.92-.598 2.48 2.48 0 0 1-.6-.92c-.109-.281-.24-.705-.275-1.485-.038-.843-.046-1.096-.046-3.233 0-2.136.008-2.388.046-3.231.036-.78.166-1.204.276-1.486.145-.373.319-.64.599-.92.28-.28.546-.453.92-.598.282-.11.705-.24 1.485-.276.738-.034 1.024-.044 2.515-.045v.002zm4.988 1.328a.96.96 0 1 0 0 1.92.96.96 0 0 0 0-1.92zm-4.27 1.122a4.109 4.109 0 1 0 0 8.217 4.109 4.109 0 0 0 0-8.217zm0 1.441a2.667 2.667 0 1 1 0 5.334 2.667 2.667 0 0 1 0-5.334z"
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ]
                        ),
                        html.Div(
                            className="grid grid-cols-1 md:grid-cols-2 gap-8",
                            children=[
                                html.Div(
                                    children=[
                                        html.H3(
                                            className="text-lg font-semibold mb-4 text-gray-200",
                                            children=["Enlaces rápidos"],
                                        ),
                                        html.Ul(
                                            className="space-y-2",
                                            children=[
                                                html.Li(
                                                    children=[
                                                        dcc.Link(
                                                            className="text-gray-400 hover:text-white transition-colors",
                                                            href="/",
                                                            children=["Inicio"],
                                                        )
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        dcc.Link(
                                                            className="text-gray-400 hover:text-white transition-colors",
                                                            href="/dashboards",
                                                            children=["Dashboards"],
                                                        )
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        dcc.Link(
                                                            className="text-gray-400 hover:text-white transition-colors",
                                                            href="/mapas",
                                                            children=["Mapas"],
                                                        )
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        dcc.Link(
                                                            className="text-gray-400 hover:text-white transition-colors",
                                                            href="/predicciones",
                                                            children=["Predicciones"],
                                                        )
                                                    ]
                                                ),
                                                html.Li(
                                                    children=[
                                                        dcc.Link(
                                                            className="text-gray-400 hover:text-white transition-colors",
                                                            href="/acerca",
                                                            children=[
                                                                "Acerca del sitio"
                                                            ],
                                                        )
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                                html.Div(
                                    children=[
                                        html.H3(
                                            className="text-lg font-semibold mb-4 text-gray-200",
                                            children=["Contacto"],
                                        ),
                                        html.Address(
                                            className="not-italic text-gray-400",
                                            children=[
                                                html.P(
                                                    className="mb-2",
                                                    children=[
                                                        "Av. Innovación Digital 123"
                                                    ],
                                                ),
                                                html.P(
                                                    className="mb-2",
                                                    children=[
                                                        "Ciudad de Datos, TE, México"
                                                    ],
                                                ),
                                                html.P(
                                                    className="mb-2",
                                                    children=["CP 45678"],
                                                ),
                                                html.P(
                                                    className="mb-2",
                                                    children=["contacto@thales.com"],
                                                ),
                                                html.P(
                                                    className="mb-2",
                                                    children=["+52 (81) 1234-5678"],
                                                ),
                                            ],
                                        ),
                                    ]
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="pt-8 border-t border-gray-700 text-center",
                    children=[
                        html.P(
                            className="text-gray-400 text-sm",
                            children=["© 2025 Thales. Todos los derechos reservados."],
                        ),
                        html.Div(
                            className="flex justify-center space-x-6 mt-4",
                            children=[
                                dcc.Link(
                                    className="text-gray-500 hover:text-gray-300 text-sm",
                                    href="#",
                                    children=["Política de privacidad"],
                                ),
                                dcc.Link(
                                    className="text-gray-500 hover:text-gray-300 text-sm",
                                    href="#",
                                    children=["Términos de uso"],
                                ),
                                dcc.Link(
                                    className="text-gray-500 hover:text-gray-300 text-sm",
                                    href="#",
                                    children=["Cookies"],
                                ),
                            ],
                        ),
                    ],
                ),
            ],
        )
    ],
)

chatbot_button = html.Div(
            className="fixed bottom-6 right-6 z-50",
            id="chatbot-button",
            children=[
                html.Button(
                    className="bg-indigo-600 hover:bg-indigo-700 text-white rounded-full w-16 h-16 flex items-center justify-center shadow-lg transition-all hover:scale-105",
                    id="open-chatbot",
                    children=[
                        dash_svg.Svg(
                            className="h-8 w-8",
                            fill="none",
                            stroke="currentColor",
                            viewBox="0 0 24 24",
                            xmlns="http://www.w3.org/2000/svg",
                            children=[
                                dash_svg.Path(
                                    d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z",
                                    strokeLinecap="round",
                                    strokeLinejoin="round",
                                    strokeWidth="2",
                                )
                            ],
                        )
                    ],
                )
            ],
        )

chatbot_window = html.Div(
            className="fixed bottom-6 right-6 z-50 hidden",
            id="chatbot-window",
            children=[
                html.Div(
                    className="bg-white rounded-lg shadow-xl w-96 overflow-hidden",
                    children=[
                        html.Div(
                            className="bg-indigo-600 text-white px-4 py-3 flex justify-between items-center",
                            children=[
                                html.Div(
                                    className="flex items-center",
                                    children=[
                                        html.Img(
                                            alt="Thales Logo",
                                            className="h-6 mr-2",
                                            src=dash.get_asset_url("images/Thales.png"),
                                        ),
                                        html.H3(
                                            className="font-medium",
                                            children=["Asistente Thales"],
                                        ),
                                    ],
                                ),
                                html.Button(
                                    className="text-white hover:text-gray-200",
                                    id="close-chatbot",
                                    children=[
                                        dash_svg.Svg(
                                            className="h-5 w-5",
                                            fill="currentColor",
                                            viewBox="0 0 20 20",
                                            xmlns="http://www.w3.org/2000/svg",
                                            children=[
                                                dash_svg.Path(
                                                    clipRule="evenodd",
                                                    d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z",
                                                    fillRule="evenodd",
                                                )
                                            ],
                                        )
                                    ],
                                ),
                            ],
                        ),
                        dcc.Loading(
                            id = "chatbot-loading",
                            children=[
                                html.Div(
                                    className="h-80 px-4 py-3 overflow-y-auto bg-gray-50",
                                    id = "chat-history",
                                    children=[
                                        html.Div(
                                            className="flex mb-3",
                                            children=[
                                                html.Div(
                                                    className="bg-indigo-100 rounded-lg py-2 px-3 max-w-[80%]",
                                                    children=[
                                                        html.P(
                                                            className="text-sm text-gray-800",
                                                            children=[
                                                                "¡Hola! Soy el asistente virtual de Thales. ¿En qué puedo ayudarte hoy? Usa el botón azul para hacer preguntas y el botón verde para interactuar con la base de datos."
                                                            ],
                                                        ),
                                                        html.Span(
                                                            className="text-xs text-gray-500 mt-1 block",
                                                            children=[datetime.now().strftime("%I:%M %p")],
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ]
                            ),
                        html.Div(
                            className="border-t border-gray-200 px-4 py-3 bg-white",
                            children=[
                                html.Div(
                                    className="flex items-center",
                                    children=[
                                        dcc.Input(
                                            className="flex-grow px-3 py-2 border rounded-l-lg focus:outline-none focus:ring-2 focus:ring-indigo-500 text-sm",
                                            type="text",
                                            placeholder="Escribe un mensaje...",
                                            id="chat-input",
                                        ),
                                        html.Button(
                                            className="bg-indigo-600 text-white px-4 py-2 hover:bg-indigo-700 transition-colors",
                                            id = "web-chat-send",
                                            children=[
                                                dash_svg.Svg(
                                                    className="h-5 w-5",
                                                    fill="currentColor",
                                                    viewBox="0 0 20 20",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M10.894 2.553a1 1 0 00-1.788 0l-7 14a1 1 0 001.169 1.409l5-1.429A1 1 0 009 15.571V11a1 1 0 112 0v4.571a1 1 0 00.725.962l5 1.428a1 1 0 001.17-1.408l-7-14z"
                                                        )
                                                    ],
                                                )
                                            ],
                                        ),
                                        html.Button(
                                            className="bg-green-600 text-white rounded-r-lg px-4 py-2 hover:bg-green-700 transition-colors ml-1",
                                            id = "db-chat-send",
                                            children=[
                                                dash_svg.Svg(
                                                    className="h-5 w-5",
                                                    fill="none",
                                                    stroke="currentColor",
                                                    viewBox="0 0 24 24",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M4 7v10c0 2 1 3 3 3h10c2 0 3-1 3-3V7c0-2-1-3-3-3H7c-2 0-3 1-3 3z",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="2",
                                                        ),
                                                        dash_svg.Path(
                                                            d="M4 7h16",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="2",
                                                        ),
                                                        dash_svg.Path(
                                                            d="M4 11h16",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="2",
                                                        ),
                                                        dash_svg.Path(
                                                            d="M4 15h16",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="2",
                                                        ),
                                                    ],
                                                )
                                            ],
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                )
            ],
        )

app.layout = html.Div(
    children= [
        dcc.Location(id="url"),
        header,
        dash.page_container,
        chatbot_button,
        chatbot_window,
        footer
    ]
)

@callback(
    Output("home-link", "className"),
    Output("dashboards-link", "className"),
    Output("mapas-link", "className"),
    Output("predicciones-link", "className"),
    Output("acerca-link", "className"),
    Input("url", "pathname")
)
def update_active_link(pathname):
    links = {
        "/": "home-link",
        "/dashboards": "dashboards-link",
        "/mapas": "mapas-link",
        "/predicciones": "predicciones-link",
        "/acerca": "acerca-link"
    }

    return [
        "text-indigo-600 hover:text-indigo-800 font-medium border-b-2 border-indigo-600" if pathname == link else "text-gray-800 hover:text-blue-800 font-medium"
        for link in links.keys()
    ]
    
@callback(
    Output("chatbot-button", "className", allow_duplicate=True),
    Output("chatbot-window", "className", allow_duplicate=True),
    Input("open-chatbot", "n_clicks"),
    prevent_initial_call=True
)
def open_chatbot(n_clicks):
    if n_clicks:
        return "fixed bottom-6 right-6 z-50 hidden", "fixed bottom-6 right-6 z-50"
    return "fixed bottom-6 right-6 z-50", "fixed bottom-6 right-6 z-50 hidden"

@callback(
    Output("chatbot-button", "className", allow_duplicate=True),
    Output("chatbot-window", "className", allow_duplicate=True),
    Input("close-chatbot", "n_clicks"),
    prevent_initial_call=True
)
def close_chatbot(n_clicks):
    if n_clicks:
        return "fixed bottom-6 right-6 z-50", "fixed bottom-6 right-6 z-50 hidden"
    return "fixed bottom-6 right-6 z-50 hidden", "fixed bottom-6 right-6 z-50"


@callback(
    Output("chat-history", "children", allow_duplicate=True),
    Output("chat-input", "value", allow_duplicate=True),
    Input("web-chat-send", "n_clicks"),
    State("chat-input", "value"),
    State("chat-history", "children"),
    prevent_initial_call=True
)
def send_web_message(n_clicks, message, chat_history):
    chat_history = chat_history or []
    chat_history.append(
        html.Div(
            className="flex justify-end mb-3",
            children=[
                html.Div(
                    className="bg-indigo-600 text-white rounded-lg py-2 px-3 max-w-[80%]",
                    children=[
                        html.P(
                            className="text-sm",
                            children=[
                                message
                            ],
                        ),
                        html.Span(
                            className="text-xs text-indigo-200 mt-1 block",
                            children=[datetime.now().strftime("%I:%M %p")],
                        ),
                    ],
                )
            ],
        )
    )
    
    try:
        json = {"query": message}
        response = requests.post(f"{backend_url}/chatbot", json=json)
        response.raise_for_status()
        reply = response.json().get("respuesta", "Lo siento, no entendí eso.")
        chat_history.append(
            html.Div(
                className="flex mb-3",
                children=[
                    html.Div(
                        className="bg-indigo-100 rounded-lg py-2 px-3 max-w-[80%]",
                        children=[
                            dcc.Markdown(
                                className="text-sm text-gray-800",
                                children=[
                                    reply
                                ],
                            ),
                            html.Span(
                                className="text-xs text-gray-500 mt-1 block",
                                children=[datetime.now().strftime("%I:%M %p")],
                            ),
                        ],
                    )
                ],
            ),
        )
    except requests.exceptions.RequestException as e:
        chat_history.append(
            html.Div(
                className="flex mb-3",
                children=[
                    html.Div(
                        className="bg-red-100 rounded-lg py-2 px-3 max-w-[80%]",
                        children=[
                            html.P(
                                className="text-sm text-red-800",
                                children=[
                                    "Error al comunicarse con el servidor."
                                ],
                            ),
                            html.Span(
                                className="text-xs text-red-500 mt-1 block",
                                children=[datetime.now().strftime("%I:%M %p")],
                            ),
                        ],
                    )
                ],
            ),
        )
    
    return chat_history, ""

@callback(
    Output("chat-history", "children", allow_duplicate=True),
    Output("chat-input", "value", allow_duplicate=True),
    Input("db-chat-send", "n_clicks"),
    State("chat-input", "value"),
    State("chat-history", "children"),
    prevent_initial_call=True
)
def send_db_message(n_clicks, message, chat_history):
    chat_history = chat_history or []
    chat_history.append(
        html.Div(
            className="flex justify-end mb-3",
            children=[
                html.Div(
                    className="bg-indigo-600 text-white rounded-lg py-2 px-3 max-w-[80%]",
                    children=[
                        html.P(
                            className="text-sm",
                            children=[
                                message
                            ],
                        ),
                        html.Span(
                            className="text-xs text-indigo-200 mt-1 block",
                            children=[datetime.now().strftime("%I:%M %p")],
                        ),
                    ],
                )
            ],
        )
    )
    try:
        json = {"query": message}
        response = requests.post(f"{backend_url}/chatbot_snowflake", json=json)
        response.raise_for_status()
        reply = response.json().get("respuesta", "Lo siento, no entendí eso.")
        chat_history.append(
            html.Div(
                className="flex mb-3",
                children=[
                    html.Div(
                        className="bg-lime-100 rounded-lg py-2 px-3 max-w-[80%]",
                        children=[
                            dcc.Markdown(
                                className="text-sm text-gray-800",
                                children=[
                                    reply
                                ],
                            ),
                            html.Span(
                                className="text-xs text-gray-500 mt-1 block",
                                children=[datetime.now().strftime("%I:%M %p")],
                            ),
                        ],
                    )
                ],
            ),
        )
    except requests.exceptions.RequestException as e:
        chat_history.append(
            html.Div(
                className="flex mb-3",
                children=[
                    html.Div(
                        className="bg-red-100 rounded-lg py-2 px-3 max-w-[80%]",
                        children=[
                            html.P(
                                className="text-sm text-red-800",
                                children=[
                                    "Error al comunicarse con el servidor."
                                ],
                            ),
                            html.Span(
                                className="text-xs text-red-500 mt-1 block",
                                children=[datetime.now().strftime("%I:%M %p")],
                            ),
                        ],
                    )
                ],
            ),
        )
    
    return chat_history, ""

if __name__ == "__main__":
    app.run(debug=True)