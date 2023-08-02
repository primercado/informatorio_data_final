import requests
import os

CIUDADES = ["London", "New York", "Cordoba", "Taipei", "Buenos Aires", "Mexico DF", "Dublin", "Tilfis", "Bogota", "Tokio"]
COORDENADAS = ["lat=31&lon=64", "lat=40&lon=-73", "lat=-31&lon=-64", "lat=25&lon=64", "lat=-34&lon=-58", "lat=19&lon=-99", "lat=53&lon=6", "lat=41&lon=44", "lat=4&lon=74", "lat=35&lon=139"]
API_KEY = 'd4032988a317610982125cfd741d1ee5'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

# Función para obtener los datos del clima
# recibe la ciudad y las coordenadas como parámetros y 
# devuelva los datos del clima en formato JSON.

def get_data (ciudad, coordenadas):
    # Construimos la URL para llamar a la API
    url = f'{BASE_URL}?{coordenadas}&appid={API_KEY}'
    # Hacemos una solicitud GET
    response = requests.get(url)
    
    # Verificamos que la conexión sea exitosa con una condicional    
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error al obtener los datos del clima para {ciudad}. Código de estado: {response.status_code}')
        return None
    

# Función para guardar los datos en un CSV:
# Toma los datos del clima y los guarda en un archivo CSV

def guarda_data_csv (data, ciudad, dia):
    directorio = os.path.join("data_analytics", "openweather")
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    archivo = os.path.join(directorio, f"tiempodiario_{dia}.csv")
    
    with open(archivo, 'w') as file:
        file.write("Ciudad,Temperatura,Humedad,Descripción del clima\n")
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        file.write(f"{ciudad},{temp},{humidity},{description}\n")



# Obtenemos primeros datos

if __name__ == "__main__":
    for ciudad, coordenada in zip(CIUDADES, COORDENADAS):
        data = get_data(ciudad, coordenada)
        if data:
            dia = data['dt']
            guarda_data_csv(data, ciudad, dia)
