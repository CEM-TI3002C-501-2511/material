import requests
import pandas as pd

url = "https://datos.cdmx.gob.mx/es/api/3/action/datastore_search_sql"

query = '''
SELECT _id,
  fecha_inicio,
  fecha_hecho,
  hora_hecho,
  delito,
  categoria_delito,
  colonia_hecho,
  alcaldia_hecho,
  latitud,
  longitud
FROM "48fcb848-220c-4af0-839b-4fd8ac812c0f"
ORDER BY _id
LIMIT 32000
OFFSET {}
'''
offset = 0
params = {
    "sql": query.format(offset)
}

response = requests.get(url, params)
json_response = response.json()
data = json_response["result"]["records"]

df = pd.DataFrame(data)
params = { "sql": query.format(len(df)) }
while data:=requests.get(url, params).json()["result"]["records"]:
    df = pd.concat([df, pd.DataFrame(data)])
    params = { "sql": query.format(len(df)) }
    
df = df.rename(columns={
    '_id': "id",
    'fecha_inicio': "inicio",
    'fecha_hecho': "fecha",
    'hora_hecho': "hora",
    'categoria_delito': "categoría",
    'colonia_hecho': "colonia",
    'alcaldia_hecho': "alcaldía"
})

df = df.dropna()

df["datetime"] = pd.to_datetime(df["fecha"].str.split("T").str[0] + " " + df["hora"].apply(lambda x: x if len(x) == 8 else x[:8]), format="mixed")

df = df.drop(columns=["fecha", "hora"])

df["inicio"] = pd.to_datetime(df["inicio"].str.split("T").str[0])

columnas = [x for x in df.columns if df[x].dtype == "object"]
for col in columnas:
    df[col] = df[col].str.lower()

def clasificar_gravedad(categoria):
    if categoria == 'delito de bajo impacto' or categoria == 'hecho no delictivo':
        return 'bajo impacto'
    elif categoria in [
        'robo a pasajero a bordo de taxi con violencia',
        'robo a transeunte en vía pública con y sin violencia',
        'robo de vehículo con y sin violencia',
        'robo a negocio con violencia',
        'robo a repartidor con y sin violencia',
        'robo a casa habitación con violencia',
        'robo a cuentahabiente saliendo del cajero con violencia',
        'robo a pasajero a bordo de microbus con y sin violencia',
        'robo a pasajero a bordo del metro con y sin violencia',
        'robo a transportista con y sin violencia'
    ]:
        return 'impacto medio'
    elif categoria in [
        'homicidio doloso',
        'lesiones dolosas por disparo de arma de fuego',
        'plagio o secuestro',
        'feminicidio',
        'violación',
        'secuestro'
    ]:
        return 'alto impacto'
    else:
        return 'desconocido'
    
df['gravedad'] = df['categoría'].apply(clasificar_gravedad)

df.to_csv("carpetas.csv", index=False)