html.Div(
    children=[
        html.Div(
            className="min-h-screen bg-gray-50 flex flex-col",
            children=[
                html.Section(
                    className="relative bg-cover bg-center py-32",
                    style={"background-image": "url(images/bg-index.jpg)"},
                    children=[
                        html.Div(className="absolute inset-0 bg-black opacity-60"),
                        html.Div(
                            className="container mx-auto px-4 relative z-10",
                            children=[
                                html.Div(
                                    className="max-w-2xl",
                                    children=[
                                        html.H1(
                                            className="text-4xl md:text-5xl font-bold text-white mb-4",
                                            children=["Plataforma Thales"],
                                        ),
                                        html.P(
                                            className="text-xl text-gray-200 mb-8",
                                            children=[
                                                "Una solución integral para la visualización y análisis de datos. Descubre insights valiosos a través de nuestros dashboards interactivos, mapas geoespaciales y modelos predictivos avanzados."
                                            ],
                                        ),
                                        html.A(
                                            className="bg-gradient-to-r from-blue-600 to-indigo-700 text-white font-medium py-3 px-8 rounded-lg hover:shadow-lg transition-all inline-block",
                                            href="#secciones",
                                            children=["Explorar Plataforma"],
                                        ),
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                html.Main(
                    className="container mx-auto py-16 px-4 flex-grow",
                    id="secciones",
                    children=[
                        html.H2(
                            className="text-3xl font-bold text-center mb-16 text-gray-800",
                            children=["Nuestros Servicios"],
                        ),
                        html.Div(
                            className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 md:flex h-[400px]",
                            children=[
                                html.Div(
                                    className="md:w-1/2 bg-indigo-50 overflow-hidden",
                                    children=[
                                        html.Img(
                                            alt="Dashboard Analytics",
                                            className="w-full h-full object-cover object-center hover:scale-105 transition-transform duration-500",
                                            src="images/bg-predicciones.jpg",
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="md:w-1/2 p-8 flex flex-col justify-center items-center text-center",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="text-2xl font-bold mb-4",
                                                    children=["Dashboards"],
                                                ),
                                                html.P(
                                                    className="text-gray-600 mx-auto max-w-md",
                                                    children=[
                                                        "Accede a nuestros paneles interactivos con datos en tiempo real. Visualiza estadísticas clave y métricas importantes para la toma de decisiones. Personaliza tus dashboards según tus necesidades y compártelos con tu equipo de forma sencilla."
                                                    ],
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            className="mt-6",
                                            children=[
                                                html.A(
                                                    className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-2 px-6 rounded-md inline-block font-medium hover:shadow-md transition-all transform hover:-translate-y-0.5",
                                                    href="dashboards.html",
                                                    children=["Explorar Dashboards"],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 md:flex flex-row-reverse h-[400px]",
                            children=[
                                html.Div(
                                    className="md:w-1/2 bg-green-50 overflow-hidden",
                                    children=[
                                        html.Img(
                                            alt="Mapas Geoespaciales",
                                            className="w-full h-full object-cover object-center hover:scale-105 transition-transform duration-500",
                                            src="images/bg-mapas.jpg",
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="md:w-1/2 p-8 flex flex-col justify-center items-center text-center",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="text-2xl font-bold mb-4",
                                                    children=["Mapas"],
                                                ),
                                                html.P(
                                                    className="text-gray-600 mx-auto max-w-md",
                                                    children=[
                                                        "Visualiza datos geoespaciales de forma interactiva. Nuestros mapas te permiten explorar patrones geográficos y tendencias regionales. Integra diversas fuentes de datos y visualízalos en mapas detallados con múltiples capas de información."
                                                    ],
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            className="mt-6",
                                            children=[
                                                html.A(
                                                    className="bg-gradient-to-r from-green-500 to-green-700 text-white py-2 px-6 rounded-md inline-block font-medium hover:shadow-md transition-all transform hover:-translate-y-0.5",
                                                    href="mapas.html",
                                                    children=["Ver Mapas"],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 md:flex h-[400px]",
                            children=[
                                html.Div(
                                    className="md:w-1/2 bg-amber-50 overflow-hidden",
                                    children=[
                                        html.Img(
                                            alt="Análisis Predictivo",
                                            className="w-full h-full object-cover object-center hover:scale-105 transition-transform duration-500",
                                            src="images/bg-predicciones.jpg",
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="md:w-1/2 p-8 flex flex-col justify-center items-center text-center",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="text-2xl font-bold mb-4",
                                                    children=["Predicciones"],
                                                ),
                                                html.P(
                                                    className="text-gray-600 mx-auto max-w-md",
                                                    children=[
                                                        "Descubre nuestros modelos predictivos basados en algoritmos de inteligencia artificial. Anticipa tendencias y prepárate para el futuro. Nuestras herramientas de análisis predictivo te ayudan a tomar decisiones fundamentadas en datos y a identificar oportunidades de crecimiento."
                                                    ],
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            className="mt-6",
                                            children=[
                                                html.A(
                                                    className="bg-gradient-to-r from-amber-500 to-amber-700 text-white py-2 px-6 rounded-md inline-block font-medium hover:shadow-md transition-all transform hover:-translate-y-0.5",
                                                    href="predicciones.html",
                                                    children=["Explorar Predicciones"],
                                                )
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 md:flex flex-row-reverse h-[400px]",
                            children=[
                                html.Div(
                                    className="md:w-1/2 bg-blue-50 overflow-hidden",
                                    children=[
                                        html.Img(
                                            alt="Nuestro Equipo",
                                            className="w-full h-full object-cover object-center hover:scale-105 transition-transform duration-500",
                                            src="images/bg-acerca.jpg",
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="md:w-1/2 p-8 flex flex-col justify-center items-center text-center",
                                    children=[
                                        html.Div(
                                            children=[
                                                html.H3(
                                                    className="text-2xl font-bold mb-4",
                                                    children=["Acerca del sitio"],
                                                ),
                                                html.P(
                                                    className="text-gray-600 mx-auto max-w-md",
                                                    children=[
                                                        "Conoce más sobre nuestra plataforma, nuestro equipo y nuestra misión. Información detallada sobre la tecnología detrás de nuestras soluciones y cómo podemos ayudarte a transformar tus datos en decisiones estratégicas para tu organización."
                                                    ],
                                                ),
                                            ]
                                        ),
                                        html.Div(
                                            className="mt-6",
                                            children=[
                                                html.A(
                                                    className="bg-gradient-to-r from-blue-500 to-blue-700 text-white py-2 px-6 rounded-md inline-block font-medium hover:shadow-md transition-all transform hover:-translate-y-0.5",
                                                    href="acerca.html",
                                                    children=["Más información"],
                                                )
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
            className="fixed bottom-6 right-6 z-50",
            id="chatbot-button",
            children=[
                html.Button(
                    className="bg-indigo-600 hover:bg-indigo-700 text-white rounded-full w-16 h-16 flex items-center justify-center shadow-lg transition-all hover:scale-105",
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
        ),
        html.Div(
            className="fixed bottom-6 right-6 z-50 hidden",
            id="chatbot-window",
            children=[
                html.Div(
                    className="bg-white rounded-lg shadow-xl w-80 overflow-hidden",
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
                                            src="images/Thales.png",
                                        ),
                                        html.H3(
                                            className="font-medium",
                                            children=["Asistente Thales"],
                                        ),
                                    ],
                                ),
                                html.Button(
                                    className="text-white hover:text-gray-200",
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
                        html.Div(
                            className="h-80 px-4 py-3 overflow-y-auto bg-gray-50",
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
                                                        "¡Hola! Soy el asistente virtual de Thales. ¿En qué puedo ayudarte hoy?"
                                                    ],
                                                ),
                                                html.Span(
                                                    className="text-xs text-gray-500 mt-1 block",
                                                    children=["11:30 AM"],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="flex justify-end mb-3",
                                    children=[
                                        html.Div(
                                            className="bg-indigo-600 text-white rounded-lg py-2 px-3 max-w-[80%]",
                                            children=[
                                                html.P(
                                                    className="text-sm",
                                                    children=[
                                                        "Me gustaría saber más sobre los dashboards disponibles"
                                                    ],
                                                ),
                                                html.Span(
                                                    className="text-xs text-indigo-200 mt-1 block",
                                                    children=["11:31 AM"],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="flex mb-3",
                                    children=[
                                        html.Div(
                                            className="bg-indigo-100 rounded-lg py-2 px-3 max-w-[80%]",
                                            children=[
                                                html.P(
                                                    className="text-sm text-gray-800",
                                                    children=[
                                                        "¡Claro! En nuestra sección de dashboards encontrarás paneles interactivos con visualizaciones de datos en tiempo real. Puedes personalizar los dashboards según tus necesidades de análisis. ¿Te gustaría que te muestre algunas opciones disponibles?"
                                                    ],
                                                ),
                                                html.Span(
                                                    className="text-xs text-gray-500 mt-1 block",
                                                    children=["11:32 AM"],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                                html.Div(id="chat-messages"),
                            ],
                        ),
                        html.Div(
                            className="border-t border-gray-200 px-4 py-3 bg-white",
                            children=[
                                html.Div(
                                    className="flex items-center",
                                    children=[
                                        html.Button(
                                            className="bg-indigo-600 text-white rounded-r-lg px-4 py-2 hover:bg-indigo-700 transition-colors",
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
                                        )
                                    ],
                                )
                            ],
                        ),
                    ],
                )
            ],
        ),
    ]
)
