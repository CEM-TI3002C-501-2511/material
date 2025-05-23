import os
import joblib
import pandas as pd
import plotly.io as pio
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel, field_validator
from datetime import date
from prophet.plot import plot_plotly, plot_components_plotly
from google import genai

def load_data():
    df = pd.read_csv("carpetas.csv")
    df["datetime"] = pd.to_datetime(df["datetime"], format="mixed")
    df = df.dropna()
    return df

load_dotenv()
# GEMINI_API_KEY = os.getenv("GEMINI")
df = load_data()
alcaldías = df["alcaldía"].drop_duplicates().sort_values().tolist()
gravedades = df["gravedad"].unique().tolist()
last_date = df["datetime"].max()

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
    return alcaldías

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
    days_diff = (fecha - last_date).days
    if days_diff < 0:
        return {"error": "La fecha debe ser mayor a la última fecha en los datos: {last_date}"}
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
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)