document.addEventListener("DOMContentLoaded", function() {
    var num1 = 7;
    var num2 = 4;

    var suma = num1 + num2;
    var resta = num1 - num2;
    var multiplicacion = num1 * num2;
    var division = num1 / num2;

    console.log("Suma: " + suma);
    console.log("Resta: " + resta);
    console.log("Multiplicación: " + multiplicacion);
    console.log("División: " + division);

    document.getElementById("resultado").innerHTML = `
        <strong>Suma:</strong> ${suma} <br>
        <strong>Resta:</strong> ${resta} <br>
        <strong>Multiplicación:</strong> ${multiplicacion} <br>
        <strong>División:</strong> ${division.toFixed(2)} <!-- Redondeamos a 2 decimales -->
    `;
});
