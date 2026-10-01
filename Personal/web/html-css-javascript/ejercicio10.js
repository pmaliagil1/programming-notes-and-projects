// Definimos las variables
var precio_sin_iva = 123.45;
var iva = 21;

// Calculamos el precio final con IVA
var precio_iva = (precio_sin_iva * iva) / 100;  // Calculamos el IVA
var precio_final = precio_sin_iva + precio_iva; // Precio final con IVA

// Mostramos el resultado en el HTML
document.getElementById("precio_final").innerHTML = `El precio final con IVA es: €${precio_final.toFixed(2)}`;
