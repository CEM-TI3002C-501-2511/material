html.Header(
    className="bg-white shadow-md",
    children=[
        html.Div(
            className="container mx-auto px-4 py-3 flex justify-between items-center",
            children=[
                html.Div(
                    className="flex items-center",
                    children=[
                        html.A(
                            className="flex items-center",
                            href="index.html",
                            children=[
                                html.Img(
                                    alt="Thales Logo",
                                    className="h-12 mr-4",
                                    src="images/Thales.png",
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
                                        html.A(
                                            className="text-blue-600 hover:text-blue-800 font-medium",
                                            href="index.html",
                                            children=["Inicio"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="text-blue-600 hover:text-blue-800 font-medium",
                                            href="dashboards.html",
                                            children=["Dashboards"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="text-blue-600 hover:text-blue-800 font-medium",
                                            href="mapas.html",
                                            children=["Mapas"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="text-blue-600 hover:text-blue-800 font-medium",
                                            href="predicciones.html",
                                            children=["Predicciones"],
                                        )
                                    ]
                                ),
                                html.Li(
                                    children=[
                                        html.A(
                                            className="text-indigo-600 hover:text-indigo-800 font-medium border-b-2 border-indigo-600",
                                            href="acerca.html",
                                            children=["Acerca del sitio"],
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
