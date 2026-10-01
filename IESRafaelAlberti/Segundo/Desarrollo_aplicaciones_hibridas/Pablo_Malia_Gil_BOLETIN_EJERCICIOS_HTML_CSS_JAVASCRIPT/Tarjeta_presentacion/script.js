const foto = document.getElementById("fotoPablo");
const botonCambiarFoto = document.getElementById("boton1");
const botonModo = document.getElementById("botonModo");
const campoDeTexto = document.getElementById("campoDeTexto");
const botonPublicar = document.getElementById("boton2");
const comentarios = document.getElementById("comentarios");
const imagenes = [
    "../image/fotoPablo.jpg",
    "../image/foto2.jpg",
    "../image/foto3.jpg"
]

let indice = 0;

botonCambiarFoto.addEventListener("click", function () {
    foto.src = imagenes[indice];
    indice = (indice + 1) % imagenes.length;
});

botonModo.addEventListener("dblclick", function () {
    if (document.body.classList.contains("modo-oscuro")) {
        document.body.classList.remove("modo-oscuro");
    } else {
        document.body.classList.add("modo-oscuro");
    }});

botonPublicar.addEventListener("click", function () {
    const texto = campoDeTexto.value.trim();

    if (texto !== "") {
        const comentario = document.createElement("p");
        comentario.textContent = texto;

        comentarios.appendChild(comentario);
        campoDeTexto.value = "";
    }
});