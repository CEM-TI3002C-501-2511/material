html.Div(
    className="min-h-screen bg-gray-50 flex flex-col",
    children=[
        html.Section(
            className="relative bg-cover bg-center py-24",
            style={"background-image": "url(images/bg-dashboards.jpg)"},
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
                                    children=["Dashboards Interactivos"],
                                ),
                                html.P(
                                    className="text-xl text-gray-200 mb-8",
                                    children=[
                                        "Visualiza, analiza y descubre tendencias en tiempo real con nuestros paneles interactivos."
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
                            children=["¿Cómo funcionan nuestros dashboards?"],
                        ),
                        html.Div(
                            className="prose lg:prose-lg mx-auto text-gray-600",
                            children=[
                                html.P(
                                    className="mb-4",
                                    children=[
                                        "Nuestros dashboards interactivos transforman datos complejos en visualizaciones claras e intuitivas que permiten tomar decisiones basadas en evidencia de manera rápida y efectiva."
                                    ],
                                ),
                                html.P(
                                    className="mb-4",
                                    children=[
                                        "Con funciones avanzadas de filtrado, segmentación y análisis en tiempo real, puedes personalizar la vista según tus necesidades específicas, explorar diferentes escenarios y descubrir patrones ocultos en tus datos."
                                    ],
                                ),
                                html.P(
                                    className="mb-6",
                                    children=["Estas herramientas te permiten:"],
                                ),
                                html.Ul(
                                    className="space-y-2 mb-8 list-disc pl-6",
                                    children=[
                                        html.Li(
                                            children=[
                                                "Monitorizar métricas clave de rendimiento en tiempo real"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Identificar tendencias y patrones emergentes en tus datos"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Comparar diferentes períodos de tiempo o segmentos de información"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Exportar datos e informes personalizados para su posterior análisis"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Compartir insights con tu equipo mediante enlaces directos o reportes automáticos"
                                            ]
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
                            className="bg-indigo-600 px-6 py-4",
                            children=[
                                html.H3(
                                    className="text-xl font-bold text-white",
                                    children=["Dashboard de ejemplo"],
                                )
                            ],
                        ),
                        html.Div(
                            className="p-2 bg-gray-50",
                            children=[
                                html.Div(
                                    className="aspect-w-16 aspect-h-9 w-full",
                                    children=[
                                        html.Iframe(
                                            className="border-0 rounded shadow",
                                            height="700",
                                            src="https://public.tableau.com/views/Avance1_17432065069130/Dashboard1?:showVizHome=no&:embed=true",
                                            width="100%",
                                        )
                                    ],
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="text-center",
                    children=[
                        html.P(
                            className="text-lg text-gray-600 mb-6",
                            children=[
                                "¿Listo para explorar más dashboards y descubrir los insights que tus datos pueden revelar?"
                            ],
                        ),
                        html.A(
                            className="bg-gradient-to-r from-indigo-600 to-purple-600 text-white py-3 px-8 rounded-lg inline-block font-medium hover:shadow-lg transition-all transform hover:-translate-y-0.5",
                            href="#",
                            children=["Solicitar una demostración personalizada"],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
