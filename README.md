# Bienvenido al TP Final del Informatorio Análisis de Datos
-----
## Integrantes:
* Mercado, Isaac Pablo Rubén


## Descripción del proyecto

El presente trabajo realiza una petición del tipo GET a la API de Open Weather, y mediante la misma solicita los siguientes datos, de las siguiente lista de ciudades: London, New York, Córdoba, Taipei, Buenos Aires, Mexico DF, Dublin, Tilfis, Bogota, Tokio:

* Temperatura en grados K
* Humedad
* Descripción del tiempo

Luego, los ubica en distintos CSV y los guarda en una determinada dirección de directorio.


-----
# Primeros Pasos
----
* Lo primero que hay que hacer es instalar un entorno virtual, lo hacemos mediante:

```
python3 -m virtualenv venv
```

* Luego hay que ejecutar el entorno virtual, en linux lo hacemos mediante:
```
source venv/bin/activate                           
```
* Luego debemos instalar las librerías
```
sudo pip3 install requiriments.txt
```
* Luego ejecutar el archivo main.py mediante
  
```
python3 main.py
```
