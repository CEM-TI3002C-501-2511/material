import dash
import dash_svg
from dash import html

dash.register_page(__name__,
    path="/acerca",
    title="Acerca del sitio",
    name="acerca"
    )

layout = html.Div(
    className="min-h-screen bg-gray-50 flex flex-col",
    children=[
        html.Section(
            className="relative bg-cover bg-center py-24",
            style={"background-image": f"url({dash.get_asset_url('images/bg-acerca.jpg')})"},
            children=[
                html.Div(className="absolute inset-0 bg-indigo-900 opacity-75"),
                html.Div(
                    className="container mx-auto px-4 relative z-10",
                    children=[
                        html.Div(
                            className="max-w-3xl mx-auto text-center",
                            children=[
                                html.H1(
                                    className="text-4xl md:text-5xl font-bold text-white mb-4",
                                    children=["Acerca del Proyecto"],
                                ),
                                html.P(
                                    className="text-xl text-gray-200 mb-8",
                                    children=[
                                        "Conoce más sobre nuestra misión, visión y el equipo detrás de SafeCityMX."
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
        html.Main(
            className="container mx-auto py-16 px-4 flex-grow",
            children=[
                html.Div(
                    className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 p-8",
                    children=[
                        html.H2(
                            className="text-3xl font-bold mb-6 text-gray-800 text-center",
                            children=["Nuestra Plataforma"],
                        ),
                        html.Div(
                            className="prose lg:prose-lg mx-auto text-gray-600 max-w-4xl",
                            children=[
                                html.P(
                                    className="mb-4",
                                    children=[
                                        "La Plataforma Thales es una solución integral para visualización y análisis de datos, diseñada para transformar información compleja en insights accionables. Desarrollada con tecnologías de vanguardia, permite a organizaciones públicas y privadas tomar decisiones basadas en datos confiables y precisos."
                                    ],
                                ),
                                html.P(
                                    className="mb-8",
                                    children=[
                                        "Lanzada en abril de 2023, nuestra plataforma ha evolucionado rápidamente para convertirse en una herramienta esencial para instituciones que buscan mejorar la seguridad y la calidad de vida en entornos urbanos a través del análisis de datos."
                                    ],
                                ),
                                html.Div(
                                    className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8",
                                    children=[
                                        html.Div(
                                            className="text-center p-6 bg-blue-50 rounded-lg",
                                            children=[
                                                html.Div(
                                                    className="bg-blue-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="h-8 w-8 text-blue-600",
                                                            fill="none",
                                                            stroke="currentColor",
                                                            viewBox="0 0 24 24",
                                                            xmlns="http://www.w3.org/2000/svg",
                                                            children=[
                                                                dash_svg.Path(
                                                                    d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z",
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    strokeWidth="2",
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                ),
                                                html.H3(
                                                    className="text-xl font-semibold text-gray-800 mb-2",
                                                    children=["Dashboards"],
                                                ),
                                                html.P(
                                                    className="text-gray-600",
                                                    children=[
                                                        "Visualizaciones dinámicas que presentan información clave mediante gráficos interactivos y métricas en tiempo real."
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="text-center p-6 bg-green-50 rounded-lg",
                                            children=[
                                                html.Div(
                                                    className="bg-green-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="h-8 w-8 text-green-600",
                                                            fill="none",
                                                            stroke="currentColor",
                                                            viewBox="0 0 24 24",
                                                            xmlns="http://www.w3.org/2000/svg",
                                                            children=[
                                                                dash_svg.Path(
                                                                    d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    strokeWidth="2",
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                ),
                                                html.H3(
                                                    className="text-xl font-semibold text-gray-800 mb-2",
                                                    children=["Mapas"],
                                                ),
                                                html.P(
                                                    className="text-gray-600",
                                                    children=[
                                                        "Visualización geoespacial avanzada que permite identificar patrones y concentraciones de incidentes a nivel geográfico."
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="text-center p-6 bg-purple-50 rounded-lg",
                                            children=[
                                                html.Div(
                                                    className="bg-purple-100 rounded-full w-16 h-16 flex items-center justify-center mx-auto mb-4",
                                                    children=[
                                                        dash_svg.Svg(
                                                            className="h-8 w-8 text-purple-600",
                                                            fill="none",
                                                            stroke="currentColor",
                                                            viewBox="0 0 24 24",
                                                            xmlns="http://www.w3.org/2000/svg",
                                                            children=[
                                                                dash_svg.Path(
                                                                    d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z",
                                                                    strokeLinecap="round",
                                                                    strokeLinejoin="round",
                                                                    strokeWidth="2",
                                                                )
                                                            ],
                                                        )
                                                    ],
                                                ),
                                                html.H3(
                                                    className="text-xl font-semibold text-gray-800 mb-2",
                                                    children=["Predicciones"],
                                                ),
                                                html.P(
                                                    className="text-gray-600",
                                                    children=[
                                                        "Modelos de aprendizaje automático que analizan datos históricos para predecir patrones futuros y probabilidades de incidentes."
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white rounded-xl shadow-lg overflow-hidden mb-12",
                    children=[
                        html.Div(
                            className="md:flex",
                            children=[
                                html.Div(
                                    className="md:w-1/2 bg-cover bg-center h-80 md:h-auto",
                                    style={
                                        "background-image": f"url({dash.get_asset_url('images/mission-acerca.jpg')})"
                                    },
                                ),
                                html.Div(
                                    className="md:w-1/2 p-8",
                                    children=[
                                        html.H3(
                                            className="text-2xl font-bold mb-4 text-gray-800",
                                            children=["Nuestra Misión"],
                                        ),
                                        html.Div(
                                            className="prose text-gray-600",
                                            children=[
                                                html.P(
                                                    children=[
                                                        "Creemos en el poder de los datos para transformar nuestra sociedad. Nuestra misión es proporcionar herramientas accesibles y potentes que permitan:"
                                                    ]
                                                ),
                                                html.Ul(
                                                    children=[
                                                        html.Li(
                                                            children=[
                                                                "Mejorar la seguridad pública a través del análisis predictivo"
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Optimizar la asignación de recursos en entornos urbanos"
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Facilitar la toma de decisiones basadas en datos"
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Crear comunidades más seguras e inteligentes"
                                                            ]
                                                        ),
                                                    ]
                                                ),
                                                html.P(
                                                    children=[
                                                        "Trabajamos día a día para democratizar el acceso a los datos y convertirlos en un activo estratégico para instituciones públicas y privadas."
                                                    ]
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
                html.Div(
                    className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 p-8",
                    children=[
                        html.H2(
                            className="text-3xl font-bold mb-8 text-gray-800 text-center",
                            children=["Nuestro Equipo"],
                        ),
                        html.Div(
                            className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto",
                            children=[
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="w-40 h-40 rounded-full overflow-hidden mx-auto mb-4",
                                            children=[
                                                html.Img(
                                                    alt="Alejandro Méndez",
                                                    className="w-full h-full object-cover object-center",
                                                    src=dash.get_asset_url("images/team-alejandro.jpg"),
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="text-xl font-bold text-gray-800 mb-1",
                                            children=["Alejandro Méndez"],
                                        ),
                                        html.P(
                                            className="text-indigo-600 mb-3",
                                            children=["Director de Tecnología"],
                                        ),
                                        html.P(
                                            className="text-gray-600 text-sm",
                                            children=[
                                                "Experto en ciencia de datos y sistemas de inteligencia artificial con más de 15 años de experiencia en el sector."
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="w-40 h-40 rounded-full overflow-hidden mx-auto mb-4",
                                            children=[
                                                html.Img(
                                                    alt="Carmen Rodríguez",
                                                    className="w-full h-full object-cover object-center",
                                                    src=f"{dash.get_asset_url('images/team-carmen.jpg')}",
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="text-xl font-bold text-gray-800 mb-1",
                                            children=["Carmen Rodríguez"],
                                        ),
                                        html.P(
                                            className="text-indigo-600 mb-3",
                                            children=["Científica de Datos Principal"],
                                        ),
                                        html.P(
                                            className="text-gray-600 text-sm",
                                            children=[
                                                "Especialista en modelos predictivos y aprendizaje automático aplicado a seguridad urbana."
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="text-center",
                                    children=[
                                        html.Div(
                                            className="w-40 h-40 rounded-full overflow-hidden mx-auto mb-4",
                                            children=[
                                                html.Img(
                                                    alt="Roberto Vega",
                                                    className="w-full h-full object-cover object-center",
                                                    src=f"{dash.get_asset_url('images/team-roberto.jpg')}",
                                                )
                                            ],
                                        ),
                                        html.H3(
                                            className="text-xl font-bold text-gray-800 mb-1",
                                            children=["Roberto Vega"],
                                        ),
                                        html.P(
                                            className="text-indigo-600 mb-3",
                                            children=["Director de Operaciones"],
                                        ),
                                        html.P(
                                            className="text-gray-600 text-sm",
                                            children=[
                                                "Responsable de la implementación estratégica de soluciones y relaciones con instituciones públicas."
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 p-8",
                    children=[
                        html.H2(
                            className="text-3xl font-bold mb-6 text-gray-800 text-center",
                            children=["Tecnologías Utilizadas"],
                        ),
                        html.Div(
                            className="prose lg:prose-lg mx-auto text-gray-600 max-w-4xl",
                            children=[
                                html.P(
                                    className="mb-6",
                                    children=[
                                        "Nuestra plataforma se basa en tecnologías de vanguardia para ofrecer análisis avanzados y visualizaciones interactivas:"
                                    ],
                                ),
                                html.Div(
                                    className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-8",
                                    children=[
                                        html.Div(
                                            className="bg-gray-50 p-6 rounded-lg",
                                            children=[
                                                html.H3(
                                                    className="text-xl font-semibold text-gray-800 mb-3",
                                                    children=["Front-end"],
                                                ),
                                                html.Ul(
                                                    className="space-y-2",
                                                    children=[
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "HTML5 y CSS3"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "JavaScript (ES6+)"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Tailwind CSS"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Bibliotecas de Visualización (D3.js, Chart.js)"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Leaflet para mapas interactivos"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="bg-gray-50 p-6 rounded-lg",
                                            children=[
                                                html.H3(
                                                    className="text-xl font-semibold text-gray-800 mb-3",
                                                    children=["Back-end y Análisis"],
                                                ),
                                                html.Ul(
                                                    className="space-y-2",
                                                    children=[
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Python para análisis de datos"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "TensorFlow y scikit-learn"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Bases de datos SQL y NoSQL"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "APIs RESTful para integración de datos"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                        html.Li(
                                                            className="flex items-center",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600 mr-2",
                                                                    fill="currentColor",
                                                                    viewBox="0 0 20 20",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            clipRule="evenodd",
                                                                            d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z",
                                                                            fillRule="evenodd",
                                                                        )
                                                                    ],
                                                                ),
                                                                html.Span(
                                                                    children=[
                                                                        "Computación en la nube (AWS, Azure)"
                                                                    ]
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="bg-white rounded-xl shadow-lg overflow-hidden",
                    children=[
                        html.Div(
                            className="md:flex",
                            children=[
                                html.Div(
                                    className="md:w-1/2 p-8",
                                    children=[
                                        html.H3(
                                            className="text-2xl font-bold mb-6 text-gray-800",
                                            children=["Contáctenos"],
                                        ),
                                        html.P(
                                            className="text-gray-600 mb-6",
                                            children=[
                                                "¿Interesado en conocer más sobre nuestra plataforma? ¿Desea programar una demostración personalizada? Estamos aquí para ayudarle a transformar sus datos en insights valiosos."
                                            ],
                                        ),
                                        html.Div(
                                            className="space-y-4",
                                            children=[
                                                html.Div(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Div(
                                                            className="flex-shrink-0 bg-indigo-100 rounded-full p-2 mr-3",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600",
                                                                    fill="none",
                                                                    stroke="currentColor",
                                                                    viewBox="0 0 24 24",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z",
                                                                            strokeLinecap="round",
                                                                            strokeLinejoin="round",
                                                                            strokeWidth="2",
                                                                        )
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.H4(
                                                                    className="text-lg font-medium text-gray-800",
                                                                    children=["Email"],
                                                                ),
                                                                html.P(
                                                                    className="text-gray-600",
                                                                    children=[
                                                                        "contacto@thales.com"
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Div(
                                                            className="flex-shrink-0 bg-indigo-100 rounded-full p-2 mr-3",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600",
                                                                    fill="none",
                                                                    stroke="currentColor",
                                                                    viewBox="0 0 24 24",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z",
                                                                            strokeLinecap="round",
                                                                            strokeLinejoin="round",
                                                                            strokeWidth="2",
                                                                        )
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.H4(
                                                                    className="text-lg font-medium text-gray-800",
                                                                    children=[
                                                                        "Teléfono"
                                                                    ],
                                                                ),
                                                                html.P(
                                                                    className="text-gray-600",
                                                                    children=[
                                                                        "+52 (81) 1234-5678"
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="flex items-start",
                                                    children=[
                                                        html.Div(
                                                            className="flex-shrink-0 bg-indigo-100 rounded-full p-2 mr-3",
                                                            children=[
                                                                dash_svg.Svg(
                                                                    className="h-5 w-5 text-indigo-600",
                                                                    fill="none",
                                                                    stroke="currentColor",
                                                                    viewBox="0 0 24 24",
                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                    children=[
                                                                        dash_svg.Path(
                                                                            d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z",
                                                                            strokeLinecap="round",
                                                                            strokeLinejoin="round",
                                                                            strokeWidth="2",
                                                                        ),
                                                                        dash_svg.Path(
                                                                            d="M15 11a3 3 0 11-6 0 3 3 0 016 0z",
                                                                            strokeLinecap="round",
                                                                            strokeLinejoin="round",
                                                                            strokeWidth="2",
                                                                        ),
                                                                    ],
                                                                )
                                                            ],
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.H4(
                                                                    className="text-lg font-medium text-gray-800",
                                                                    children=[
                                                                        "Dirección"
                                                                    ],
                                                                ),
                                                                html.P(
                                                                    className="text-gray-600",
                                                                    children=[
                                                                        "Av. Innovación Digital 123",
                                                                        html.Br(),
                                                                        html.Span(
                                                                            children=[
                                                                                "Ciudad de Datos, TE, México"
                                                                            ]
                                                                        ),
                                                                        html.Br(),
                                                                        html.Span(
                                                                            children=[
                                                                                "CP 45678"
                                                                            ]
                                                                        ),
                                                                    ],
                                                                ),
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                html.Div(
                                    className="md:w-1/2 h-80 md:h-auto",
                                    id="map",
                                    children=[
                                        html.Img(
                                            alt="Ubicación en mapa",
                                            className="w-full h-full object-cover object-center",
                                            src=dash.get_asset_url("images/map-location.jpg"),
                                        )
                                    ],
                                ),
                            ],
                        )
                    ],
                ),
            ],
        ),
    ],
)
