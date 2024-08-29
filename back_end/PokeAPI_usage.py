"""
Difícil
13/05/2024
#20
PETICIONES HTTP
/*
 * EJERCICIO:
 * Utilizando un mecanismo de peticiones HTTP de tu lenguaje, realiza
 * una petición a la web que tú quieras, verifica que dicha petición
 * fue exitosa y muestra por consola el contenido de la web.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utilizando la PokéAPI (https://pokeapi.co), crea un programa por
 * terminal al que le puedas solicitar información de un Pokémon concreto
 * utilizando su nombre o número.
 * - Muestra el nombre, id, peso, altura y tipo(s) del Pokémon
 * - Muestra el nombre de su cadena de evoluciones
 * - Muestra los juegos en los que aparece
 * - Controla posibles errores
 */
"""

import requests

url_base = "https://pokeapi.co/api/v2/"

def solicitar_poke_por_nombre(pokemon_nombre):
    pokemon_nombre = pokemon_nombre.lower()
    url = f"{url_base}pokemon/{pokemon_nombre}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        return filtar_datos(response_json)
    else:
        print("No se pudo encontrar tu Pokémon")
        return None
    
def solicitar_poke_por_id(pokemon_id):
    url = f"{url_base}pokemon/{pokemon_id}"
    response = requests.get(url)
    if response.status_code == 200:
        response_json = response.json()
        return filtar_datos(response_json)
    else:
        print("No se pudo encontrar tu Pokémon")
        return None

def obtener_cadena_evolutiva(evolution_url):
    response = requests.get(evolution_url)
    if response.status_code == 200:
        evolution_data = response.json()
        return filtrar_cadena_evolutiva(evolution_data["chain"])
    else:
        return []

def filtrar_cadena_evolutiva(chain):
    evoluciones = []
    actual = chain
    while actual:
        evoluciones.append(actual["species"]["name"])
        if actual["evolves_to"]:
            actual = actual["evolves_to"][0]
        else:
            actual = None
    return evoluciones

def filtar_datos(json_poke):
    species_url = json_poke["species"]["url"]
    species_response = requests.get(species_url)
    if species_response.status_code == 200:
        species_data = species_response.json()
        evolution_url = species_data["evolution_chain"]["url"]
        evoluciones = obtener_cadena_evolutiva(evolution_url)
    else:
        evoluciones = []

    poke_filtrado = {
        "Nombre" : json_poke["forms"][0]["name"],
        "ID" : json_poke["id"],
        "Peso" : json_poke["weight"],
        "Altura" : json_poke["height"],
        "Tipos" : [tipo["type"]["name"] for tipo in json_poke["types"]],
        "Juegos" : [juego["version"]["name"] for juego in json_poke["game_indices"]],
        "Evoluciones": evoluciones
    }
    return poke_filtrado

def solicitud():
    print("***** BIENVENIDO A LA POKEAPI *****")
    opcion = input("Deseas buscar a tu Pokémon por ID o por Nombre?\na)ID           b)Nombre\n")

    try:
        if opcion == "a":
            poke_id = input("Escribe el ID de tu pokemon: ")
            pokemon_filtrado = solicitar_poke_por_id(poke_id)
            if pokemon_filtrado:
                print(f"Tu Pokémon es: {pokemon_filtrado}")
            else:
                print("No se encontró este Pokémon...")
                solicitud()

        elif opcion == "b":
            poke_nombre = input("Escribe el nombre de tu pokemon: ")
            pokemon_filtrado = solicitar_poke_por_nombre(poke_nombre)
            if pokemon_filtrado:
                print(f"Tu Pokémon es: {pokemon_filtrado}")
            else:
                print("No se encontró este Pokémon...")
                solicitud()
        else:
            raise Exception
    except Exception as e:
        print(f"Tuviste un error: {e}, inténtalo de nuevo...")
        solicitud()

solicitud()
