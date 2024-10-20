// Función para añadir redirección a un elemento
function addRedirect(elementId, url) {
    document.getElementById(elementId).addEventListener('click', function(event) {
        event.preventDefault(); // Prevenir el comportamiento por defecto del enlace
        window.location.href = url;
    });
}

// Añadir redirecciones a los elementos de navegación
addRedirect('home', 'index.html');
addRedirect('about', 'about.html');
addRedirect('services', 'services.html');
addRedirect('contact', 'https://example.com/contact');

function handleClick(platform) {
    switch(platform) {
        case 'fb':
            window.location.href = 'https://www.facebook.com/GraAyeTheSaxGod';
            break;
        case 'tw':
            window.location.href = 'https://x.com/GraAye_';
            break;
        case 'wapp':
            window.location.href = 'https://wa.me/7851092040';
            break;
        default:
            console.log('Plataforma no reconocida');
    }
}