import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

class AlumnoModel(BaseModel):
    id: int
    alumno: str
    parcial_1: float
    parcial_2: float
    parcial_3: float
    final: float

def load_data():
    df = pd.read_csv("calificaciones.csv")
    return df

df = load_data()
app = FastAPI()

@app.get("/")
def home():
    return "Hola mundo"

# Query parameter order
@app.get("/alumnos")
def get_alumnos(order: str = "asc"):
    if order == "desc":
        return df.sort_values(by="id", ascending=False).to_dict(orient="records")
    else:
        return df.sort_values(by="id", ascending=True).to_dict(orient="records")

# Path parameter {alumno_id}
@app.get("/alumno/{alumno_id}")
def get_alumno(alumno_id: int):
    alumno = df[df["id"] == alumno_id]
    return alumno.to_dict(orient="records")

@app.post("/alumno")
def post_alumno(alumno: AlumnoModel):
    nuevo_alumno = pd.DataFrame({
        "id": [alumno.id],
        "alumno": [alumno.alumno],
        "parcial_1": [alumno.parcial_1],
        "parcial_2": [alumno.parcial_2],
        "parcial_3": [alumno.parcial_3],
        "final": [alumno.final]
    })
    return nuevo_alumno.to_dict(orient="records")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", reload=True)