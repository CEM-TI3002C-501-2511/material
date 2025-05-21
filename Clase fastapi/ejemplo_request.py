import requests

# response = requests.get("http://127.0.0.1:8000/alumnos")
# json_response = response.json()
# print(response)
# print(json_response)

# json = {
#     "id": 10,
#     "alumno": "Juan Perez",
#     "parcial_1": 8.5,
#     "parcial_2": 9.0,
#     "parcial_3": 7.5,
#     "final": 8.0
# }
# response = requests.post("http://127.0.0.1:8000/alumno", json=json)
# print(response)
# print(response.json())

# Email:	moets2xfgi@jxpomup.com
# Token:	qBnTgMvoQOdpKnXkPJPAFvQWkEejEGiT

base_url = "https://www.ncei.noaa.gov/cdo-web/api/v2"
token = "qBnTgMvoQOdpKnXkPJPAFvQWkEejEGiT"

# {'metadata': {'resultset': {'offset': 1, 'count': 12, 'limit': 25}}, 'results': [{'name': 'City', 'id': 'CITY'}, {'name': 'Climate Division', 'id': 'CLIM_DIV'}, {'name': 'Climate Region', 'id': 'CLIM_REG'}, {'name': 'Country', 'id': 'CNTRY'}, {'name': 'County', 'id': 'CNTY'}, {'name': 'Hydrologic Accounting Unit', 'id': 'HYD_ACC'}, {'name': 'Hydrologic Cataloging Unit', 'id': 'HYD_CAT'}, {'name': 'Hydrologic Region', 'id': 'HYD_REG'}, {'name': 'Hydrologic Subregion', 'id': 'HYD_SUB'}, {'name': 'State', 'id': 'ST'}, {'name': 'US Territory', 'id': 'US_TERR'}, {'name': 'Zip Code', 'id': 'ZIP'}]}

# FIPS:MX

# {'mindate': '1902-06-01', 'maxdate': '2025-05-14', 'name': 'Mexico', 'datacoverage': 1, 'id': 'FIPS:MX'}

# GHCND:MXM00076680

query = {
    "locationcategoryid": "CNTRY",
    "limit": 1000
}
response = requests.get(f"{base_url}/datasets", headers={"token": token})
print(response)
print(response.json())