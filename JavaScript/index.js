import { agregarItemAlCarrusel } from "./ItemCarrusel.js";

let index = 0;
var totalItems = 0;


async function cargarConfig() {
    const res = await fetch('config.json');
    const config = await res.json();
    return config;

}

async function fetchData() {
    const config =  await cargarConfig();


    fetch('http://'+config.IP+':'+config.PORT+'/carusel')  // Asegúrate de que la URL esté correcta
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al obtener los productos: ' + response.statusText);
            }
            return response.json();  // Parsear la respuesta como JSON
        })
        .then(data => {
            const productos = data.data;  // Aquí se asume que el resultado de la API tiene una clave 'data' con los productos
            totalItems = productos.length;
            // Vaciar el carrusel antes de agregar nuevos items
            limpiarCarrusel();  // Asegúrate de que esta función exista para limpiar el carrusel

            // Llenar el carrusel con los productos obtenidos
            for (let i = 0; i < totalItems; i++) {
                agregarItemAlCarrusel(
                    productos[i].nombre,
                    productos[i].descripcion,
                    productos[i].precio,
                    productos[i].image ? `data:image/jpeg;base64,${productos[i].image}` : 'Images/default.jpg'
                );
            }
        })
        .catch(error => {
            console.error('Hubo un problema con la operación fetch:', error);
        });
}
function limpiarCarrusel() {
    const carruselContainer = document.querySelector('.carousel-content');
    carruselContainer.innerHTML = '';  // Elimina todo el contenido actual del carrusel
}

function updateCarousel() {
    const carouselContent = document.querySelector('.carousel-content');
    const itemWidth = 100; // Each item takes up 100% of the carousel width
    const offset = -index * itemWidth;
    carouselContent.style.transform = `translateX(${offset}%)`; // Move using percentage

    // Disable or enable buttons based on index
    document.getElementById('prev').disabled = index === 0;
    document.getElementById('next').disabled = index === totalItems - 1;
}

// Event listeners for next and previous buttons
document.getElementById('next').addEventListener('click', function() {
    if (index < totalItems - 1) {
        index++;
        updateCarousel();
    }
});

document.getElementById('prev').addEventListener('click', function() {
    if (index > 0) {
        index--;
        updateCarousel();
    }
});

// Initialize carousel
await fetchData();
updateCarousel();
