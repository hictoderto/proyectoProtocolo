export function agregarItemAlCarrusel(nombre, informacion, precio, imagenURL) {
    console.log(precio);
    const carrusel = document.querySelector('.carousel-content');

    if (!carrusel) {
        console.error("El carrusel no existe en el documento.");
        return; // Exit early if the carousel container is not found
    }

    const item = document.createElement('div');
    item.className = 'item';

    const img = document.createElement('img');
    img.src = imagenURL || 'Images/person.jpg'; // Fallback to a default image if none provided
    img.alt = 'Producto'; // More descriptive alt text for accessibility

    const info = document.createElement('div');
    info.className = 'info';

    const h1 = document.createElement('h1');
    h1.textContent = nombre;

    const h2 = document.createElement('h2');
    h2.textContent = informacion;

    const h3 = document.createElement('h3');
    h3.textContent = precio;

    // Assembling the structure
    info.appendChild(h1);
    info.appendChild(h2);
    info.appendChild(h3);

    item.appendChild(img);
    item.appendChild(info);

    // Add the item to the carousel
    carrusel.appendChild(item);
}
