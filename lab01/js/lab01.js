// Se espera a que se cargue el dom para poder ejecutar el siguiente codiddo
document.addEventListener("DOMContentLoaded", function() {
    // Seleccionamos el párrafo por su ID
    const parrafo = document.getElementById("parrafo-con-script-externo");

    // Aplicamos estilos con JavaScript
    parrafo.style.color = "pink";
    parrafo.style.fontSize = "20px";
    parrafo.style.backgroundColor = "black";
    parrafo.style.padding = "10px";
    parrafo.style.borderRadius = "5px";
});