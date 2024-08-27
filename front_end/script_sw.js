// Función asincrónica para obtener la información de un personaje
async function fetchCharacter() {
    // Obtiene el valor del ID del personaje ingresado por el usuario
    const characterId = document.getElementById('character-id').value;
    
    // Realiza una solicitud a la API de FastAPI para obtener los datos del personaje
    const response = await fetch(`http://127.0.0.1:8000/get_char/${characterId}`);
    
    // Verifica si la respuesta es exitosa
    if (response.ok) {
        // Convierte la respuesta a formato JSON
        const character = await response.json();
        
        // Muestra la información del personaje en la página
        displayCharacterInfo(character);
        
        // Muestra la imagen del personaje en la página
        displayCharacterImage(characterId);
    } else {
        // Muestra una alerta si el personaje no se encuentra
        alert('Personaje no encontrado');
    }
}

// Función para mostrar la información del personaje en la página
function displayCharacterInfo(character) {
    // Obtiene el contenedor donde se mostrará la información del personaje
    const characterInfoDiv = document.getElementById('character-info');
    
    // Inserta la información del personaje en el contenedor
    characterInfoDiv.innerHTML = `
        <h2>${character.Nombre}</h2>
        <p><strong>Género:</strong> ${character.Genero}</p>
        <p><strong>Año de Nacimiento:</strong> ${character.Anio_nacimiento}</p>
    `;
}

// Función para mostrar la imagen del personaje en la página
function displayCharacterImage(characterId) {
    // Obtiene el contenedor donde se mostrará la imagen del personaje
    const characterImageDiv = document.getElementById('character-image');
    
    // Construye la URL de la imagen del personaje utilizando el ID del personaje
    const imageUrl = `https://starwars-visualguide.com/assets/img/characters/${characterId}.jpg`;
    
    // Inserta la imagen del personaje en el contenedor
    characterImageDiv.innerHTML = `<img src="${imageUrl}" alt="Imagen de personaje">`;
}
