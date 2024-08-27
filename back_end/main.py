from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory = "c:/py/front_end")) #* Importa a los elementos estáticos al proyecto

class ConversionRequest(BaseModel): # Se define la clase de lo que se importará desde el front hacia el back
    value: float
    from_unit: str
    to_unit: str

#* Creamos nuestra API la cual contendrá toda nuestra lógica de conversión
@app.post("/convert")
async def convert_units(request: ConversionRequest):
    value = request.value
    from_unit = request.from_unit
    to_unit = request.to_unit

    # Aquí puedes agregar la lógica de conversión real

    if from_unit == to_unit:
        return {"result" : value}

    if from_unit == "Meters" and to_unit == "Kilometers":
        result = value / 1000 

    elif from_unit == "Kilometers" and to_unit == "Meters":
        result = value * 1000

    elif from_unit == "Meters" and to_unit == "Miles":
        result = value / 0.00062137

    elif from_unit == "Kilometers" and to_unit == "Miles":
        result = value / 0.62137119

    elif from_unit == "Meters" and to_unit == "Yards":
        result = value * 1.0936133

    elif from_unit == "Kilometers" and to_unit == "Yards":
        result = value * 1093.6133

    elif from_unit == "Miles" and to_unit == "Meters":
        result = value * 0.00062137

    elif from_unit == "Miles" and to_unit == "Kilometers":
        result = value * 0.62137119

    elif from_unit == "Miles" and to_unit == "Yards":
        result = value * 1760

    elif from_unit == "Yards" and to_unit == "Meters":
        result = value / 1.0936133

    elif from_unit == "Yards" and to_unit == "Kilometers":
        result = value / 1093.6133

    elif from_unit == "Yards" and to_unit == "Miles":
        result = value / 0.00056818

    elif from_unit == "Grams" and to_unit == "Kilograms":
        result = value / 1000

    elif from_unit == "Grams" and to_unit == "Pounds":
        result = value * 0.00220462

    elif from_unit == "Grams" and to_unit == "Ounces":
        result = value * 0.03527396

    elif from_unit == "Kilograms" and to_unit == "Grams":
        result = value * 1000

    elif from_unit == "Kilograms" and to_unit == "Pounds":
        result = value * 2.20462262

    elif from_unit == "Kilograms" and to_unit == "Ounces":
        result = value * 35.273962

    elif from_unit == "Pounds" and to_unit == "Grams":
        result = value / 0.00220462

    elif from_unit == "Pounds" and to_unit == "Kilograms":
        result = value / 2.20462262

    elif from_unit == "Pounds" and to_unit == "Ounces":
        result = value * 16

    elif from_unit == "Ounces" and to_unit == "Grams":
        result = value / 0.03527396

    elif from_unit == "Ounces" and to_unit == "Kilograms":
        result = value / 35.273962

    elif from_unit == "Ounces" and to_unit == "Pounds":
        result = value / 16

    return {"result": result}

#! Para poder acceder a la aplicación solo se enciende el servidor (C:/carpeta python -m uvicorn archivo:app --reload)
#? Una vez encendido, se accede con el URL localhost:8000/static/index.html