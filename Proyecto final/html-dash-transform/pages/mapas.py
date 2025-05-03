html.Div(
    className="min-h-screen bg-gray-50 flex flex-col",
    children=[
        html.Section(
            className="relative bg-cover bg-center py-24",
            style={"background-image": "url(images/bg-mapas.jpg)"},
            children=[
                html.Div(className="absolute inset-0 bg-green-900 opacity-75"),
                html.Div(
                    className="container mx-auto px-4 relative z-10",
                    children=[
                        html.Div(
                            className="max-w-3xl mx-auto text-center",
                            children=[
                                html.H1(
                                    className="text-4xl md:text-5xl font-bold text-white mb-4",
                                    children=["Mapas Interactivos"],
                                ),
                                html.P(
                                    className="text-xl text-gray-200 mb-8",
                                    children=[
                                        "Explora y analiza datos geográficos para identificar patrones y tendencias en diferentes zonas."
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
                            children=["Mapas de Seguridad"],
                        ),
                        html.Div(
                            className="prose lg:prose-lg mx-auto text-gray-600",
                            children=[
                                html.P(
                                    className="mb-4",
                                    children=[
                                        "Nuestros mapas interactivos de seguridad te permiten visualizar y analizar los diferentes niveles de seguridad en la Ciudad de México, desglosados por alcaldías y colonias."
                                    ],
                                ),
                                html.P(
                                    className="mb-4",
                                    children=[
                                        "Con datos actualizados y análisis históricos, estos mapas ofrecen una visión integral de las tendencias de seguridad en diferentes zonas de la ciudad, permitiéndote identificar áreas de mayor y menor riesgo."
                                    ],
                                ),
                                html.P(
                                    className="mb-6",
                                    children=[
                                        "Características principales de nuestros mapas:"
                                    ],
                                ),
                                html.Ul(
                                    className="space-y-2 mb-8 list-disc pl-6",
                                    children=[
                                        html.Li(
                                            children=[
                                                "Visualización por código de colores según nivel de seguridad"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Filtrado por tipo de incidente y período de tiempo"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Comparativa histórica para analizar tendencias"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Datos actualizados mensualmente con información oficial"
                                            ]
                                        ),
                                        html.Li(
                                            children=[
                                                "Posibilidad de hacer zoom en áreas específicas para análisis detallado"
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
                            className="bg-green-600 px-6 py-4",
                            children=[
                                html.H3(
                                    className="text-xl font-bold text-white",
                                    children=[
                                        "Mapa de Seguridad de la Ciudad de México"
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="p-6 bg-gray-50",
                            children=[
                                html.Div(
                                    className="aspect-w-16 aspect-h-9 w-full bg-gray-200 rounded-lg flex items-center justify-center",
                                    children=[
                                        html.Div(
                                            className="text-center p-8",
                                            children=[
                                                dash_svg.Svg(
                                                    className="h-24 w-24 mx-auto text-gray-400 mb-4",
                                                    fill="none",
                                                    stroke="currentColor",
                                                    viewBox="0 0 24 24",
                                                    xmlns="http://www.w3.org/2000/svg",
                                                    children=[
                                                        dash_svg.Path(
                                                            d="M9 20l-5.447-2.724A1 1 0 013 16.382V5.618a1 1 0 011.447-.894L9 7m0 13l6-3m-6 3V7m6 10l4.553 2.276A1 1 0 0021 18.382V7.618a1 1 0 00-.553-.894L15 4m0 13V4m0 0L9 7",
                                                            strokeLinecap="round",
                                                            strokeLinejoin="round",
                                                            strokeWidth="1",
                                                        )
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-gray-600 text-lg font-medium",
                                                    children=[
                                                        "Mapa interactivo de niveles de seguridad"
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-gray-500 mt-2",
                                                    children=[
                                                        "El mapa muestra las diferentes alcaldías y colonias de la Ciudad de México con un código de colores que indica el nivel de seguridad en cada zona, basado en datos estadísticos recientes."
                                                    ],
                                                ),
                                                html.P(
                                                    className="text-sm text-gray-400 mt-4",
                                                    children=[
                                                        "[Aquí se mostrará el mapa interactivo]"
                                                    ],
                                                ),
                                            ],
                                        )
                                    ],
                                )
                            ],
                        ),
                        html.Div(
                            className="p-6 border-t",
                            children=[
                                html.H4(
                                    className="font-semibold text-lg mb-2",
                                    children=["Interpretación del mapa"],
                                ),
                                html.Div(
                                    className="flex flex-wrap gap-4",
                                    children=[
                                        html.Div(
                                            className="flex items-center",
                                            children=[
                                                html.Div(
                                                    className="w-4 h-4 rounded bg-red-500 mr-2"
                                                ),
                                                html.Span(
                                                    className="text-sm",
                                                    children=["Alto riesgo"],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="flex items-center",
                                            children=[
                                                html.Div(
                                                    className="w-4 h-4 rounded bg-yellow-500 mr-2"
                                                ),
                                                html.Span(
                                                    className="text-sm",
                                                    children=["Riesgo medio"],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="flex items-center",
                                            children=[
                                                html.Div(
                                                    className="w-4 h-4 rounded bg-green-500 mr-2"
                                                ),
                                                html.Span(
                                                    className="text-sm",
                                                    children=["Bajo riesgo"],
                                                ),
                                            ],
                                        ),
                                        html.Div(
                                            className="flex items-center",
                                            children=[
                                                html.Div(
                                                    className="w-4 h-4 rounded bg-blue-500 mr-2"
                                                ),
                                                html.Span(
                                                    className="text-sm",
                                                    children=["Sin datos suficientes"],
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
                    className="bg-white rounded-xl shadow-lg overflow-hidden mb-12 p-8",
                    children=[
                        html.H3(
                            className="text-2xl font-bold mb-4 text-gray-800",
                            children=["Análisis de Seguridad"],
                        ),
                        html.P(
                            className="text-gray-600 mb-4",
                            children=[
                                "Nuestro análisis de seguridad se basa en datos de múltiples fuentes, incluyendo reportes oficiales de la Secretaría de Seguridad Ciudadana, denuncias ciudadanas y análisis estadísticos independientes. Esto nos permite ofrecer una visión más completa y equilibrada de la situación de seguridad en diferentes zonas."
                            ],
                        ),
                        html.P(
                            className="text-gray-600 mb-4",
                            children=[
                                "Los datos se actualizan mensualmente y se analizan tendencias a lo largo del tiempo para identificar patrones y cambios significativos en los niveles de seguridad. Esto permite a las autoridades, empresas y ciudadanos tomar decisiones informadas sobre seguridad y prevención."
                            ],
                        ),
                        html.Div(
                            className="mt-6 flex justify-center",
                            children=[
                                html.A(
                                    className="bg-gradient-to-r from-green-500 to-green-700 text-white py-2 px-6 rounded-md inline-block font-medium hover:shadow-md transition-all transform hover:-translate-y-0.5",
                                    href="#",
                                    children=["Descargar informe completo"],
                                )
                            ],
                        ),
                    ],
                ),
            ],
        ),
    ],
)
