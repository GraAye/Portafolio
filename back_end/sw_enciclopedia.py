# Back end para página que muestre información de los personajes de SW usando SWAPI

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import requests

#* Guardamos la URL para reutilizarla sin necesidad de escribirla
base_url = "https://swapi.dev/api/"

# Iniciamos nuestra app de FastAPI
app = FastAPI()
app.mount("/static", StaticFiles(directory = "c:/py/front_end")) #! <--- Usamos la función mount para cargar la carpeta front end a nuestro proyecto

# Configuración de CORS, lo cual permite que acceda solo a estos URL por seguridad
origins = [
    "http://localhost",
    "http://localhost:8000",
    # Agrega aquí cualquier otro origen que necesites permitir
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#! Definimos la función para obtener la información del API de Star Wars
def get_resourse(resource : str, id : int):

    #* Guardamos la URL en un formato variable
    url = f"{base_url}{resource}/{id}/"
    response = requests.get(url)
    if response.status_code == 200:

        #* Regresa lo obtenido en la API mediante un JSON
        return response.json()
    else:
        raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST, detail = "Se ha realizado mal esta solicitud...")

#! Definimos la API con una función asíncrona
@app.get("/get_char/{id}")
async def get_char(id : int):

    #* Guardamos el JSON de la API
    character = get_resourse("people", id)

    #* Verifica si hay respuesta
    if character:

        #* Obtiene el género obtenido
        char_gender = character.get("gender")

        #* Si el género es male o female lo traduce a Español
        if char_gender == "male":
            char_gender = "Masculino"
        elif char_gender == "female":
            char_gender == "Femenino"

        #* Definimos un JSON con las características que necesita
        filtered_char = {
            "Nombre" : character.get("name"),
            "Genero" : char_gender,
            "Anio_nacimiento" : character.get("birth_year")
        }

        #* Retorna el JSON filtrado
        return filtered_char
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Este personaje no se encontró")

        #? Acceder localhost:8000/static/index_sw.html