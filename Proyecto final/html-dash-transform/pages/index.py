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
)
