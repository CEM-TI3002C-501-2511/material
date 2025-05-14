import dash
import dash_svg
from datetime import date
from dash import html, dcc

dash.register_page(__name__,
    path="/predicciones",
    title="Predicciones de Seguridad",
    name="predicciones"
    )

layout = html.Div(
    children=[
        html.Div(
            className="min-h-screen bg-gray-50 flex flex-col",
            children=[
                html.Section(
                    className="relative bg-cover bg-center py-24",
                    style={"background-image": f"url({dash.get_asset_url('images/bg-predicciones.jpg')})"},
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
                                                                ),
                                                                dcc.DatePickerSingle(
                                                                    className="w-full py-2",
                                                                    id="fecha",
                                                                    date=date.today(),
                                                                    display_format="YYYY-MM-DD",
                                                                    with_portal=True
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Hora"],
                                                                ),
                                                                dcc.Slider(
                                                                    id="hora",
                                                                    min=0,
                                                                    max=23,
                                                                    step=1,
                                                                    value=12,
                                                                    marks={
                                                                        i: str(i)
                                                                        for i in range(24)
                                                                    },
                                                                    className="w-full mt-4 px-4 py-2 focus:ring-purple-500 focus:border-purple-500",
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
                                                                ),
                                                                dcc.Input(
                                                                    type="number",
                                                                    id="latitud",
                                                                    className="w-full px-4 py-2 bg-white border border-gray-300 rounded-md focus:ring-purple-500 focus:border-purple-500",
                                                                    placeholder="Ej: 19.4326",
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
                                                                ),
                                                                dcc.Input(
                                                                    type="number",
                                                                    id="longitud",
                                                                    className="w-full px-4 py-2 bg-white border border-gray-300 rounded-md focus:ring-purple-500 focus:border-purple-500",
                                                                    placeholder="Ej: -99.1332",
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
                                                    className="grid grid-cols-1 md:grid-cols-3 gap-6",
                                                    children=[
                                                        html.Div(
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Fecha"],
                                                                ),
                                                                dcc.DatePickerSingle(
                                                                    className="w-full py-2",
                                                                    id="fecha_alcaldia",
                                                                    date=date.today(),
                                                                    display_format="YYYY-MM-DD",
                                                                    with_portal=True
                                                                )
                                                            ]
                                                        ),
                                                        html.Div(
                                                            className="col-span-2",
                                                            children=[
                                                                html.Label(
                                                                    className="block text-sm font-medium text-gray-700 mb-1",
                                                                    children=["Alcaldía"],
                                                                ),
                                                                dcc.Dropdown(
                                                                    className="w-full rounded-md focus:ring-indigo-500 focus:border-indigo-500",
                                                                    id="alcaldia_dropdown",
                                                                    options=[
                                                                        {"label": "Alcaldía 1", "value": "alcaldia_1"},
                                                                        {"label": "Alcaldía 2", "value": "alcaldia_2"},
                                                                        {"label": "Alcaldía 3", "value": "alcaldia_3"},
                                                                    ],
                                                                    value="alcaldia_1"
                                                                )
                                                            ]
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
