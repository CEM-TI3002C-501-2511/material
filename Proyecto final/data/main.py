import os
import requests
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import snowflake.connector.pandas_tools

def get_conn():
    load_dotenv()
    USER = os.getenv("SNOWFLAKE_USER")
    PASSWORD = os.getenv("SNOWFLAKE_PASSWORD")
    ACCOUNT = os.getenv("SNOWFLAKE_ACCOUNT")
    DATABASE = os.getenv("SNOWFLAKE_DATABASE")
    SCHEMA = os.getenv("SNOWFLAKE_SCHEMA")

    conn = snowflake.connector.connect(
        user=USER,
        password=PASSWORD,
        account=ACCOUNT,
        database=DATABASE,
        schema=SCHEMA
        )
    return conn

def get_latest_id():
    conn = get_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT MAX(ID) FROM CARPETAS")
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        cursor.close()
        conn.close()
        
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

def update_snowflake():
    latest_id = get_latest_id()
    if latest_id is not None:
        print(f"Latest ID in CARPETAS: {latest_id}")
    else:
        print("No records found in CARPETAS.")
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
    WHERE _id > {}
    ORDER BY _id
    OFFSET {}
    LIMIT 32000
    '''
    offset = 0
    params = {
        "sql": query.format(latest_id, offset)
    }
    response = requests.get(url, params)
    json_response = response.json()
    data = json_response["result"]["records"]
    
    while data:
        df = pd.DataFrame(data)
        df = df.rename(columns={
            "_id": "id",
            "fecha_inicio": "inicio",
            "fecha_hecho": "fecha",
            "hora_hecho": "hora",
            "categoria_delito": "categoria",
            "colonia_hecho": "colonia",
            "alcaldia_hecho": "alcaldia"
        })
        
        df = df.dropna()
        
        df["datetime"] = pd.to_datetime(df["fecha"].str.split("T").str[0] + " " + df["hora"].apply(lambda x: x if len(x) == 8 else x[:8]), format="mixed").dt.strftime("%Y-%m-%d %H:%M:%S")
        
        df = df.drop(columns=["fecha", "hora"])

        df["inicio"] = pd.to_datetime(df["inicio"].str.split("T").str[0]).dt.strftime("%Y-%m-%d")

        columnas = [x for x in df.columns if df[x].dtype == "object"]
        for col in columnas:
            df[col] = df[col].str.lower()
            
        df['gravedad'] = df['categoria'].apply(clasificar_gravedad)
        df.columns = map(lambda x: str(x).upper(), df.columns)
        # df = df.set_index("ID")
        conn = get_conn()
        # cur = conn.cursor()
        try:
            snowflake.connector.pandas_tools.write_pandas(conn, df, "CARPETAS")
            print(f"Inserted {len(df)} records into CARPETAS.")
        except Exception as e:
            print(f"Error inserting data into Snowflake: {e}")
        finally:
            # cur.close()
            conn.close()
        offset += len(data)
        params = {
            "sql": query.format(latest_id, offset)
        }
        response = requests.get(url, params)
        json_response = response.json()
        data = json_response["result"]["records"]
    
if __name__ == "__main__":
    update_snowflake()