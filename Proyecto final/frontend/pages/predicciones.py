html.Div(
    children=[
        html.Div(
            className="min-h-screen bg-gray-50 flex flex-col",
            children=[
                html.Section(
                    className="relative bg-cover bg-center py-24",
                    style={"background-image": "url(images/bg-predicciones.jpg)"},
                    children=[
                        html.Div(className="absolute inset-0 bg-purple-900 opacity-75"),
                        html.Div(
                            className="container mx-auto px-4 relative z-10",
                            children=[
                                html.Div(
                                    className="max-w-3xl mx-auto text-center",
                                    children=[
                                        html.H1(
                                            className="text-4xl md:text-5xl font-bold text-white mb-4",
                                            children=["Predicciones de Seguridad"],
                                        ),
                                        html.P(
                                            className="text-xl text-gray-200 mb-8",
                                            children=[
                                                "Anticipa riesgos con nuestro avanzado sistema de predicción basado en inteligencia artificial y aprendizaje automático."
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
                                    children=["Sistema de Predicción de Riesgos"],
                                ),
                                html.Div(
                                    className="prose lg:prose-lg mx-auto text-gray-600",
                                    children=[
                                        html.P(
                                            className="mb-4",
                                            children=[
                                                "Nuestro sistema de predicción utiliza algoritmos avanzados de aprendizaje automático para analizar patrones históricos y predecir la probabilidad de diferentes tipos de incidentes en ubicaciones específicas."
                                            ],
                                        ),
                                        html.P(
                                            className="mb-6",
                                            children=[
                                                "Utiliza cualquiera de los formularios a continuación para obtener predicciones basadas en fecha, hora y ubicación geográfica."
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
                                    className="bg-purple-600 px-6 py-4",
                                    children=[
                                        html.H3(
                                            className="text-xl font-bold text-white",
                                            children=["Predicción por Coordenadas"],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="p-8 bg-gray-50",
                                    children=[
                                        html.Form(
                                            className="space-y-6",
                                            id="predictionForm",
                                            children=[
                                                html.Div(
                                                    className="grid grid-cols-1 md:grid-cols-2 gap-6",
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Fecha"],
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Hora"],
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=[
                                                                        "Latitud"
                                                                    ],
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=[
                                                                        "Longitud"
                                                                    ],
                                                                )
                                                            ]
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="flex justify-center",
                                                    children=[
                                                        html.Button(
                                                            className="bg-gradient-to-r from-purple-600 to-indigo-600 text-white py-3 px-8 rounded-lg inline-block font-medium hover:shadow-lg transition-all transform hover:-translate-y-0.5",
                                                            type="submit",
                                                            children=[
                                                                "Calcular Predicción"
                                                            ],
                                                        )
                                                    ],
                                                ),
                                            ],
                                        )
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
                                            children=[
                                                "Predicción por Alcaldía de la CDMX"
                                            ],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="p-8 bg-gray-50",
                                    children=[
                                        html.Form(
                                            className="space-y-6",
                                            id="alcaldiaForm",
                                            children=[
                                                html.Div(
                                                    className="grid grid-cols-1 md:grid-cols-2 gap-6",
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Fecha"],
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Hora"],
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            className="md:col-span-2",
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=[
                                                                        "Alcaldía"
                                                                    ],
                                                                ),
                                                                html.Select(
                                                                    className="w-full px-4 py-2 border border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500",
                                                                    id="alcaldia",
                                                                    name="alcaldia",
                                                                    required="",
                                                                    children=[
                                                                        html.Option(
                                                                            value="",
                                                                            children=[
                                                                                "Selecciona una alcaldía"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="alvaro_obregon",
                                                                            children=[
                                                                                "Álvaro Obregón"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="azcapotzalco",
                                                                            children=[
                                                                                "Azcapotzalco"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="benito_juarez",
                                                                            children=[
                                                                                "Benito Juárez"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="coyoacan",
                                                                            children=[
                                                                                "Coyoacán"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="cuajimalpa",
                                                                            children=[
                                                                                "Cuajimalpa"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="cuauhtemoc",
                                                                            children=[
                                                                                "Cuauhtémoc"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="gustavo_a_madero",
                                                                            children=[
                                                                                "Gustavo A. Madero"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="iztacalco",
                                                                            children=[
                                                                                "Iztacalco"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="iztapalapa",
                                                                            children=[
                                                                                "Iztapalapa"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="magdalena_contreras",
                                                                            children=[
                                                                                "La Magdalena Contreras"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="miguel_hidalgo",
                                                                            children=[
                                                                                "Miguel Hidalgo"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="milpa_alta",
                                                                            children=[
                                                                                "Milpa Alta"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="tlahuac",
                                                                            children=[
                                                                                "Tláhuac"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="tlalpan",
                                                                            children=[
                                                                                "Tlalpan"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="venustiano_carranza",
                                                                            children=[
                                                                                "Venustiano Carranza"
                                                                            ],
                                                                        ),
                                                                        html.Option(
                                                                            value="xochimilco",
                                                                            children=[
                                                                                "Xochimilco"
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                                html.Div(
                                                    className="flex justify-center",
                                                    children=[
                                                        html.Button(
                                                            className="bg-gradient-to-r from-indigo-600 to-blue-600 text-white py-3 px-8 rounded-lg inline-block font-medium hover:shadow-lg transition-all transform hover:-translate-y-0.5",
                                                            type="submit",
                                                            children=[
                                                                "Calcular Predicción"
                                                            ],
                                                        )
                                                    ],
                                                ),
                                            ],
                                        )
                                    ],
                                ),
                            ],
                        ),
                        html.Div(
                            className="bg-white rounded-xl shadow-lg overflow-hidden",
                            children=[
                                html.Div(
                                    className="bg-purple-600 px-6 py-4",
                                    children=[
                                        html.H3(
                                            className="text-xl font-bold text-white",
                                            children=["Resultados de la Predicción"],
                                        )
                                    ],
                                ),
                                html.Div(
                                    className="p-8",
                                    children=[
                                        html.H4(
                                            className="text-lg font-semibold text-gray-800 mb-4",
                                            children=[
                                                "Predicciones para el 24/04/2025 a las 14:30 en [25.6714, -100.3094]"
                                            ],
                                        ),
                                        html.Div(
                                            className="overflow-x-auto",
                                            children=[
                                                html.Table(
                                                    className="min-w-full divide-y divide-gray-200 border border-gray-200 rounded-lg overflow-hidden",
                                                    children=[
                                                        html.Thead(
                                                            className="bg-gradient-to-r from-purple-500 to-indigo-600",
                                                            children=[
                                                                html.Tr(
                                                                    children=[
                                                                        html.Th(
                                                                            className="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider",
                                                                            scope="col",
                                                                            children=[
                                                                                "Tipo de Impacto"
                                                                            ],
                                                                        ),
                                                                        html.Th(
                                                                            className="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider",
                                                                            scope="col",
                                                                            children=[
                                                                                "Probabilidad (%)"
                                                                            ],
                                                                        ),
                                                                        html.Th(
                                                                            className="px-6 py-3 text-left text-xs font-medium text-white uppercase tracking-wider",
                                                                            scope="col",
                                                                            children=[
                                                                                "Indicador"
                                                                            ],
                                                                        ),
                                                                    ]
                                                                )
                                                            ],
                                                        ),
                                                        html.Tbody(
                                                            className="bg-white divide-y divide-gray-200",
                                                            children=[
                                                                html.Tr(
                                                                    className="hover:bg-gray-50",
                                                                    children=[
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="flex items-center",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="flex-shrink-0 h-10 w-10 bg-green-100 rounded-full flex items-center justify-center",
                                                                                            children=[
                                                                                                dash_svg.Svg(
                                                                                                    className="h-6 w-6 text-green-600",
                                                                                                    fill="none",
                                                                                                    stroke="currentColor",
                                                                                                    viewBox="0 0 24 24",
                                                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                                                    children=[
                                                                                                        dash_svg.Path(
                                                                                                            d="M5 13l4 4L19 7",
                                                                                                            strokeLinecap="round",
                                                                                                            strokeLinejoin="round",
                                                                                                            strokeWidth="2",
                                                                                                        )
                                                                                                    ],
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                        html.Div(
                                                                                            className="ml-4",
                                                                                            children=[
                                                                                                html.Div(
                                                                                                    className="text-sm font-medium text-gray-900",
                                                                                                    children=[
                                                                                                        "Bajo Impacto"
                                                                                                    ],
                                                                                                ),
                                                                                                html.Div(
                                                                                                    className="text-sm text-gray-500",
                                                                                                    children=[
                                                                                                        "Delitos menores"
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="text-sm text-gray-900",
                                                                                    children=[
                                                                                        "78%"
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="w-full bg-gray-200 rounded-full h-2.5",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="bg-green-500 h-2.5 rounded-full",
                                                                                            style={
                                                                                                "width": "78%"
                                                                                            },
                                                                                        )
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Tr(
                                                                    className="hover:bg-gray-50",
                                                                    children=[
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="flex items-center",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="flex-shrink-0 h-10 w-10 bg-yellow-100 rounded-full flex items-center justify-center",
                                                                                            children=[
                                                                                                dash_svg.Svg(
                                                                                                    className="h-6 w-6 text-yellow-600",
                                                                                                    fill="none",
                                                                                                    stroke="currentColor",
                                                                                                    viewBox="0 0 24 24",
                                                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                                                    children=[
                                                                                                        dash_svg.Path(
                                                                                                            d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z",
                                                                                                            strokeLinecap="round",
                                                                                                            strokeLinejoin="round",
                                                                                                            strokeWidth="2",
                                                                                                        )
                                                                                                    ],
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                        html.Div(
                                                                                            className="ml-4",
                                                                                            children=[
                                                                                                html.Div(
                                                                                                    className="text-sm font-medium text-gray-900",
                                                                                                    children=[
                                                                                                        "Impacto Medio"
                                                                                                    ],
                                                                                                ),
                                                                                                html.Div(
                                                                                                    className="text-sm text-gray-500",
                                                                                                    children=[
                                                                                                        "Delitos contra la propiedad"
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="text-sm text-gray-900",
                                                                                    children=[
                                                                                        "45%"
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="w-full bg-gray-200 rounded-full h-2.5",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="bg-yellow-500 h-2.5 rounded-full",
                                                                                            style={
                                                                                                "width": "45%"
                                                                                            },
                                                                                        )
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                    ],
                                                                ),
                                                                html.Tr(
                                                                    className="hover:bg-gray-50",
                                                                    children=[
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="flex items-center",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="flex-shrink-0 h-10 w-10 bg-red-100 rounded-full flex items-center justify-center",
                                                                                            children=[
                                                                                                dash_svg.Svg(
                                                                                                    className="h-6 w-6 text-red-600",
                                                                                                    fill="none",
                                                                                                    stroke="currentColor",
                                                                                                    viewBox="0 0 24 24",
                                                                                                    xmlns="http://www.w3.org/2000/svg",
                                                                                                    children=[
                                                                                                        dash_svg.Path(
                                                                                                            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
                                                                                                            strokeLinecap="round",
                                                                                                            strokeLinejoin="round",
                                                                                                            strokeWidth="2",
                                                                                                        )
                                                                                                    ],
                                                                                                )
                                                                                            ],
                                                                                        ),
                                                                                        html.Div(
                                                                                            className="ml-4",
                                                                                            children=[
                                                                                                html.Div(
                                                                                                    className="text-sm font-medium text-gray-900",
                                                                                                    children=[
                                                                                                        "Alto Impacto"
                                                                                                    ],
                                                                                                ),
                                                                                                html.Div(
                                                                                                    className="text-sm text-gray-500",
                                                                                                    children=[
                                                                                                        "Delitos violentos"
                                                                                                    ],
                                                                                                ),
                                                                                            ],
                                                                                        ),
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="text-sm text-gray-900",
                                                                                    children=[
                                                                                        "12%"
                                                                                    ],
                                                                                )
                                                                            ],
                                                                        ),
                                                                        html.Td(
                                                                            className="px-6 py-4 whitespace-nowrap",
                                                                            children=[
                                                                                html.Div(
                                                                                    className="w-full bg-gray-200 rounded-full h-2.5",
                                                                                    children=[
                                                                                        html.Div(
                                                                                            className="bg-red-500 h-2.5 rounded-full",
                                                                                            style={
                                                                                                "width": "12%"
                                                                                            },
                                                                                        )
                                                                                    ],
                                                                                )
                                                                            ],
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
                                            className="mt-8 p-6 bg-gray-50 rounded-lg border border-gray-200",
                                            children=[
                                                html.H4(
                                                    className="text-lg font-semibold text-gray-800 mb-2",
                                                    children=["Recomendaciones"],
                                                ),
                                                html.P(
                                                    className="text-sm text-gray-600 mb-3",
                                                    children=[
                                                        "Basado en nuestro análisis, esta zona presenta un riesgo moderado. Recomendamos:"
                                                    ],
                                                ),
                                                html.Ul(
                                                    className="list-disc pl-5 text-sm text-gray-600 space-y-1",
                                                    children=[
                                                        html.Li(
                                                            children=[
                                                                "Mantener precauciones normales de seguridad"
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Evitar zonas poco iluminadas después de las 21:00 horas"
                                                            ]
                                                        ),
                                                        html.Li(
                                                            children=[
                                                                "Consultar actualizaciones de predicción regularmente"
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
        html.Script(
            children=[
                """
                // Lógica para el formulario
                document.getElementById('predictionForm').addEventListener('submit', function(e) {
                    e.preventDefault();
                    // Aquí iría la lógica para procesar el formulario
                    // Por ahora solo mostramos un mensaje de confirmación
                    alert('¡Predicción calculada correctamente!');
                });
                """
            ]
        ),
    ]
)
