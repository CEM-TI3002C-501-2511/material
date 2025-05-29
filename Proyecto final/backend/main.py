import os
import joblib
import pandas as pd
import plotly.io as pio
import snowflake.connector
from decimal import Decimal
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from datetime import date
from prophet.plot import plot_plotly, plot_components_plotly
from google import genai

# def load_data():
#     df = pd.read_csv("carpetas.csv")
#     df["datetime"] = pd.to_datetime(df["datetime"], format="mixed")
#     df = df.dropna()
#     return df

def get_conn():
    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        database=DATABASE,
        schema=SCHEMA
        )
    return conn

def obtener_tablas_snowflake():
    """
    Obtiene la lista de tablas de una base de datos y esquema específicos en Snowflake.

    Returns:
        list: Una lista de nombres de las tablas encontradas en el esquema.
              Retorna una lista vacía si ocurre algún error o no se encuentran tablas.
    """
    tables = []
    try:
        conn = get_conn()
        cursor = conn.cursor()
        sql = f"SHOW TABLES IN {DATABASE}.{SCHEMA}"
        cursor.execute(sql)
        for row in cursor:
            tables.append(row[1])  # El nombre de la tabla está en la segunda columna
    except snowflake.connector.errors.Error as e:
        print(f"Error al conectar o ejecutar la consulta en Snowflake: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    return tables

def obtener_esquema_tabla_snowflake(table_name: str):
    """
    Obtiene el esquema (nombre y tipo de datos de las columnas) de una tabla específica en Snowflake.

    Args:
        table_name (str): El nombre de la tabla cuyo esquema se desea obtener.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario contiene las claves 'name' (nombre de la columna)
              y 'type' (tipo de datos de la columna).
              Retorna una lista vacía si ocurre algún error o la tabla no se encuentra.
    """
    schema_info = []
    try:
        conn = get_conn()
        cursor = conn.cursor()
        sql = f"DESCRIBE TABLE {DATABASE}.{SCHEMA}.{table_name}"
        cursor.execute(sql)
        for row in cursor:
            schema_info.append({"name": row[0], "type": row[1]})
    except snowflake.connector.errors.Error as e:
        print(f"Error al conectar o ejecutar la consulta en Snowflake: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    return schema_info

def ejecutar_consulta_snowflake(sql_query: str):
    """
    Ejecuta una consulta SQL en Snowflake y devuelve los resultados como una lista de diccionarios.

    Args:
        sql_query (str): La consulta SQL a ejecutar.

    Returns:
        list: Una lista de diccionarios, donde cada diccionario representa una fila de los resultados.
              Las claves del diccionario son los nombres de las columnas.
              Retorna una lista vacía si no hay resultados o si ocurre un error.
    """

    results = []
    conn = None
    try:
        conn = get_conn()
        cursor = conn.cursor()
        cursor.execute(sql_query)
        column_names = [col[0] for col in cursor.description]
        for row in cursor:
            row_dict = {}
            for i, col_name in enumerate(column_names):
                if isinstance(row[i], Decimal):
                    row_dict[col_name] = float(row[i])
                else:
                    row_dict[col_name] = row[i]
            results.append(row_dict)
    except snowflake.connector.errors.Error as e:
        print(f"Error al ejecutar la consulta en Snowflake: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()
    return results

load_dotenv()
USER = os.getenv("SNOWFLAKE_USER")
PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
DATABASE = os.getenv("SNOWFLAKE_DATABASE")
SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")
# df = load_data()
# alcaldías = df["alcaldía"].drop_duplicates().sort_values().tolist()
# gravedades = df["gravedad"].unique().tolist()
# last_date = df["datetime"].max()

class CoordinatesModel(BaseModel):
    hora: int
    latitud: float
    longitud: float
    
    @field_validator("hora", mode="after")
    @classmethod
    def validate_hora(cls, value: int) -> int:
        if value < 0 or value > 23:
            raise ValueError("La hora debe estar entre 0 y 23")
        return value

class AlcaldiaModel(BaseModel):
    fecha: date
    alcaldia: str
    @field_validator("alcaldia", mode="after")
    @classmethod
    def validate_alcaldia(cls, value : str) -> str:
        alcaldías = get_alcaldías()
        if value not in alcaldías:
            raise ValueError(f"Alcaldia {value} no es válida. Opciones: {", ".join(alcaldías)}")
        return value
    
class GeminiQueryModel(BaseModel):
    query: str
    @field_validator("query", mode="after")
    @classmethod
    def validate_query(cls, value: str) -> str:
        if len(value) < 10:
            raise ValueError("La consulta debe tener al menos 10 caracteres")
        return value

def load_coordinates_model():
    return joblib.load(f"modelos/modelo_coordenadas.joblib")

def load_alcaldia_model(alcaldia, gravedad):
    return joblib.load(f"modelos/{alcaldia}_{gravedad}.joblib")

app = FastAPI()

@app.get("/alcaldias")
def get_alcaldías():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT alcaldia FROM CARPETAS ORDER BY alcaldia")
    alcaldías = [row[0] for row in cursor.fetchall() if row[0] is not None]
    cursor.close()
    conn.close()
    return alcaldías

@app.get("/gravedades")
def get_gravedades():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT gravedad FROM CARPETAS ORDER BY gravedad")
    gravedades = [row[0] for row in cursor.fetchall() if row[0] is not None]
    cursor.close()
    conn.close()
    return gravedades

@app.get("/ultima_fecha")
def get_ultima_fecha():
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(datetime) FROM CARPETAS")
    last_date = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    if last_date:
        return {"ultima_fecha": last_date.strftime("%Y-%m-%d")}
    else:
        return {"ultima_fecha": None}

@app.post("/prediccion_coordenadas")
def predict_coordinates(data: CoordinatesModel):
    model = load_coordinates_model()
    pred_df = pd.DataFrame({
        "hora": [data.hora],
        "latitud": [data.latitud],
        "longitud": [data.longitud]
    })
    preds = model.predict_proba(pred_df)
    bajo_impacto = preds[0][0][1]
    impacto_medio = preds[1][0][1]
    alto_impacto = preds[2][0][1]
    recomendaciones = []
    if bajo_impacto >= 0.50:
        recomendaciones.extend([
            "Mantener precauciones normales de seguridad",
            "Evitar zonas poco iluminadas después de las 21:00 horas",
            "Consultar actualizaciones de predicción regularmente"
        ])
    if impacto_medio >= 0.40:
        recomendaciones.extend([
            "Evitar transitar solo por zonas con antecedentes delictivos",
            "Utilizar rutas conocidas y transitadas",
            "Informar a un contacto de confianza sobre tu ubicación",
            "Consultar actualizaciones de predicción diariamente"
        ])
    if alto_impacto >= 0.30:
        recomendaciones.extend([
            "Evitar salir innecesariamente durante horarios de alto riesgo",
            "Reportar cualquier actividad sospechosa a las autoridades",
            "Mantener comunicación constante con familiares o amigos",
            "Revisar predicciones y alertas de seguridad antes de salir",
            "Considerar transporte seguro o acompañado por terceros"
        ])
    return {
        "bajo impacto": preds[0][0][1],
        "impacto medio": preds[1][0][1],
        "alto impacto": preds[2][0][1],
        "recomendaciones": recomendaciones
    }
    
@app.post("/prediccion_alcaldia")
def predict_alcaldia(data: AlcaldiaModel):
    resultados = {}
    fecha = pd.to_datetime(data.fecha)
    última_fecha = pd.to_datetime(get_ultima_fecha()["ultima_fecha"])
    if última_fecha is None:
        return {"error": "No hay datos disponibles para realizar la predicción. Por favor, asegúrate de que la base de datos contiene registros."}
    days_diff = (fecha - última_fecha).days
    if days_diff < 0:
        return {"error": "La fecha debe ser mayor a la última fecha en los datos: {last_date}"}
    gravedades = get_gravedades()
    for gravedad in gravedades:
        model = load_alcaldia_model(data.alcaldia, gravedad)
        future = model.make_future_dataframe(periods=days_diff, freq="D")
        forecast = model.predict(future)
        predictions = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
        fig1 = plot_plotly(model, forecast)
        fig2 = plot_components_plotly(model, forecast)
        resultados[gravedad] = {
            "predicciones": predictions.to_dict(orient="records"),
            "figura": pio.to_json(fig1),
            "componentes": pio.to_json(fig2)
        }
    return resultados

@app.post("/chatbot")
def chatbot(data: GeminiQueryModel):
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model = "gemini-2.0-flash",
            contents = data.query,
            config = genai.types.GenerateContentConfig(
                tools=[genai.types.Tool(google_search=genai.types.GoogleSearch())],
                )
            )
        return {"respuesta": response.text}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Error al procesar la consulta"}
    
@app.post("/chatbot_snowflake")
def chatbot_snowflake(data: GeminiQueryModel):
    instruction = """Eres un experto en interactuar con una base de datos Snowflake. 
Tu objetivo es ayudar al usuario a obtener información de la base de datos respondiendo a sus preguntas en lenguaje natural. 
Tienes a tu disposición las siguientes herramientas (funciones) para interactuar con la base de datos:

- obtener_tablas_snowflake(): Obtiene la lista de tablas disponibles en la base de datos.
- obtener_esquema_tabla_snowflake(table_name: string): Obtiene el esquema (nombres y tipos de columnas) de una tabla específica.
- ejecutar_consulta_snowflake(sql_query: string): Ejecuta una consulta SQL en Snowflake y devuelve los resultados.

La base de datos contiene las siguientes tablas:
- La tabla 'CARPETAS' tiene información sobre las carpetas de investigación de delitos, incluyendo la alcaldía, fecha y hora del delito, latitud y longitud del lugar, y la gravedad del delito.

Utiliza estas herramientas de forma inteligente para responder a las preguntas del usuario. Si necesitas información sobre las tablas o su estructura para poder responder a la pregunta, no dudes en utilizar las herramientas disponibles antes de intentar generar una respuesta final. 
Sé conciso y responde en lenguaje natural cuando sea posible. Si la respuesta requiere datos de la base de datos, utiliza la herramienta 'ejecutar_consulta_snowflake' para obtenerlos."""
    try:
        client = genai.Client()
        response = client.models.generate_content(
            model = "gemini-2.0-flash",
            contents = data.query,
            config = genai.types.GenerateContentConfig(
                system_instruction=instruction,
                tools=[obtener_tablas_snowflake, obtener_esquema_tabla_snowflake, ejecutar_consulta_snowflake]
                )
            )
        return {"respuesta": response.text}
    except Exception as e:
        print(f"Error: {e}")
        return {"error": "Error al procesar la consulta"}
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)