const saludo = document.getElementById("saludo");
const foto = document.getElementById("foto");
const btn1 = document.getElementById('btn1');
const btn2 = document.getElementById("btn2");
const nombreAlumno = document.getElementById("nombreAlumno");
const btn5 = document.getElementById("btn5");
const btn3 = document.getElementById("btn3")
const btn4 = document.getElementById("btn4")
const imagenes = ['../image/foto1.jpg', '../image/foto2.jpg', '../image/foto3.jpg'];
let indice = 0;

console.log(saludo);

btn2.addEventListener('click', function() {
  saludo.style.color = 'blue';
});

nombreAlumno.addEventListener("mouseover", function(){
    nombreAlumno.style.fontSize = "30px";
})

btn5.addEventListener('click', function(){
  nombreAlumno.style.fontFamily = "Arial";
})

btn5.addEventListener('dblclick', function(){
  saludo.style.backgroundColor = 'lightgreen';
})

btn3.addEventListener('click', function() {
  const texto = campoTexto.value;
  saludo.textContent = texto;
});

btn4.addEventListener('click', function() {
  document.title = 'Listos para Capacitor';
});

btn1.addEventListener('click', function() {
  indice = (indice + 1) % imagenes.length;
  foto.src = imagenes[indice];
});